# Style Guide for the OntoLex Specification

This guide describes how the specification in `index.md` is written, built and
checked. It covers the source format, how vocabulary terms are defined, examples
and their diagrams, wording and spelling, links and citations, and the checks to
run before opening a pull request.

The guide is written for this repository, which holds the core specification
and its five modules (*ontolex*, *synsem*, *decomp*, *vartrans* and *lime*). The
other OntoLex repositories each specify a single module, for example
[Morphology](https://github.com/ontolex/morph) and [Frequency, Attestation and
Corpus Information](https://github.com/ontolex/frequency-attestation-corpus-information).
The conventions apply to them as well. See
[Module repositories](#module-repositories) for the differences.

## Sources and outputs

| Source | Purpose |
|---|---|
| `index.md` | The specification: Pandoc Markdown with embedded HTML and RDFa |
| `respec.template` | The Pandoc template: HTML skeleton, ReSpec configuration, Mermaid script and CSS |
| `Examples/<module>/*.ttl` | One Turtle file per example; each is the source of the example's diagram |
| `Diagrams/` | Hand-drawn module overview figures and other images |
| `Ontologies/translations/<module>.csv` | Labels and comments in languages other than English |
| `Scripts/` | The build: `expand_tags.py`, `mermaid_lib.py`, `build_ontology.py`, `extract_ontology.sh` |

The specification is the single source of the ontology. The OWL files for each
module are generated from the RDFa in `index.md`, so a change to a definition in
the text is a change to the ontology, and the other way round. The hand-written
files in `Ontologies/` are not yet replaced by the generated ones and should not
be edited to fix the specification.

## Module repositories

A repository for a single module uses the same toolchain (Pandoc, the ReSpec
template, `expand_tags.py`, `rapper` and `build_ontology.py`) and the same
conventions for terms, wording, examples and checks. Their layout varies, and
these differences are expected:

- **One ontology.** The module has one namespace and produces one ontology file,
  so there is no splitting by module. The ontology metadata in the front matter
  describes that one module.
- **Paths.** The scripts may be at the repository root rather than in
  `Scripts/`, examples may be in `examples/` or `samples/`, and figures in
  `img/` or similar. Adapt the commands in this guide accordingly.
- **Copies of the scripts.** Each repository has its own copy of
  `expand_tags.py`, `build_ontology.py` and `respec.template`, and they have
  drifted. When a fix to one of them is general, for example to the namespace
  table or the qualified cardinality syntax, apply it to the other repositories
  too.
- **The other modules are external vocabularies.** A module refers to OntoLex
  terms (`ontolex:LexicalEntry`) as an external vocabulary. In the text, link to
  their definitions in the core specification
  (`[lexical entry](https://www.w3.org/2016/05/ontolex/#lexical-entry-class)`) rather
  than writing CURIEs. In entity blocks, the CURIE form is fine as long as the
  prefix is in the `expand_tags.py` namespace table.
- **Namespaces and versions.** Use the module's own namespace under
  `http://www.w3.org/ns/lemon/`, and the same current versions of other
  vocabularies as the core specification (for example LexInfo 3.0).

## Building

You need [Pandoc](https://pandoc.org/), `rapper` (from `raptor2-utils`) and
the Python packages `beautifulsoup4`, `rdflib` and `PyYAML`.

Build the HTML page from the repository root:

```bash
pandoc --template respec.template -f markdown-auto_identifiers --wrap=none index.md -o index.html
python Scripts/expand_tags.py index.html index.html
```

`expand_tags.py` expands the shorthand tags in the entity definitions into RDFa
and renders the example diagrams. If the output HTML is written outside the
repository root, pass `--base .` so that the example files can be found.

ReSpec and Mermaid run in the browser, so open the page through a local web
server (for example `python -m http.server`) rather than as a file, and wait
until ReSpec has finished.

Generate the ontology files:

```bash
Scripts/extract_ontology.sh generated
```

This builds the page, extracts the RDFa with `rapper`, and runs
`build_ontology.py`, which adds the translations, the module headers from the
front matter, `rdfs:isDefinedBy` and `vs:term_status`, and the declarations of
inverse properties, splits the result by module and checks it. It fails if a
check fails.

The GitHub action runs the same steps on every pull request and publishes the
page and the generated files when changes reach `master`.

## Document structure and ReSpec

- **Front matter.** The YAML block at the top of `index.md` holds the title, the
  editors (with `name`, `url`, `company` and `companyURL`) and, under
  `ontology`, the metadata of each module (title, description, version,
  creators, contributors, imports). This metadata ends up in the generated
  ontologies, so keep the contributor URLs working.
- **ReSpec configuration.** Status, `shortName`, `github` and `latestVersion`
  are set in `respec.template`, not in `index.md`.
- **Sections.** Each section is a `<section id="...">` with a Markdown heading
  inside it. Give every section a short, stable `id`. Anchors are part of the
  published URL, so do not rename them without a reason. `abstract` and `sotd`
  are the ReSpec abstract and status sections.
- **Auto identifiers are off** (`-f markdown-auto_identifiers`). Link to a
  section by its `id` (`[Lexical Concept](#lexical-concept)`), and check that
  the `id` exists.
- **No ReSpec errors or warnings.** A warning such as "Found definition for …,
  but nothing links to it" or a broken local link is a defect. Fix it rather
  than leaving it. See [Checks](#checks).

## Defining vocabulary terms

Every class and property is defined in an entity block. The `about` attribute
gives the term's IRI and `typeof` its type:

```html
<div class="entity" about="ontolex:evokes" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Evokes</objectProperty>

<div property="rdfs:comment"> The <dfn>evokes</dfn> property relates a lexical entry to one of the lexical concepts it evokes, i.e. the mental concept that speakers of a language might associate when hearing the lexical entry. </div>

<div class="description">
<domain>[=Lexical Entry=]</domain>
<range>[=Lexical Concept=]</range>
<inverse>[=is evoked by=]</inverse>
</div>
</div>
```

- **Type.** Use `owl:Class`, `owl:ObjectProperty` or `owl:DatatypeProperty`.
  The label element matches the type (`<class>`, `<objectProperty>` or
  `<datatypeProperty>`).
- **Label.** The English `rdfs:label` is in Title Case and plain English
  ("Lexical Concept", "Subject of Property"), never camelCase ("SynArg"). It must
  not repeat the label of another term. When a property would collide with a
  class, add "Property" ("Syntactic Argument Property").
- **Comment and `<dfn>`.** The `rdfs:comment` is one or more complete sentences.
  It contains the `<dfn>` that ReSpec links to, so the comment reads "The
  <dfn>x</dfn> property …" or "A <dfn>x</dfn> represents …". The `<dfn>` text is
  the term's name in lower-case English, and it is how every `[=x=]` reference
  finds the term. If the `<dfn>` text already ends in "property", do not add
  another "property" after it. Use `data-lt` for alternative names
  (`<dfn data-lt="OntoMap|Onto Map">ontology map</dfn>`).
- **Description.** Inside `<div class="description">` use the shorthand tags
  that `expand_tags.py` turns into RDFa:

  | Tag | Meaning |
  |---|---|
  | `<domain>`, `<range>` | `rdfs:domain`, `rdfs:range` |
  | `<subclass>`, `<subproperty>` | `rdfs:subClassOf`, `rdfs:subPropertyOf` |
  | `<inverse>` | `owl:inverseOf` |
  | `<equivalentClass>`, `<equivalentProperty>` | `owl:equivalentClass`, `owl:equivalentProperty` |
  | `<functional/>`, `<inverse-functional/>`, `<symmetric/>` | property characteristics |

  The tag content is one of the following:
  - a term reference (`[=Lexical Entry=]`);
  - a CURIE with a prefix that `expand_tags.py` knows (`skos:Concept`, `xsd:language`);
  - a full IRI;
  - an expression built from these:

  | Expression | Meaning |
  |---|---|
  | `A, B` | several values |
  | `A OR B` | `owl:unionOf` |
  | `p o q` | property chain |
  | `p only C` | `owl:allValuesFrom` |
  | `p min 1`, `p max 1`, `p exactly 1` | cardinality |
  | `p min 1 C` | qualified cardinality, with `owl:onClass` |

  A reference that does not resolve stops the build.
- **Inverse properties** are declared only through `<inverse>` on the forward
  property. `build_ontology.py` generates the inverse's declaration, domain,
  range and characteristic. To link to an inverse in the text, it needs an entry
  in `build_dfn_about_map` in `expand_tags.py`, as for `is evoked by`.
- **Characteristics in the text must match the formal definition.** Do not state
  in prose that a property is functional, transitive, etc. unless the entity
  block says so, and check the claim against the examples.
- **Terms not to be published.** All terms are generated as
  `vs:term_status "stable"`. A term that is not stable should not be defined in
  the specification.
- **Translations** go in `Ontologies/translations/<module>.csv`
  (`term,property,lang,text`), not in `index.md`.

## Wording

- **Refer to vocabulary terms in English, not in code.**
  - Terms defined in this specification are written as `[=term=]` links
    ("the [=evokes=] property", "a [=lexical concept=]").
  - Terms from other vocabularies are written as natural-language links to their
    definitions: `[SKOS Concept](http://www.w3.org/2004/02/skos/core#Concept)`,
    `[VoID Dataset](http://rdfs.org/ns/void#Dataset)`,
    `[SKOS 'in scheme' property](http://www.w3.org/2004/02/skos/core#inScheme)`.
  - Avoid camelCase words (`isEvokedBy`, `partOfSpeech`) and CURIEs
    (`skos:Concept`) in the running text.
- **Use code formatting only for literal syntax**: listings, `@prefix`
  declarations, IRIs the reader must type, and identifiers the text is explaining
  as syntax (`rdf:_1`, `rdf:_2`). Formulas such as
  `*Noun* ≡ ∃ partOfSpeech.NounPOS` are code and stay as written.
- **Modules** are named in italics (*synsem*, *vartrans*, *lime*), or by their
  full names ("the Syntax and Semantics module").
- **Example resources** mentioned in the text are in italics (*arg1*,
  *own_frame_transitive*).
- **Spelling is American English** ("behavior", "organization",
  "lexicalization"). Some British forms remain ("modelling", "organisation",
  "colour"); change them when editing the passage.
- **Write complete sentences**, and keep the module and term counts in the text
  ("the following five modules") in line with the document.

## Examples

Every example is an `aside` whose `src` names its Turtle file, followed by the
listing:

````markdown
<aside class="example" src="Examples/ontolex/example14.ttl">

```turtle
:lexical_entry a ontolex:LexicalEntry .
```

</aside>
````

- **One file per example.** Put it at `Examples/<module>/exampleN.ttl`. The file
  is the source of the diagram, and the listing is what readers see.
- **The listing and the file must describe the same graph.** The listing may omit
  the `@prefix` lines, which are given in the Conventions section. Apart from
  that, a listing parsed with the file's prefixes must be isomorphic to the file.
  Change both together. See [Checks](#checks).
- **Each listing must parse.** End every statement with `.`, prefix every local
  name (`:mother_form`, not `mother_form`), and use only declared prefixes.
- **Prefixes in the file:** declare every prefix the file uses, and use
  `@prefix : <#> .` for the example's own resources. Avoid relative IRIs such as
  `<cat>`.
- **Use current vocabularies:**
  - LexInfo 3.0, `http://www.lexinfo.net/ontology/3.0/lexinfo#`. Check that every
    term exists in it.
  - VoID, `http://rdfs.org/ns/void#`.
  - Other vocabularies at their current namespaces.
- **Introduce terms in order.** An example uses only terms that have been
  introduced by that point in the document, for example `dct:language` before
  `lime:language`.
- **Use real, resolvable IRIs for external resources:**
  - DBpedia resources in the `http://dbpedia.org/resource/` form, not
    `/page/`;
  - language codes as `http://id.loc.gov/vocabulary/iso639-2/eng` (three
    letters) or `http://lexvo.org/id/iso639-1/en`.

  If a resource cannot resolve, say so in the text or choose another one.
- **Close the `aside`.** An unclosed `aside` swallows the following text into the
  example.

### Diagrams

Example diagrams are generated, not drawn:

- At build time, `expand_tags.py` uses `Scripts/mermaid_lib.py` to turn the
  `.ttl` file into a Mermaid flowchart, and Mermaid renders it in the browser.
  Do not add PNGs for examples.
- Each node shows its name and type, a rule, then its literal properties.
  - Literals longer than 30 characters are cut and marked "...".
  - Blank nodes have no label.
  - Several properties between the same two nodes share one arrow
    (`constituent / rdf:_1`).
- **Layout:** diagrams with 12 or more nodes are laid out left to right, and
  smaller ones top down. An empty marker file next to the example overrides the
  layout:
  - `exampleN.LR` forces left to right;
  - `exampleN.elk` uses the ELK layout engine, which places edge labels better.
    Use it when labels overlap.
- **Readability.** Wide diagrams are scaled down to the page width, but not
  below 70% of their natural size; past that they scroll. If a diagram is still
  unreadable, simplify the example, try `.LR` or `.elk`, or leave the example
  without a `src` (no diagram).
- Check every new or changed example in the browser, in both light and dark mode.
- **Other figures** (the module overviews in `Diagrams/`) are hand-drawn. When a
  module changes, check that its figure still matches.
- **Template constraint.** `rapper` parses the built page as XML. Do not put
  tag-like text, such as a literal `<hr>`, in the scripts in `respec.template`,
  even in comments.

## Links and citations

- Prefer stable targets: W3C Recommendations, DOIs and the ACL Anthology over
  project home pages. Avoid links that are likely to disappear (personal pages,
  project sites, rendered views of ontologies).
- Use `https` where the site supports it, and link to the documentation of a
  vocabulary term rather than to the namespace document.
- If a resource is gone, link to its publication or an archive, or remove the
  link. Do not leave dead links.
- Link text is the name of the thing ("[Web Annotation Data
  Model](https://www.w3.org/TR/annotation-model/)"), not "here" or a bare URL.
  Placeholder IRIs (`…/iso639-3/xxx`) are written as code, not as links.
- ReSpec can generate a References section from `[[SHORTNAME]]` citations to
  [specref](https://www.specref.org/) (for example `[[RDF11-CONCEPTS]]`, or
  `[[!RDF11-CONCEPTS]]` for a normative reference). Papers not in specref can be
  added with `localBiblio` in the ReSpec configuration. The document currently
  cites by inline links. Use one style within a section.

## Checks

Run these checks before opening a pull request. The first two also run in CI.

1. **Build and extract.** `Scripts/extract_ontology.sh <dir>` must succeed. If
   you changed a definition, compare the generated files with the previous
   version and describe any change to the ontology in the pull request.
2. **ReSpec warnings.** Open the built page and run
   `document.respec.warnings` and `document.respec.errors` in the browser
   console. ReSpec also shows them in its pill menu. Both must be empty.
3. **Examples match their files.** For each `aside` with a `src`, parse the
   listing (with the file's prefixes) and the file with `rdflib` and check that
   they are isomorphic (`rdflib.compare.to_isomorphic`). Every listing must
   parse.
4. **External vocabularies.** Check that the terms used from LexInfo and other
   vocabularies exist in their current versions.
5. **Spelling.** Run a spell checker over the prose, for example
   `aspell --lang=en_US --mode=markdown list < index.md | sort | uniq -c`, and
   review the output by hand. Most hits are identifiers.
6. **Links.** Check that the external links resolve, for example with `curl -sIL`
   over the URLs in `index.md`. Some sites refuse scripts (403/429). Check those
   in a browser before reporting them.
7. **Diagrams.** Look at every new or changed example diagram in the built page.

## Pull requests

- Make one pull request per topic, against the current draft branch. Describe
  what changed and why, and how it was checked.
- Pull requests that target the draft branch do not close issues automatically.
  Close them by hand when the change is merged.
- Changes to the meaning of the model, such as a domain, a range or a
  characteristic, need agreement in the community group. Keep them in their own
  pull request, separate from editorial fixes.
