#!/bin/sh
# Build the specification and extract the ontology files from its RDFa.
#
# Usage (from the repository root): Scripts/extract_ontology.sh [output-dir]
#   (defaults to `generated`)
#
# Writes <module>.ttl and <module>.rdf for each module to the output directory,
# and a comparison with the hand-written files in Ontologies/ to
# <output-dir>/comparison.md. Needs pandoc, rapper (raptor2-utils) and the
# Python packages beautifulsoup4, rdflib and PyYAML. See README.md.

set -e

OUT="${1:-generated}"
HTML="$(mktemp --suffix=.html)"
TTL="$(mktemp --suffix=.ttl)"
trap 'rm -f "$HTML" "$TTL"' EXIT

mkdir -p "$OUT"

pandoc --template respec.template -f markdown-auto_identifiers --wrap=none index.md -o "$HTML"
python3 Scripts/expand_tags.py "$HTML" "$HTML"
rapper -i rdfa -o turtle "$HTML" > "$TTL"

python3 Scripts/build_ontology.py "$TTL" \
    --metadata index.md --translations Ontologies/translations \
    --split "$OUT" --check

python3 Scripts/compare_ontologies.py "$OUT" -o "$OUT/comparison.md"
echo "Wrote ontology files and comparison.md to $OUT" >&2
