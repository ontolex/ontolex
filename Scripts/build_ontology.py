"""Clean up the ontology extracted from the specification's RDFa.

The ontology is authored as RDFa inside the specification and extracted
with `rapper`. The text of the definitions contains ReSpec markup, such as
`[=lexical entries=]`, which is turned into links when the page is rendered
but is passed through unchanged by `rapper`. Pandoc also leaves stray
newlines and indentation around some definitions. This script removes the
markup and normalizes whitespace in all literals, binds the usual prefixes
and writes the result as Turtle.

Usage (from the repository root):

    pandoc --template respec.template -f markdown-auto_identifiers --wrap=none index.md -o index.html
    python Scripts/expand_tags.py index.html index.html
    rapper -i rdfa -o turtle index.html | python Scripts/build_ontology.py -o ontolex.ttl

Requires `rdflib`.
"""
import argparse
import re
import sys

from rdflib import Graph, Literal, URIRef

NAMESPACES = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ontolex": "http://www.w3.org/ns/lemon/ontolex#",
    "synsem": "http://www.w3.org/ns/lemon/synsem#",
    "decomp": "http://www.w3.org/ns/lemon/decomp#",
    "vartrans": "http://www.w3.org/ns/lemon/vartrans#",
    "lime": "http://www.w3.org/ns/lemon/lime#",
    "lexicog": "http://www.w3.org/ns/lemon/lexicog#",
    "lexinfo": "http://www.lexinfo.net/ontology/2.0/lexinfo#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "semiotics": "http://www.ontologydesignpatterns.org/cp/owl/semiotics.owl#",
    "dcterms": "http://purl.org/dc/terms/",
}

# ReSpec term references: [=term=] or [=term|display text=]
_TERM_REF = re.compile(r"\[=\s*(?:[^=\]|]*\|)?([^=\]]*?)\s*=\]")


def clean_text(text):
    """Remove ReSpec markup and normalize whitespace in a literal's text."""
    text = _TERM_REF.sub(r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def clean_graph(graph):
    cleaned = Graph()
    for prefix, uri in NAMESPACES.items():
        cleaned.bind(prefix, URIRef(uri))
    for s, p, o in graph:
        if isinstance(o, Literal) and o.datatype is None:
            o = Literal(clean_text(str(o)), lang=o.language)
        cleaned.add((s, p, o))
    return cleaned


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("input", nargs="?", default="-",
                        help="Turtle file to clean (default: standard input)")
    parser.add_argument("-o", "--output", default="-",
                        help="output Turtle file (default: standard output)")
    args = parser.parse_args()

    data = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    graph = Graph()
    graph.parse(data=data, format="turtle")
    result = clean_graph(graph).serialize(format="turtle")
    if args.output == "-":
        sys.stdout.write(result)
    else:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
