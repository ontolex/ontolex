"""Write the Turtle file of each example from its listing in index.md.

The listings in index.md are the source of the examples. Each
`<aside class="example" src="Examples/...ttl">` contains one ```turtle
listing, and this script writes that listing to the file named by `src`,
preceded by the `@prefix` declarations it needs. The diagram of the example is
generated from that file at build time (see expand_tags.py).

The prefixes are taken from the listings of @prefix declarations outside the
examples (in the Conventions or Namespaces section), with `:` defaulting to
`<#>` for the example's own resources.
Prefixes that a listing declares itself are left to the listing. Only the
prefixes a listing uses are written.

Usage (from the repository root):
    python3 extract_examples.py [index.md]           write the files
    python3 extract_examples.py --check [index.md]   fail if any file
                                                             is out of date
"""
import argparse
import os
import re
import sys

from rdflib import Graph

EXAMPLE = re.compile(r'<(aside|div) class="example"([^>]*)>(.*?)</\1>', re.S)
SRC = re.compile(r'\bsrc="([^"]+\.ttl)"')
LISTING = re.compile(r"```turtle\n(.*?)```", re.S)
PREFIX = re.compile(r"@prefix\s+([A-Za-z][\w.-]*|):\s*<([^>]*)>\s*\.")


def common_prefixes(spec):
    """The prefixes the document declares for all examples, in order.

    These are the Turtle listings outside the examples that consist only of
    @prefix declarations (in the Conventions or Namespaces section). The empty
    prefix defaults to `<#>` unless one of them declares it.
    """
    outside = EXAMPLE.sub("", spec)
    prefixes = {"": "#"}
    found = False
    for listing in LISTING.findall(outside):
        lines = [l for l in listing.splitlines() if l.strip() and not l.strip().startswith("#")]
        if lines and all(PREFIX.fullmatch(l.strip()) for l in lines):
            found = True
            for name, iri in PREFIX.findall(listing):
                prefixes[name] = iri
    if not found:
        raise SystemExit("no listing of @prefix declarations found outside the examples")
    return prefixes


def used_prefixes(listing):
    """The prefixes used in a listing (ignoring IRIs, strings and comments)."""
    text = re.sub(r'"""(?:.|\n)*?"""|"(?:[^"\\\n]|\\.)*"', '""', listing)
    text = re.sub(r"<[^>\s]*>", "<>", text)
    text = re.sub(r"(?m)#.*$", "", text)
    text = re.sub(r"(?m)^\s*@prefix.*$", "", text)
    return set(re.findall(r"(?<![\w:/#.-])([A-Za-z][\w-]*|):(?=[\w-])", text))


def example_file(listing, prefixes):
    declared = {name for name, _ in PREFIX.findall(listing)}
    used = used_prefixes(listing)
    missing = used - declared - set(prefixes)
    if missing:
        raise ValueError("undeclared prefixes: " + ", ".join(sorted(missing)))
    header = ["@prefix %s: <%s> ." % (name, iri)
              for name, iri in prefixes.items() if name in used and name not in declared]
    return ("\n".join(header) + "\n\n" if header else "") + listing


def examples(spec):
    """(src, listing, line) for every example with a src attribute."""
    for m in EXAMPLE.finditer(spec):
        src = SRC.search(m.group(2))
        if not src:
            continue
        line = spec.count("\n", 0, m.start()) + 1
        listings = LISTING.findall(m.group(3))
        if len(listings) != 1:
            raise SystemExit("index.md:%d: expected one ```turtle listing in the example, found %d"
                             % (line, len(listings)))
        yield src.group(1), listings[0], line


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("spec", nargs="?", default="index.md")
    parser.add_argument("--check", action="store_true",
                        help="do not write; exit 1 if a file differs from its listing")
    args = parser.parse_args()

    with open(args.spec, encoding="utf-8") as f:
        spec = f.read()
    base = os.path.dirname(os.path.abspath(args.spec))
    prefixes = common_prefixes(spec)

    errors, stale, seen = 0, 0, set()
    for src, listing, line in examples(spec):
        where = "%s:%d (%s)" % (args.spec, line, src)
        if src in seen:
            print("%s: another example already uses this file" % where)
            errors += 1
            continue
        seen.add(src)
        try:
            text = example_file(listing, prefixes)
            Graph().parse(data=text, format="turtle")
        except Exception as e:  # rdflib raises various parser exceptions
            print("%s: %s" % (where, str(e).strip().splitlines()[0]))
            errors += 1
            continue
        path = os.path.join(base, src)
        current = open(path, encoding="utf-8").read() if os.path.exists(path) else None
        if current == text:
            continue
        stale += 1
        if args.check:
            print("%s: file is out of date; run %s" % (where, sys.argv[0]))
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
    # Every Turtle file under the example directories should come from a listing.
    for d in sorted({src.split("/")[0] for src in seen}):
        for root, _, names in os.walk(os.path.join(base, d)):
            for name in sorted(names):
                rel = os.path.relpath(os.path.join(root, name), base).replace(os.sep, "/")
                if name.endswith(".ttl") and rel not in seen:
                    print("%s: not used by any example in %s; delete it" % (rel, args.spec))
                    errors += 1
    print("%d examples, %d errors, %d %s" % (len(seen), errors, stale,
          "out of date" if args.check else "written"), file=sys.stderr)
    return 1 if errors or (stale and args.check) else 0


if __name__ == "__main__":
    sys.exit(main())
