"""Build the OntoLex ontology files from the specification.

The ontology is authored as RDFa inside the specification (`index.md`) and
extracted with `rapper`. This script post-processes the extracted Turtle:

* removes ReSpec markup, such as `[=lexical entries=]`, which is turned into
  links when the page is rendered but is passed through unchanged by `rapper`,
  and normalizes whitespace in literals;
* declares the inverse properties that the specification only names, e.g.
  `ontolex:isSenseOf`, the inverse of `ontolex:sense`, from `owl:inverseOf`
  (domain, range and characteristics are derived from the property they invert);
* optionally adds translated labels and comments from CSV files
  (`--translations DIR`, one `<module>.csv` per module with the columns
  `term,property,lang,text`);
* optionally adds the metadata of each `owl:Ontology` from the YAML front
  matter of the specification (`--metadata index.md`);
* optionally splits the result into one file per module (`--split DIR`),
  written as both Turtle and RDF/XML;
* adds `rdfs:isDefinedBy` and `vs:term_status "stable"` to every class and
  property of a module;
* optionally checks the result for known problems (`--check`).

Usage (from the repository root):

    pandoc --template respec.template -f markdown-auto_identifiers --wrap=none index.md -o index.html
    python Scripts/expand_tags.py index.html index.html
    rapper -i rdfa -o turtle index.html | python Scripts/build_ontology.py \\
        --metadata index.md --translations Ontologies/translations --split generated --check

Without `--split` the combined graph is written to `-o` (default: standard
output). Requires `rdflib` and, for `--metadata`, `PyYAML`.
"""
import argparse
import csv
import os
import re
import sys

from rdflib import BNode, Graph, Literal, Namespace, URIRef
from rdflib.namespace import OWL, RDF, RDFS, XSD

LEMON = "http://www.w3.org/ns/lemon/"

NAMESPACES = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ontolex": LEMON + "ontolex#",
    "synsem": LEMON + "synsem#",
    "decomp": LEMON + "decomp#",
    "vartrans": LEMON + "vartrans#",
    "lime": LEMON + "lime#",
    "lexicog": LEMON + "lexicog#",
    "lexinfo": "http://www.lexinfo.net/ontology/2.0/lexinfo#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "semiotics": "http://www.ontologydesignpatterns.org/cp/owl/semiotics.owl#",
    "dcterms": "http://purl.org/dc/terms/",
    "dc": "http://purl.org/dc/elements/1.1/",
    "cc": "http://creativecommons.org/ns#",
    "vann": "http://purl.org/vocab/vann/",
    "vs": "http://www.w3.org/2003/06/sw-vocab-status/ns#",
    "voaf": "http://purl.org/vocommons/voaf#",
}

DC = Namespace(NAMESPACES["dc"])
CC = Namespace(NAMESPACES["cc"])
VANN = Namespace(NAMESPACES["vann"])
VOAF = Namespace(NAMESPACES["voaf"])
VS = Namespace("http://www.w3.org/2003/06/sw-vocab-status/ns#")

# ReSpec term references: [=term=] or [=term|display text=]
_TERM_REF = re.compile(r"\[=\s*(?:[^=\]|]*\|)?([^=\]]*?)\s*=\]")


