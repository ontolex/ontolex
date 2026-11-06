# OntoLex Model for Ontology-Lexica

The OntoLex (Ontology-Lexicon) model is a W3C community standard designed to represent the relationships between lexical information (words, phrases, morphology) and ontological concepts in RDF. It enables the integration of linguistic data with semantic web technologies, facilitating tasks such as multilingual knowledge representation, natural language processing, and semantic search.

At its core, OntoLex provides a structured way to describe how lexical entries (e.g., words or expressions) map to meanings (senses) and link to formal concepts in an ontology. The model includes several key modules, including `ontolex` for core lexical information, `lemon` for lexical senses, `decomp` for decomposition of multi-word expressions, `synsem` for syntactic and semantic properties, and `vartrans` for capturing lexical variation and translation.

By bridging the gap between lexicons and ontologies, OntoLex supports the development of interoperable, multilingual linguistic resources for the Semantic Web.

The following version of the specification have been published

* Version 1.0: https://www.w3.org/2016/05/ontolex/ (May 2016)

The live version of the specification is available at https://ontolex.github.io/ontolex/

## Building the Specification

The specification uses [ReSpec](https://respec.org/docs/) and is generated from the main Markdown file at `index.md`. The specification is automatically constructed by a GitHub action that runs on every push to the main branch. The action builds the specification and deploys it to https://ontolex.github.io/ontolex/

If you want to build it locally, you will need to install [PanDoc](https://pandoc.org/). You can then run the following command in the root directory of the repository:

```bash
pandoc --template respec.template -f markdown-auto_identifiers --wrap=none index.md -o index.html
python expand_tags.py index.html index.html
```

## Extracting the Ontology

The ontology is encoded in RDFa within the HTML specification. To extract the ontology, you can use a tool such as `rapper`


```bash
rapper -i rdfa -o turtle index.html > ontolex.ttl
```

## Building Examples

The examples are built using the `Examples` directory. Each example is a Turtle file
that can be converted using GraphViz. The examples can be built using the following command:

```bash
bash Examples/create_images.sh
```

## Contributing

We welcome contributions to the OntoLex specification. If you find issues, have suggestions, or want to contribute new examples, please open an issue or a pull request in the GitHub repository.

Modules can be proposed by any member and a working group and resources 
including GitHub will be set up by the chairs. Each module should have 
at least two chairs to lead the development. Any member of the group may 
propose a module on this mailing list.

Each module should meet for a monthly meeting that will be announced on 
this mailing list and published in this calendar:

https://calendar.google.com/calendar/u/1?cid=Nzc5NjIwZTcyNzljZDdhYmRiMDU5ODhhMWU3ZGNkOTcxMGMzMWVlZDJkYmE4N2ZlOTQ2MjhhNDEwODNiODQ0ZEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t

Modules will aim to produce a specification and use case document within 
six months of the start, and a draft specification within 12 months of 
the specification document.

The drafts will be reviewed by the community in 3 month cycles, in which 
comments will be solicited from the community group. Once the draft is 
stable (defined as not having received any comments during the last 
cycle), it will be released as a report of the CG.

