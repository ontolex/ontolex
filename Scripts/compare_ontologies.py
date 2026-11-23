"""Compare the generated ontology files with the hand-written ones.

For each module, reports the triples that are only in the hand-written file
(`Ontologies/<module>.owl`) and only in the generated file
(`<generated dir>/<module>.ttl`), grouped by term, as Markdown.

Usage:

    python Scripts/compare_ontologies.py generated [-o comparison.md]

Blank nodes are matched structurally, so restrictions and lists that are
equal are not reported. Requires `rdflib`.
"""
import argparse
import os
import sys
from collections import defaultdict

from rdflib import BNode, Graph, Literal
from rdflib.compare import graph_diff, to_isomorphic

MODULES = ["ontolex", "synsem", "decomp", "vartrans", "lime"]
MAX_TERMS = 60  # terms listed per direction and module before truncating


def short(graph, node):
    if isinstance(node, BNode):
        return "[]"
    if isinstance(node, Literal):
        text = str(node).replace("|", "\\|")
        text = text if len(text) <= 70 else text[:67] + "..."
        suffix = f"@{node.language}" if node.language else ""
        return f'"{text}"{suffix}'
    return graph.namespace_manager.normalizeUri(node)


def group(graph, triples):
    by_subject = defaultdict(list)
    for s, p, o in triples:
        by_subject[s].append((p, o))
    return by_subject


def section(graph, title, triples, out):
    by_subject = group(graph, triples)
    out.append(f"**{title}:** {len(triples)} triples in {len(by_subject)} terms\n")
    if not by_subject:
        return
    subjects = sorted(by_subject, key=lambda s: (isinstance(s, BNode), str(s)))
    for s in subjects[:MAX_TERMS]:
        # translations are summarized by language rather than listed
        langs = sorted({o.language for p, o in by_subject[s]
                        if isinstance(o, Literal) and o.language and o.language != "en"})
        others = [(p, o) for p, o in by_subject[s]
                  if not (isinstance(o, Literal) and o.language and o.language != "en")]
        line = f"- `{short(graph, s)}`"
        if langs:
            line += f" translations ({', '.join(langs)})"
        out.append(line)
        for p, o in sorted(others, key=lambda po: (str(po[0]), str(po[1]))):
            out.append(f"  - `{short(graph, p)}` {short(graph, o)}")
    if len(subjects) > MAX_TERMS:
        out.append(f"- ... and {len(subjects) - MAX_TERMS} more terms")
    out.append("")


def compare(generated_dir, hand_dir):
    out = ["# Generated vs hand-written ontologies\n"]
    summary = []
    details = []
    for module in MODULES:
        hand_path = os.path.join(hand_dir, module + ".owl")
        gen_path = os.path.join(generated_dir, module + ".ttl")
        hand, gen = Graph(), Graph()
        hand.parse(hand_path, format="xml")
        gen.parse(gen_path, format="turtle")
        _, only_hand, only_gen = graph_diff(to_isomorphic(hand), to_isomorphic(gen))
        only_hand, only_gen = list(only_hand), list(only_gen)
        summary.append(f"| {module} | {len(hand)} | {len(gen)} | {len(only_hand)} | {len(only_gen)} |")
        details.append(f"## {module}\n")
        if not only_hand and not only_gen:
            details.append("Identical.\n")
            continue
        merged = Graph()
        for prefix, ns in list(hand.namespaces()) + list(gen.namespaces()):
            merged.bind(prefix, ns, override=False)
        section(merged, "Only in hand-written", only_hand, details)
        section(merged, "Only in generated", only_gen, details)
    out.append("| module | hand-written | generated | only hand-written | only generated |")
    out.append("|---|---|---|---|---|")
    out.extend(summary)
    out.append("")
    out.extend(details)
    return "\n".join(out) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("generated", help="directory with the generated <module>.ttl files")
    parser.add_argument("--hand-written", default="Ontologies", metavar="DIR",
                        help="directory with the hand-written <module>.owl files (default: Ontologies)")
    parser.add_argument("-o", "--output", help="write the report to this file instead of standard output")
    args = parser.parse_args()
    report = compare(args.generated, args.hand_written)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report)
    else:
        sys.stdout.write(report)


if __name__ == "__main__":
    main()