def clean_text(text):
    """Remove ReSpec markup and normalize whitespace in a literal's text."""
    text = _TERM_REF.sub(r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def new_graph():
    graph = Graph()
    for prefix, uri in NAMESPACES.items():
        graph.bind(prefix, URIRef(uri))
    return graph


def clean_graph(graph):
    cleaned = new_graph()
    for s, p, o in graph:
        if isinstance(o, Literal) and o.datatype is None:
            o = Literal(clean_text(str(o)), lang=o.language)
        cleaned.add((s, p, o))
    return cleaned


def expand_curie(term):
    """Expand `prefix:local` using NAMESPACES (full URIs are returned as is)."""
    prefix, _, local = term.partition(":")
    if prefix in NAMESPACES and not local.startswith("//"):
        return URIRef(NAMESPACES[prefix] + local)
    return URIRef(term)


def _words(local):
    """`isSenseOf` -> `is sense of`."""
    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", local).lower()


def _copy_node(graph, node):
    """Return `node`, or a copy of it with fresh blank nodes if it is one."""
    if not isinstance(node, BNode):
        return node
    copy = BNode()
    for p, o in graph.predicate_objects(node):
        graph.add((copy, p, _copy_node(graph, o)))
    return copy


def add_inverses(graph):
    """Declare the properties that are only the target of an `owl:inverseOf`.

    The specification defines inverse properties in prose (`isSenseOf` is the
    inverse of `sense`) and states them with `<inverse>` on the original
    property. For each such property in the OntoLex namespaces this adds the
    declaration, label and comment, `owl:inverseOf` in both directions, the
    domain and range swapped, and the inverse characteristic (the inverse of a
    functional property is inverse functional and vice versa).

    Returns the list of the properties that were declared.
    """
    declared = set(graph.subjects(RDF.type, None))
    added = []
    for a, b in list(graph.subject_objects(OWL.inverseOf)):
        for new, original in ((b, a), (a, b)):
            if (isinstance(new, BNode) or isinstance(original, BNode)
                    or not str(new).startswith(LEMON) or new in declared):
                continue
            graph.add((new, RDF.type, OWL.ObjectProperty))
            graph.add((new, OWL.inverseOf, original))
            graph.add((original, OWL.inverseOf, new))
            label = _words(str(new).rsplit("#", 1)[1])
            graph.add((new, RDFS.label, Literal(label, lang="en")))
            graph.add((new, RDFS.comment, Literal(
                f"The inverse property of {str(original).rsplit('#', 1)[1]}.", lang="en")))
            for src, dst in ((RDFS.domain, RDFS.range), (RDFS.range, RDFS.domain)):
                for o in list(graph.objects(original, src)):
                    graph.add((new, dst, _copy_node(graph, o)))
            for src, dst in ((OWL.FunctionalProperty, OWL.InverseFunctionalProperty),
                             (OWL.InverseFunctionalProperty, OWL.FunctionalProperty)):
                if (original, RDF.type, src) in graph:
                    graph.add((new, RDF.type, dst))
            declared.add(new)
            added.append(new)
    return added


def add_translations(graph, directory):
    """Add labels and comments from `<directory>/*.csv`.

    Returns the rows that were skipped because their term is not in the
    graph, as (file, term, property, lang) tuples.
    """
    properties = {"rdfs:label": RDFS.label, "rdfs:comment": RDFS.comment}
    subjects = set(graph.subjects())
    orphans = []
    for name in sorted(os.listdir(directory)):
        if not name.endswith(".csv"):
            continue
        with open(os.path.join(directory, name), encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                term = expand_curie(row["term"])
                if term not in subjects:
                    orphans.append((name, row["term"], row["property"], row["lang"]))
                    continue
                graph.add((term, properties[row["property"]],
                           Literal(clean_text(row["text"]), lang=row["lang"])))
    return orphans


def read_front_matter(path):
    import yaml
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---\n"):
        raise ValueError(f"{path} has no YAML front matter")
    return yaml.safe_load(text[4:text.index("\n---\n")])


def module_graph_metadata(module, meta):
    """Return the triples of the `owl:Ontology` header of one module."""
    common = meta
    info = meta["modules"][module]
    ont = URIRef(LEMON + module)
    g = new_graph()
    g.add((ont, RDF.type, OWL.Ontology))
    g.add((ont, RDF.type, VOAF.Vocabulary))
    g.add((ont, OWL.versionInfo, Literal(str(common["version"]), datatype=XSD.decimal)))
    for key in ("modified", "issued"):
        g.add((ont, DC[key], Literal(str(common[key]), datatype=XSD.date)))
    g.add((ont, VANN.preferredNamespacePrefix, Literal(module)))
    g.add((ont, VANN.preferredNamespaceUri, Literal(LEMON + module + "#")))
    g.add((ont, DC.rights, Literal(common["rights"])))
    g.add((ont, DC.title, Literal(info["title"], lang="en")))
    g.add((ont, DC.description, Literal(info["description"], lang="en")))
    if "label" in info:
        g.add((ont, RDFS.label, Literal(info["label"], lang="en")))
    for person in common.get("creators", []):
        g.add((ont, DC.creator, URIRef(person)))
    for person in common.get("contributors", []):
        g.add((ont, DC.contributor, URIRef(person)))
    g.add((ont, DC.publisher, URIRef(common["publisher"])))
    g.add((ont, CC.license, URIRef(common["license"])))
    for imported in info.get("imports", []):
        g.add((ont, OWL.imports, URIRef(LEMON + imported)))
    if common.get("history"):
        g.add((ont, RDFS.comment, Literal(common["history"], lang="en")))
    return g


def split_graph(graph, modules):
    """Split `graph` by namespace into one graph per module.

    Blank nodes (e.g. restrictions and lists) follow the subject that refers
    to them. Returns (graphs, unassigned subjects).
    """
    graphs = {m: new_graph() for m in modules}
    unassigned = set()

    def add_with_bnodes(target, subject):
        for p, o in graph.predicate_objects(subject):
            target.add((subject, p, o))
            if isinstance(o, BNode):
                add_with_bnodes(target, o)

    for s in set(graph.subjects()):
        if isinstance(s, BNode):
            continue
        for m in modules:
            if str(s).startswith(LEMON + m + "#"):
                add_with_bnodes(graphs[m], s)
                break
        else:
            unassigned.add(s)
    return graphs, unassigned


def add_defined_by(graph, module):
    """Add `rdfs:isDefinedBy <module>` and `vs:term_status "stable"` to the
    classes and properties of a module."""
    graph.add((VS.term_status, RDF.type, OWL.AnnotationProperty))
    ontology = URIRef(LEMON + module)
    kinds = (OWL.Class, OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty)
    for kind in kinds:
        for s in list(graph.subjects(RDF.type, kind)):
            if str(s).startswith(LEMON + module + "#") and (s, RDFS.isDefinedBy, None) not in graph:
                graph.add((s, RDFS.isDefinedBy, ontology))
            if str(s).startswith(LEMON + module + "#"):
                graph.add((s, VS.term_status, Literal("stable")))


def check(graphs):
    """Return a list of problems found in the per-module graphs."""
    problems = []
    for module, g in graphs.items():
        if not any(True for _ in g.triples((None, RDF.type, OWL.Ontology))):
            problems.append(f"{module}: no owl:Ontology header")
        if len(g) < 20:
            problems.append(f"{module}: suspiciously small ({len(g)} triples)")
        for s, p, o in g:
            if str(p).startswith("file:"):
                problems.append(f"{module}: junk predicate {p} (is the <tag> expanded?)")
                break
        for s, p, o in g:
            if isinstance(o, Literal) and ("[=" in str(o) or "=]" in str(o)):
                problems.append(f"{module}: markup left in literal of {s}: {str(o)[:60]!r}")
        if module != "lime" and not any(True for _ in g.triples((None, RDFS.domain, None))):
            problems.append(f"{module}: no rdfs:domain triples")
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("input", nargs="?", default="-",
                        help="Turtle file to process (default: standard input)")
    parser.add_argument("-o", "--output", default="-",
                        help="output Turtle file for the combined graph (default: standard output)")
    parser.add_argument("--translations", metavar="DIR",
                        help="directory with translation CSV files")
    parser.add_argument("--metadata", metavar="INDEX_MD",
                        help="specification whose YAML front matter defines the ontology headers")
    parser.add_argument("--split", metavar="DIR",
                        help="write one Turtle and RDF/XML file per module to this directory")
    parser.add_argument("--check", action="store_true",
                        help="exit with an error if the result has known problems")
    args = parser.parse_args()

    data = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    graph = Graph()
    graph.parse(data=data, format="turtle")
    graph = clean_graph(graph)

    for term in add_inverses(graph):
        sys.stderr.write(f"Declared the inverse property {term}\n")

    if args.translations:
        orphans = add_translations(graph, args.translations)
        if orphans:
            sys.stderr.write(f"Warning: {len(orphans)} translations for terms not in the "
                             f"specification were skipped:\n")
            for name, term, prop, lang in orphans:
                sys.stderr.write(f"  {name}: {term} {prop} @{lang}\n")

    if args.split or args.check or args.metadata:
        if not args.metadata:
            parser.error("--split and --check need --metadata to know the modules")
        meta = read_front_matter(args.metadata)["ontology"]
        modules = list(meta["modules"])
        graphs, unassigned = split_graph(graph, modules)
        for m in modules:
            graphs[m] += module_graph_metadata(m, meta)
            add_defined_by(graphs[m], m)
        if unassigned:
            sys.stderr.write("Warning: terms not in any module were not written: "
                             + ", ".join(sorted(str(s) for s in unassigned)) + "\n")
        if args.split:
            os.makedirs(args.split, exist_ok=True)
            for m, g in graphs.items():
                g.serialize(os.path.join(args.split, m + ".ttl"), format="turtle")
                g.serialize(os.path.join(args.split, m + ".rdf"), format="xml")
        if args.check:
            problems = check(graphs)
            for problem in problems:
                sys.stderr.write("Error: " + problem + "\n")
            if problems:
                sys.exit(1)
        if args.split:
            return

    result = graph.serialize(format="turtle")
    if args.output == "-":
        sys.stdout.write(result)
    else:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)


if __name__ == "__main__":
    main()
