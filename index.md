---
title: Lexicon Model for Ontologies
editor:
- name: John P. McCrae
  url: http://john.mccr.ae/
  company: University of Galway
---

<section id="abstract">
This document describes the lexicon model for ontologies (*lemon*) as a
main outcome of the work of the Ontology Lexicon (Ontolex) community
group.

Ontologies are an important component of the Semantic Web but current
ontology languages such as OWL and RDF(S) lack support for enriching
ontologies with linguistic information, in particular with information
concerning how ontology entities, i.e. properties, classes, individuals,
etc. can be realized in natural language. The model described in this
document aims to close this gap by providing a vocabulary that allows
ontologies to be enriched with information about how the vocabulary
elements described in them are realized linguistically, in particular in
natural languages.

OWL and RDF(S) rely on the RDFS label property to capture the relation
between a vocabulary element and its (preferred) lexicalization in a
given language. This lexicalization provides a lexical anchor that makes
the class, property, individual etc. understandable to a human user. The
use of a simple label for linguistic grounding as available in OWL and
RDF(S) is far from being able to capture the necessary linguistic and
lexical information that Natural Language Processing (NLP) applications
working with a particular ontology need.

The aim of *lemon* is to provide rich linguistic grounding for
ontologies. Rich linguistic grounding includes the representation of
morphological and syntactic properties of lexical entries as well as the
syntax-semantics interface, i.e. the meaning of these lexical entries
with respect to an ontology or vocabulary.
</section>

<section id="sotd">
This document is the first official report of the OntoLex community
group. It does not represent the view of single individuals but reflects
the consensus and agreement reach as part of the regular group
discussions. The report should be regarded as the official specification
of *lemon*.
</section>

<section id="overview">
## Overview

This document describes the specification of the *lexicon model for
ontologies* (*lemon*) as resulting from the work of the W3C Ontology
Lexicon Community Group.

The aim of the *lexicon model for ontologies* (*lemon*) is to provide
rich linguistic grounding for ontologies. Rich linguistic grounding
includes the representation of morphological and syntactic properties of
lexical entries as well as the syntax-semantics interface, i.e. the
meaning of these lexical entries with respect to an ontology or
vocabulary.

This document is structured into nine sections, where the first five
correspond to the main modules of *lemon*. Depending on their needs and
requirements, applications will use one or more of the modules mentioned
below, with the use of the OntoLex module being the minimal choice.

-   Ontology-lexicon interface (ontolex)
-   Syntax and Semantics (synsem)
-   Decomposition (decomp)
-   Variation and Translation (vartrans)
-   Linguistic Metadata (lime)

The last three sections do not describe the formal modelling but clarify

-   how one can add linguistic levels of description by means of
    external ontologies (section Linguistic Description)
-   how one can use *lemon* to describe lexical nets and other
    linguistic resources (section Lexical Nets)
-   the relation between *lemon* and the Simple Knowledge Organization
    System (SKOS), the Lexical Markup Model (LMF), and the Open
    Annotation Model (section Relation to Other Models)

<section id="introduction">
## Introduction

Ontologies are an important component of the Semantic Web but current
standards such as [OWL](http://www.w3.org/TR/owl-features/) only support
the addition of a simple label to entities in the ontology. It is not
currently possible to add inflected forms, different genders, usage
notes or create a full lexical resource such as Princeton WordNet. The
model described in this document aims to close this gap by providing a
vocabulary that allows ontologies to be enriched with information about
how the vocabulary elements described in them are realized
linguistically, in particular in natural languages, in order to render
ontologies suitable for supporting meaningful interaction with and
manipulation of them by human users and allowing NLP tools to be able
work with ontologies.

OWL and RDF(S) rely on a property `rdfs:label`{.cm} to capture the
relation between a vocabulary element and its (preferred) lexicalization
in a given language. This lexicalization provides a lexical anchor that
makes the concept, property, individual etc. understandable to a human
user. The use of a simple label for linguistic grounding as available in
OWL and RDF(S) is far from being able to capture the necessary
linguistic and lexical information that Natural Language Processing
(NLP) applications working with a particular ontology need. Such NLP
applications are for example:

-   Natural language generation systems that produce coherent discourses
    by verbalizing a set of triples
-   Question Answering systems that interpret user questions with
    respect to one or more ontologies
-   Text interpretation systems that extract triples with respect to one
    or more ontologies
-   Query interpretation and semantic search in information retrieval
    systems
-   Natural language based interfaces to ontologies, Semantic Web and
    Linked Data.

</section>

<section id="purpose">
## Purpose of the model

The purpose of the model is to support linguistic grounding of a given
ontology by adding information about how the elements in the vocabulary
of the ontology (individuals, classes, properties) are lexicalized in a
given natural language.

The model follows the principle of *semantics by reference*
\[[1](http://link.springer.com/article/10.1007/s10579-012-9182-3/fulltext.html)\]
in the sense that the semantics of a [=lexical
entry=] is expressed by reference to an
individual, class or property defined in the ontology. In some cases,
the lexicon itself can add named concepts which are not made explicit in
the ontology.

The model described here is open in the sense that it provides a core
vocabulary to add information about the linguistic realization of
ontology and vocabulary elements. This vocabulary can and should be
extended as required by a particular application. In particular, the
model abstracts from specific linguistic theory or category systems used
to describe the linguistic properties of lexical entries and their
syntactic behavior, encouraging reuse of existing data category systems
or linguistic ontologies. The model is thus agnostic with respect to the
linguistic theory and category systems. We make explicit in this
document at which points we refer to an external repository of data
categories or introduce novel sub-properties of properties defined in
*lemon*.

The model as presented here is inspired by many other models, in
particular the [Lexical Markup
Framework](http://www.lexicalmarkupframework.org) (LMF), the
[LexInfo](http://www.lexinfo.net/) model, the
[LIR](http://mayor2.dia.fi.upm.es/oeg-upm/index.php/en/technologies/63-lir)
model, the [Linguistic Meta
Model](http://ontologydesignpatterns.org/wiki/Ontology:LMM) (LMM), the
[semiotics.owl](http://www.ontologydesignpatterns.org/cp/owl/semiotics.owl)
ontology design pattern, and the [Senso
Comune](http://www.sensocomune.it) core model.

It is important to also mention what is not the purpose of the model:

-   It is not the goal of the model to replace any existing W3C Standard
    or Recommendation. In particular, this model is not intended to
    represent informal schemas such as taxonomies, thesauri and other
    classification schemes. This is covered by the
    [SKOS](http://www.w3.org/2004/02/skos/) model.
-   It is not a vocabulary for annotation of texts. If you need to add
    annotations to textual data, then please consider using the [Open
    Annotation](http://www.openannotation.org/spec/core/), [NLP
    Interchange Format
    (NIF)](http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core/nif-core.html)
    or the [Extremely Annotational RDF Markup
    (Earmark)](http://www.essepuntato.it/lode/owlapi/http://www.essepuntato.it/2008/12/earmark).
-   It is not a formal model of semantics but a model of lexicography.
    The model is not supposed to be used to define an ontology and
    instead assumes that there is a given ontology in some ontology
    language that is to be linked to a lexicon that expresses how the
    classes, properties and individuals defined in the ontology are
    lexicalized.
-   It does not contain a complete collection of linguistic categories.
    There are many existing efforts to provide a vocabulary to describe
    the properties of linguistic objects, such as
    [ISOcat](http://www.isocat.org), [the CLARIN concept
    registry](https://openskos.meertens.knaw.nl/ccr/browser/),
    [OLiA](http://purl.org/olia/),
    [GOLD](http://linguistics-ontology.org/),
    [LexInfo](http://www.lexinfo.net). The model builds on those and
    does not introduce any vocabulary of linguistic description.
-   The lexicon model for ontologies is a model for describing lexical
    resources in connection to ontologies, it is not a generic
    vocabulary supporting the publication of any sort of linguistic data
    including typological data, corpora, word lists etc. See the
    activities of the [Open Linguistics Working
    Group](http://linguistics.okfn.org/) for more information here.

</section>

<section id="namespaces">
## Namespaces

The model is available with the following sub-namespaces for the various
modules of the overall model:

-   <http://www.w3.org/ns/lemon/ontolex>\#
-   <http://www.w3.org/ns/lemon/synsem>\#
-   <http://www.w3.org/ns/lemon/decomp>\#
-   <http://www.w3.org/ns/lemon/vartrans>\#
-   <http://www.w3.org/ns/lemon/lime>\#

All modules may be imported from the following URL:

-   <http://www.w3.org/ns/lemon/all>

</section>

<section id="conventions">
## Conventions in this document

Throughout this document, we will use [Turtle RDF
Syntax](http://www.w3.org/TR/turtle/) to provide examples showing the
use of the model. Axioms will be paraphrased in natural language. We
will assume the following namespaces throughout all the examples in this
document:

```turtle
@prefix ontolex: <http://www.w3.org/ns/lemon/ontolex#> .
@prefix synsem: <http://www.w3.org/ns/lemon/synsem#> .
@prefix decomp: <http://www.w3.org/ns/lemon/decomp#> .
@prefix vartrans: <http://www.w3.org/ns/lemon/vartrans#> .
@prefix lime: <http://www.w3.org/ns/lemon/lime#> .
```

As we frequently also refer to other models, we will also assume the
following namespaces in all examples:

```turtle
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.
@prefix owl: <http://www.w3.org/2002/07/owl#>.
@prefix xsd: <http://www.w3.org/2001/XMLSchema#>.
@prefix skos: <http://www.w3.org/2004/02/skos#>.
@prefix dbr: <http://dbpedia.org/resource/>.
@prefix dbo: <http://dbpedia.org/ontology/>.
@prefix void: <http://rdfs.org/ns/void#>.
@prefix lexinfo: <http://www.lexinfo.net/ontology/2.0/lexinfo#>.
@prefix semiotics: <http://www.ontologydesignpatterns.org/cp/owl/semiotics.owl#>.
@prefix oils: <http://lemon-model.net/oils#>.
@prefix dct: <http://purl.org/dc/terms/>.
@prefix provo: <http://www.w3.org/ns/prov#>.
```

Furthermore, we require that instances of the model adhere to the [RDF
1.1 specification](http://www.w3.org/TR/rdf11-concepts/) and follow the
appropriate guidelines. In particular, we require that language tags
adhere to [Best Common Practice
47](http://www.rfc-editor.org/rfc/bcp/bcp47.txt), where tags are made up
of a language code (based on [ISO 639 codes part 1, 2, 3 or
5](http://www.iso.org/iso/home/standards/language_codes.htm)),
optionally followed by a hyphen and a [ISO
3166-1](http://www.iso.org/iso/iso-3166-1_decoding_table.html) country
code. Language tags may also contain further
[subtags](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry)
expressing e.g. the region, script or further variants.

In all examples in this document, the above namespaces are introduced
using an appropriate `@prefix`{.cm} statement. Prefixes are omitted from
class and object property definitions if the referenced ontology element
is defined in the same module. For cross-module and external references,
the prefix is made explicit.

In many examples we will use the
[LexInfo](http://www.lexinfo.net/ontology/2.0/lexinfo#) ontology to
describe grammatical categories, although this is not required for using
this model. The LexInfo model and guidelines for constructing and
extending linguistic category schemes are provided in the section on
[linguistic description](#linguistic-description).

</section>
</section>

<section id="core">

## Core

The following diagram depicts the core model (ontolex). Boxes represent
classes of the model. Arrows with filled heads represent object
properties, while arrows with empty heads represent subclass relations.
In arrows labeled \'X/Y\' (e.g. *sense/isSenseOf*), X (*sense*) is the
name of the object property and Y (*isSenseOf*) the name of the inverse
property.

![](Lemon_OntoLex_Core.png "Lemon_OntoLex_Core.png")

<section id="lexical-entries">

## Lexical Entries

The main class of the core of the lexicon ontology model is the class
[=lexical entry=]. A lexical entry is defined as
follows:

<div class="entity" about="ontolex:LexicalEntry" typeof="owl:Class">
<class property="rdfs:label" lang="en">Lexical Entry</class>

<div property="rdfs:comment">A <dfn>lexical entry</dfn> represents a unit of analysis of the lexicon that consists of a set of forms that are grammatically related and a set of base meanings that are associated with all of these forms. Thus, a lexical entry is a word, multiword expression or affix with a single part-of-speech, morphological pattern, etymology and set of senses. </div>

<div class="description">
<subclass>[=lexical form=] min 1 [=Form=], [=canonical form=] max 1 [=Form=], semiotics:Expression</subclass>
</div>
</div>

A [=Lexical Entry=] thus needs to be associated with at least one
[=form=], and has at most one [=canonical form=]  (see below).

Lexical entries are further specialized into [=words=],
[=affixes=]  (e.g., suffix, prefix, infix or circumfix)
and [=multiword expressions=].

<div class="entity" about="ontolex:Word" typeof="owl:Class">
<class property="rdfs:label" lang="en">Word</class>

<div property="rdfs:comment"> A <dfn>word</dfn> is a lexical entry that consists of a single token. </div>

<div class="description">
<subclass>[=Lexical Entry=]</subclass>
</div>
</div>

<div class="entity" about="ontolex:MultiwordExpression" typeof="owl:Class">
<class property="rdfs:label" lang="en">Multiword Expression</class>

<div property="rdfs:comment"> A <dfn>multiword expression</dfn> is a lexical entry that consists of two or more words. </div>

<div class="description">
<subclass>[=Lexical Entry=]</subclass>
</div>
</div>

<div class="entity" about="ontolex:Affix" typeof="owl:Class">
<class property="rdfs:label" lang="en">Affix</class>

<div property="rdfs:comment"> An <dfn>affix</dfn> is a lexical entry that represents a morpheme (suffix, prefix, infix, circumfix) that is attached to a word stem to form a new word. </div>

<div class="description">
<subclass>[=Lexical Entry=]</subclass>
</div>
</div>

The following Turtle code gives examples of lexical entries for each of
these subclasses, corresponding to the [=word=] *cat*, the [=multiword
expression=] *minimum finance lease payments* and the [=affix=] *anti*:

<aside class="example">
[![no
desc](Examples/ontolex/example1.png)](Examples/ontolex/example1.png)

```turtle
:cat a ontolex:Word

:minimum_finance_lease_payments a ontolex:MultiwordExpression

:anti- a ontolex:Affix
```
</aside>

</div>
</section>

<section id="forms">
## Forms

A [=lexical entry=] can be realized in different
ways from a grammatical point of view. These different grammatical
realizations are represented as different [=forms=] of
the lexical entry. A [=form=] is defined as follows:

<div class="entity" about="ontolex:Form" typeof="owl:Class">
<class property="rdfs:label" lang="en">Form</class>

<div property="rdfs:comment"> A <dfn>form</dfn> represents one grammatical realization of a lexical entry. </div>

<div class="description">
<subclass>[=written representation=] min 1 rdf:langString</subclass>
</div>
</div>

A lexical entry can be associated to one of its forms by means of the
[=lexical form=] property, although it is
preferred to use one of the two subproperties (canonical form, other
form) defined below.

<div class="entity" about="ontolex:lexicalForm" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Lexical Form</objectProperty>

<div property="rdfs:comment"> The <dfn>lexical form</dfn> property relates a lexical entry to one grammatical form variant of the lexical entry.
</div>

<div class="description">
<domain>[=Lexical Entry=]</domain>
<range>[=Form=]</range>
</div>
</div>

Each form can thus have one or more [=written representations=], defined as follows:

<div class="entity" about="ontolex:writtenRep" typeof="owl:DatatypeProperty">
<datatypeProperty property="rdfs:label" lang="en">Written Representation</datatypeProperty>

<div property="rdfs:comment"> The <dfn>written representation</dfn> property indicates the written representation of a form. </div>

<div class="description">
<domain>[=Form=]</domain>
<range>rdf:langString</range>
<subproperty>[=representation=]</subproperty>
</div>
</div>

A simple example of a lexical entry with two different forms
corresponding to two different grammatical realizations (as singular and
plural noun, respectively) is given below:

<aside class="example">
[![no
desc](Examples/ontolex/example2.png)](Examples/ontolex/example2.png){.tn}

```turtle
:lex_child a ontolex:LexicalEntry ;                                                
  ontolex:lexicalForm :form_child_singular, :form_child_plural .              
                                                                                
:form_child_singular a ontolex:Form ;                                          
  ontolex:writtenRep "child"@en .                                               
                                                                                
:form_child_plural a ontolex:Form ;                                            
  ontolex:writtenRep "children"@en .
```
</aside>

Different forms are used to express different morphological forms of the
entry. They should not be used to represent orthographical variants,
which should be represented as different representations of the same
form. For example, for the lexical entry *color*, we would have two
different representations of the same form, one for the British English
written representation *colour* and one for the American English written
representation *color*. Both representations have the same pronunciation
and the same meaning, so they are two different lexicographic variants
of the same lexical entry:

<aside class="example">
[![no
desc](Examples/ontolex/example3.png)](Examples/ontolex/example3.png){.tn}

```turtle
:lex_color a ontolex:LexicalEntry;
     ontolex:lexicalForm :form_color.

:form_color a ontolex:Form;
     ontolex:writtenRep "colour"@en-GB, "color"@en-US.
```
</aside>

The general property [=representation=] is used to assign strings to forms

<div class="entity" about="ontolex:representation" typeof="owl:DatatypeProperty">
<datatypeProperty property="rdfs:label" lang="en">Representation</datatypeProperty>

<div property="rdfs:comment"> The <dfn>representation</dfn> property indicates a string by which the form is represented according to some scheme. </div>

<div class="description">
<domain>[=Form=]</domain>
<range>rdf:langString</range>
</div>
</div>

A form may also have a [=phonetic representation=], indicating the
pronunciation of the word.

<div class="entity" about="ontolex:phoneticRep" typeof="owl:DatatypeProperty">
<datatypeProperty property="rdfs:label" lang="en">Phonetic Representation</datatypeProperty>

<div property="rdfs:comment"> The <dfn>phonetic representation</dfn> property indicates one phonetic representation of the pronunciation of the form using a scheme such as the International Phonetic Alphabet (IPA). </div>

<div class="description">
<domain>[=Form=]</domain>
<range>rdf:langString</range>
<subproperty>[=representation=]</subproperty>
</div>
</div>

The following example shows how we can represent two different
pronunciations for one form of a lexical entry using the example of
\"privacy\" (the phonetic code is based on IPA):

<aside class="example">
[![no
desc](Examples/ontolex/example4.png)](Examples/ontolex/example4.png){.tn}

```turtle
:lex_privacy a ontolex:LexicalEntry;
     ontolex:lexicalForm :form_privacy.

:form_privacy a ontolex:Form;
     ontolex:writtenRep "privacy"@en;
     ontolex:phoneticRep "ˈpɹɪv.ə.si"@en-US-fonipa;
     ontolex:phoneticRep "ˈpɹaɪ.və.si"@en-GB-fonipa.
```
</aside>

Phonetic representation and written representation are both considered
to be sub-properties of a more general property
[=representation=], for which users may define
extra sub-properties as required.

<div class="entity" about="ontolex:representation" typeof="owl:DatatypeProperty">
<datatypeProperty property="rdfs:label" lang="en">Representation</datatypeProperty>

<div property="rdfs:comment"> The **representation** property indicates a string by which the form is represented according to some scheme. </div>

<div class="description">
<domain>[=Form=]</domain>
<range>rdf:langString</range>
</div>
</div>

A [=lexical entry=] has a [=canonical form=], which is the form that primarily
identifies this entry and may be used as an index term in the lexicon.
The canonical form for single words is typically the lemma of that word
and is determined by lexicographic conventions for that language. In the
case of verbs, the lemma is typically the infinitive form or,
alternatively, the present tense of the verb (note that if an external
particle is used to indicate the infinitive as in English \"to play\",
this particle should be omitted). For nouns it is the noun singular
form, while for adjectives it is the positive (i.e., non-negative,
non-graded) form. For [=multiword expressions=] it is assumed that the same
principles of lemmatization are applied to the head word.

The property [=canonical form=] has a
[=lexical entry=] as domain and a
[=form=] as range. It is a subproperty of the property
[=lexical form=]. The canonical form has to be
unique, so that the property canonical form is declared to be
functional:

<div class="entity" about="ontolex:canonicalForm" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Canonical Form</objectProperty>

<div property="rdfs:comment"> The <dfn>canonical form</dfn> property relates a lexical entry to its canonical or dictionary form. This usually indicates the \"lemma\" form of a lexical entry. </div>

<div class="description">
<domain>[=Lexical Entry=]</domain>
<range>[=Form=]</range>
<subproperty>[=lexical form=]</subproperty>
</div>
</div>

It is recommended to use the <a href="http://www.w3.org/2000/01/rdf-schema#label">rdfs:label</a>
property to indicate the
canonical form in addition to the property
[=canonical form=] to ensure compatibility with
RDFS-based systems that expect an RDFS label. The lexical entries for
the noun *\"cat\"*, the verb *\"marry\"* and the adjective *\"high\"*
would look as follows (in Turtle syntax):

<aside class="example">
[![no
desc](Examples/ontolex/example5.png)](Examples/ontolex/example5.png){.tn}

```turtle
:lex_cat a ontolex:LexicalEntry, ontolex:Word;
     ontolex:canonicalForm :form_cat;
     rdfs:label "cat"@en .

:form_cat a ontolex:Form;
     ontolex:writtenRep "cat"@en .

:lex_marry a ontolex:LexicalEntry, ontolex:Word;
     ontolex:canonicalForm :form_marry;
     rdfs:label "marry"@en .

:form_marry a ontolex:Form;
     ontolex:writtenRep "marry"@en .

:lex_high a ontolex:LexicalEntry, ontolex:Word;
     ontolex:canonicalForm :form_high;
     rdfs:label "high"@en .

:form_high a ontolex:Form; 
    ontolex:writtenRep "high"@en .
```
</aside>

Of course, [=lexical entries=] need not to correspond to one [=word=] only, they
can correspond to a [=multiword expression=], as the following example for the
lexical entry \"intangible assets\" shows:

<aside class="example">
[![no
desc](Examples/ontolex/example6.png)](Examples/ontolex/example6.png){.tn}

```turtle
:lex_intangible_assets a ontolex:LexicalEntry, ontolex:MultiwordExpression;
     ontolex:canonicalForm :form_intangible_assets;
     rdfs:label "intangible assets"@en .

:form_intangible_assets a ontolex:Form;
     ontolex:writtenRep "intangible assets"@en .
```
</aside>

[=Multiword expressions=] are assumed to be distinct in both their full form
and any abbreviated form as there may be distinct lexical and pragmatic
properties associated with the two different forms of the term. Links
using other vocabularies such as
[LexInfo](http://www.lexinfo.net/ontology/2.0/lexinfo) may be used to
describe the type of abbreviation:

<aside class="example">
[![no
desc](Examples/ontolex/example6a.png)](Examples/ontolex/example6a.png){.tn}

```turtle
:nasa a ontolex:LexicalEntry, lexinfo:Acronym ;
  ontolex:canonicalForm :form_nasa ;
  lexinfo:abbreviationFor :national_aeronautics_and_space_administration;
  rdfs:label "NASA"@en .

:form_nasa a ontolex:Form ;
  ontolex:writtenRep "NASA"@en .

:national_aeronautics_and_space_administration a ontolex:LexicalEntry, ontolex:MultiwordExpression ;
  ontolex:canonicalForm :form_national_aeronautics_and_space_administration ;
  lexinfo:abbreviationFor :nasa ;
  rdfs:label "National Aeronautics and Space Administration"@en .

:form_national_aeronautics_and_space_administration a ontolex:Form ;
  ontolex:writtenRep "National Aeronautics and Space Administration"@en .
```
</aside>

It is also possible to indicate non-canonical forms of lexical entries,
which we call [=other forms=]:

<div class="entity" about="ontolex:otherForm" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Other Form</objectProperty>

<div property="rdfs:comment"> The <dfn>other form</dfn> property relates a lexical entry to a non-preferred (\"non-lemma\") form that realizes the given lexical entry. </div>

<div class="description">
<domain>[=Lexical Entry=]</domain>
<range>[=Form=]</range>
<subproperty>[=lexical form=]</subproperty>
</div>
</div>

For example, we may specify non-canonical forms of the verb *(to) marry*
as follows:

<aside class="example">
[![no
desc](Examples/ontolex/example7.png)](Examples/ontolex/example7.png){.tn}

```turtle
:lex_marry a ontolex:LexicalEntry ;
  ontolex:canonicalForm :form_marry ;
  ontolex:otherForm :form_marries .

:form_marry a ontolex:Form;
     ontolex:writtenRep "marry"@en .

:form_marries a ontolex:Form;
     ontolex:writtenRep "marries"@en .
```
</aside>

The morphological class (i.e., declension, conjugation or similar) may
be specified with the [=morphological
pattern=] property to avoid having to
list all regular forms of a word. The implementation of these patterns
is not specified by this document (but should be provided by some
suitable vocabulary such as [LIAM](http://lemon-model.net/liam)).

<div class="entity" about="ontolex:morphologicalPattern" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Morphological Pattern</objectProperty>

<div property="rdfs:comment"> The <dfn>morphological pattern</dfn> property indicates the morphological class of a word. </div>

<div class="description">
<domain>[=Lexical Entry=]</domain>
</div>
</div>

The following example shows how to indicate the conjugation for the
Latin words *amare* and *videre*.

<aside class="example">
[![no
desc](Examples/ontolex/example8.png)](Examples/ontolex/example8.png){.tn}

```turtle
:amare ontolex:morphologicalPattern :latin_first_conjugation ;
  ontolex:canonicalForm :amare_form .

:amare_form ontolex:writtenRep "amare"@la .

:videre ontolex:morphologicalPattern :latin_second_conjugation ;
  ontolex:canonicalForm :videre_form .

:videre_form ontolex:writtenRep "videre"@la
```
</aside>

</section>

<section id="semantics">
## Semantics

The model supports the specification of the meaning of [=lexical
entries=] with respect to a given ontology. The
lexicon model for ontologies follows the paradigm of *semantics by
reference* in the sense that the meaning of a lexical entry is specified
by pointing to the ontological concept that captures or represents its
meaning.

The property [=denotes=] is defined as follows:

<div class="entity" about="ontolex:denotes" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Denotes</objectProperty>

<div property="rdfs:comment"> The <dfn>denotes</dfn> property relates a lexical entry to a predicate in a given ontology that represents its meaning and has some denotational or model-theoretic semantics. </div>

<div class="description">
<domain>[=Lexical Entry=]</domain>
<range>rdfs:Resource</range>
<subproperty>semiotics:denotes</subproperty>
</div>
</div>

For the [=lexical entries=] *cat* and *marriage*, the meaning could be
expressed by pointing to the corresponding DBpedia resources:

<aside class="example">
[![no
desc](Examples/ontolex/example9.png)](Examples/ontolex/example9.png){.tn}

```turtle
:lex_cat a ontolex:LexicalEntry;
   ontolex:canonicalForm :form_cat;
   ontolex:denotes <http://dbpedia.org/resource/Cat>.

:form_cat a ontolex:Form;
   ontolex:writtenRep "cat"@en.

:lex_marriage a ontolex:LexicalEntry;
   ontolex:canonicalForm :form_marriage;
   ontolex:denotes <http://dbpedia.org/resource/Marriage>.

:form_marriage a ontolex:Form;
   ontolex:writtenRep "marriage"@en .
```
</aside>

The following example shows how we can model the fact that a word is
ambiguous with respect to the meanings it denotes, for example the word
\'troll\' can refer both to a mythical creature and to someone who makes
inflammatory posts on the internet. These two meanings can be easily
captured as shown in the following example:

<aside class="example">
[![no
desc](Examples/ontolex/example10.png)](Examples/ontolex/example10.png){.tn}

```turtle
:troll a ontolex:LexicalEntry ;
  ontolex:denotes <http://dbpedia.org/resource/Troll> ;
  ontolex:denotes <http://dbpedia.org/resource/Internet_troll> .
```
</aside>

Two terms may be different lexical entries if they are distinct in
part-of-speech, gender, inflected forms or etymology. For example the
following words with lemma \'bank\' are all considered distinct:

<aside class="example">
[![no
desc](Examples/ontolex/example10a.png)](Examples/ontolex/example10a.png){.tn}

```turtle
:bank1_en a ontolex:LexicalEntry ;
  dct:language <http://id.loc.gov/vocabulary/iso639-2/eng>, <http://lexvo.org/id/iso639-1/en> ;
  lexinfo:partOfSpeech lexinfo:noun ;
  lexinfo:etymologicalRoot :banque_frm ;
  ontolex:denotes <http://dbpedia.org/resource/Bank> .

:bank2_en a ontolex:LexicalEntry ;
  dct:language <http://id.loc.gov/vocabulary/iso639-2/eng>, <http://lexvo.org/id/iso639-1/en> ;
  lexinfo:partOfSpeech lexinfo:noun ;
  lexinfo:etymologicalRoot :hobanca_ang ;
  ontolex:denotes <http://dbpedia.org/resource/Bank_(geographic)> .

:bank3_en a ontolex:LexicalEntry ;
  dct:language <http://id.loc.gov/vocabulary/iso639-2/eng>, <http://lexvo.org/id/iso639-1/en> ;
  lexinfo:partOfSpeech lexinfo:verb ;
  lexinfo:etymologicalRoot :hobanca_ang ;
  ontolex:denotes <http://dbpedia.org/resource/Banked_turn> .

:bank1_de a ontolex:LexicalEntry ;
  dct:language <http://id.loc.gov/vocabulary/iso639-2/de>, <http://lexvo.org/id/iso639-1/de> ;
  lexinfo:partOfSpeech lexinfo:noun ;
  lexinfo:gender lexinfo:feminine ;
  ontolex:denotes <http://dbpedia.org/resource/Bank> ;
  ontolex:otherForm :banken .

:banken ontolex:writtenRep "Banken"@de ;
  lexinfo:number lexinfo:plural .

:bank2_de a ontolex:LexicalEntry ;
  odct:language <http://id.loc.gov/vocabulary/iso639-2/de>, <http://lexvo.org/id/iso639-1/de> ;
  lexinfo:partOfSpeech lexinfo:noun ;
  lexinfo:gender lexinfo:feminine ;
  ontolex:denotes <http://dbpedia.org/resource/Bench_(furniture)> ;
  ontolex:otherForm :baenke .

:baenke ontolex:writtenRep "Bänke"@de ;
  lexinfo:number lexinfo:plural .
```
</aside>

Note that the target of a denotation does not need to be an individual
in the ontology but may also refer to a class, property or datatype
property defined by the ontology. The model is agnostic with respect to
the ontology language used to express the ontological meaning referred
to. The assumption is merely that the entity in the range represents
some predicate that has a denotational semantics in some formal logical
system.

Properties in the model for linking to ontologies have an inverse
property named as \"is *x*-ed by\", where *x* is the original property
name to enable the lexicon to be defined in an ontology focused manner.
In the case of denotes this property is <dfn>is denoted by</dfn>.

In some cases the meaning of a lexical entry is not explicit in the
given ontology. Yet, to represent the meaning of a lexical entry we
might want to create a new class at the interface between lexicon and
ontology by reusing atomic ontological entities defined in the ontology
in question. For example, we might want to express the meaning of an
adjective by creating an anonymous restriction class at the level of the
lexicon-ontology interface. This is illustrated below for the adjective
\"female\" expressing the membership of an anonymous class
$∃gender.\{female\}$:

<aside class="example">
[![no
desc](Examples/ontolex/example10b.png)](Examples/ontolex/example10b.png){.tn}

```turtle
:female a ontolex:LexicalEntry; 
  lexinfo:partOfSpeech lexinfo:adjective;
  ontolex:canonicalForm :female_canonical_form;
  ontolex:sense :female_sense.

:female_canonical_form ontolex:writtenRep "female"@en.

:female_sense ontolex:reference [
    a owl:Restriction;
    owl:onProperty <http://dbpedia.org/ontology/gender> ;
    owl:hasValue <http://dbpedia.org/resource/Female> ] ;
  synsem:isA :female_arg .
```
</aside>

</section>

<section id="lexical-sense-reference">
## Lexical Sense & Reference

For many practical modelling situations, the
[=denotes=] property is not sufficient to capture the
precise linking between a [=lexical entry=] and
its meaning with respect to a given ontology. Thus, lemon introduces an
intermediate element called [=lexical sense=] to
capture the particular sense of a word that refers to the particular
ontology entity. The [=lexical entry=] is linked
to a [=lexical sense=] by means of the
[=sense=] property and the [=lexical sense=] is linked to the ontology by means of
the [=reference=] property. The chain
[=sense=] ∘ [=reference=] is
equivalent to the property [=denotes=] introduced
above.

<div class="entity" about="ontolex:LexicalSense" typeof="owl:Class">
<class property="rdfs:label" lang="en">Lexical Sense</class>

<div property="rdfs:comment"> A <dfn>lexical sense</dfn> represents the lexical meaning of a lexical entry when interpreted as referring to the corresponding ontology element. A lexical sense thus represents a reification of a pair of a uniquely determined lexical entry and a uniquely determined ontology entity it refers to. A link between a lexical entry and an ontology entity via a Lexical Sense object implies that the lexical entry can be used to refer to the ontology entity in question. </div>

<div class="description">
<subclass>[=sense=] min 1 [=Lexical Entry=], [=reference=] exactly 1 rdfs:Resource, [=is sense of=] exactly 1 [=Lexical Entry=], semiotics:Meaning</subclass>
</div>
</div>

Via the lexical sense object we can attach additional properties to a
pair of lexical entry and ontological predicate that it denotes to
describe under which conditions (context, register, domain, etc.) it is
valid to regard the lexical entry as having the ontological entity as
meaning. For example, we may wish to express the usages of the word
\"consumption\" in terms of the topic and diachronic usage of the word.
As shown in the following example, we can use the Dublin Core property
*subject* to indicate the topic of the Sense. The example also shows how
to use the property *dating* defined in the LexInfo ontology to specify
that the fourth sense of consumption is outdated.

<aside class="example">
[![no
desc](Examples/ontolex/example11.png)](Examples/ontolex/example11.png){.tn}

```turtle
:lex_consumption a ontolex:LexicalEntry;
   ontolex:canonicalForm :form_consumption;
   ontolex:sense :consumption_sense1;
   ontolex:sense :consumption_sense2;
   ontolex:sense :consumption_sense3;
   ontolex:sense :consumption_sense4 .

:form_consumption ontolex:writtenRep "consumption"@en.

:consumption_sense1 a ontolex:LexicalSense;
  dct:subject <http://dbpedia.org/resource/Ecology> ;
  ontolex:reference <http://dbpedia.org/resource/Consumption_(ecology)> .

:consumption_sense2 a ontolex:LexicalSense;
  dct:subject <http://dbpedia.org/resource/Anatomy> ;
  ontolex:reference <http://dbpedia.org/resource/Ingestion> .

:consumption_sense3 a ontolex:LexicalSense;
   dct:subject <http://dbpedia.org/resource/Economics> ;
   ontolex:reference <http://dbpedia.org/resource/Consumption_(economics)> .

:consumption_sense4 a ontolex:LexicalSense;
   dct:subject <http://dbpedia.org/resource/Medicine> ;
   lexinfo:dating lexinfo:old ;
   ontolex:reference <http://dbpedia.org/resource/Tuberculosis> .
```

</aside>

The lexical sense has a single lexical entry and a single reference in
the ontology. As a consequence, the properties \"sense\" and
\"reference\" are defined as inverse functional and functional,
respectively.

<div class="entity" about="ontolex:sense" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Sense</objectProperty>

<div property="rdfs:comment"> The <dfn>sense</dfn> property relates a lexical entry to one of its lexical senses.
</div>

<div class="description">
<domain>[=Lexical Entry=]</domain>
<range>[=Lexical Sense=]</range>
<inverse>[=is sense of=]</inverse>
<inverse-functional/>
</div>
</div>

The inverse of the [=sense=] property is <dfn>is sense of</dfn>, which relates a
[=lexical sense=] to the [=lexical entry=].

<div class="entity" about="ontolex:reference" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Reference</objectProperty>

<div property="rdfs:comment"> The <dfn>reference</dfn> property relates a lexical sense to an ontological predicate that represents the denotation of the corresponding lexical entry. </div>

<div class="description">
<domain>[=Lexical Sense=] OR [=Onto Map=]</domain>
<range>rdfs:Resource</range>
<inverse>[=is reference of=]</inverse>
<functional/>
</div>
</div>

The inverse of [=reference=] is <dfn>is reference of</dfn>, which relates an
ontology element to the [=lexical sense=] that refers to it.

</section>

<section id="usage">
## Usage

The interpretation of a word ([=lexical entry=]) with respect to a meaning
defined in a given ontology is often modulated by usage conditions or
pragmatic implications in particular due to *register*, *connotations*
or *meaning nuances* of a word. For example, consider as an example the
French words \'rivière\' and \'fleuve\', which refer to rivers flowing
into a sea and flowing into other rivers, respectively. As corresponding
ontological classes to capture the specific meanings of these French
words might not be available in the ontology, these meaning nuances can
be specified using the property [=usage=], which allows
information to be captured related to usage conditions and pragmatic
implications under which the lexical entry can be used to refer to the
ontological meaning in question. These usage conditions are not
introduced *instead of* a formally defined sense but complement the
corresponding sense by additional information describing the usage of
the lexical entry.

How exactly constraints on the usage of senses are defined is not
specified by *lemon*. Yet, we give an example below that shows how to
model the lexical meaning of \'rivière\' and \'fleuve\' when used to
refer to the DBpedia class [River](http://dbpedia.org/ontology/River):

<aside class="example">
[![no
desc](Examples/ontolex/example12.png)](Examples/ontolex/example12.png){.tn}

```turtle
:riviere a ontolex:LexicalEntry ;
  ontolex:sense :riviere_sense .

:fleuve a ontolex:LexicalEntry ;
  ontolex:sense :fleuve_sense .

:riviere_sense ontolex:reference <http://dbpedia.org/ontology/River> ;
  ontolex:usage [ 
    rdf:value "A riviere is a river that flows into another river"@en
  ] .

:fleuve_sense ontolex:reference <http://dbpedia.org/ontology/River>;
  ontolex:usage [
    rdf:value "A fleuve is a river that flows into the sea"@en
  ] .
```

</aside>

<div class="entity" about="ontolex:usage" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Usage</objectProperty>

<div property="rdfs:comment"> The <dfn>usage</dfn> property indicates usage conditions or pragmatic implications when using the lexical entry to refer to the given ontological meaning. </div>

<div class="description">
<domain>[=Lexical Sense=]</domain>
<range>rdfs:Resource</range>
</div>
</div>

</section>

<section id="lexical-concept">
## Lexical Concept

We have seen above how to capture the fact that a certain lexical entry
can be used to denote a certain ontological predicate. We capture this
by saying that the lexical entry [=denotes=] the
class or ontology element in question. However, sometimes we would like
to express the fact that a certain lexical entry
[=evokes=] a certain mental concept rather than that
it refers to a class with a formal interpretation in some model. Thus,
in lemon we introduce the class [=Lexical
Concept=] that represents *a mental
abstraction, concept or unit of thought that embodies the meaning of one
or more lexical entries.* Lexical Concepts also support the
identification of synonyms, as different lexical entries having senses
referring to the same Lexical Concept are considered to be synonym. A
[=lexical concept=] is thus a subclass of
[skos:Concept](http://www.w3.org/2004/02/skos/core#Concept).

<div class="entity" about="ontolex:LexicalConcept" typeof="owl:Class">
<class property="rdfs:label" lang="en">Lexical Concept</class>

<div property="rdfs:comment"> A <dfn>lexical concept</dfn> represents a mental abstraction, concept or unit of thought that embodies the meaning of one of more lexical entries. </div>

<div class="description">
<subclass>skos:Concept</subclass>
</div>
</div>

The lexical entry is said to [=evoke=] a particular
lexical concept, similar to how a lexical entry
[=denotes=] an ontology reference.

<div class="entity" about="ontolex:evokes" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Evokes</objectProperty>

<div property="rdfs:comment"> The <dfn>evokes</dfn> property relates a lexical entry to one of the lexical concepts it evokes, i.e. the mental concept that speakers of a language might associate when hearing the lexical entry. </div>

<div class="description">
<domain>[=Lexical Entry=]</domain>
<range>[=Lexical Concept=]</range>
<inverse>[=is evoked by=]</inverse>
<inverse-functional/>
</div>
</div>

The inverse of [=evokes=] is <dfn>is evoked by</dfn>, which relates a
[=lexical concept=] to the [=lexical entry=] that evokes it. The
[=evokes=] property is inverse functional, which means that a
[=lexical concept=] can be evoked by at most one
[=lexical entry=].

The evoked concept is different from the reference in the ontology, as
the reference primarily gives an interpretation of a word in terms of
the identifiers that would be generated by the semantic parsing of the
sentence. For example if we were to understand the sentence *John F.
Kennedy died in 1963*. we may understand the verb \"die (in)\" as
generating the URI [deathDate](http://dbpedia.org/ontology/deathDate)
within a SPARQL query. However, we might also want to record the actual
lexical sense of the word with respect to a mental lexicon, in which
*die* evokes the event of dying, as modelled in the following example:

<aside class="example">
[![no
desc](Examples/ontolex/example13.png)](Examples/ontolex/example13.png){.tn}

```turtle
:die a ontolex:Word ;
     ontolex:denotes <http://dbpedia.org/ontology/deathDate> ;
     ontolex:evokes  :Dying .
```

</aside>

We can link a lexical concept to a lexical sense that lexicalizes the
concept via the property [=lexicalized
sense=]:

<div class="entity" about="ontolex:lexicalizedSense" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Lexicalized Sense</objectProperty>

<div property="rdfs:comment"> The <dfn>lexicalized sense</dfn> property relates a lexical concept to a corresponding lexical sense that lexicalizes the concept. </div>

<div class="description">
<domain>[=Lexical Concept=]</domain>
<range>[=Lexical Sense=]</range>
<inverse>[=is lexicalized sense of=]</inverse>
</div>
</div>

The inverse of [=lexicalized sense=] is
<dfn>is lexicalized sense of</dfn>, which relates a
[=lexical sense=] to the [=lexical concept=] that it lexicalizes. 

A simple example involving the use of a lexical concept is the
following:

<aside class="example">
[![no
desc](Examples/ontolex/example14.png)](Examples/ontolex/example14.png){.tn}

```turtle
:temporary_change_of_possession a ontolex:LexicalConcept;
     ontolex:lexicalizedSense :borrow_sense;
     ontolex:lexicalizedSense :lend_sense;
     ontolex:isEvokedBy :borrow_le;
     ontolex:isEvokedBy :lend_le.

:borrow_le a ontolex:LexicalEntry;
     ontolex:sense :borrow_sense;
     ontolex:evokes :temporary_change_of_possession.

:lend_le a ontolex:LexicalEntry;
    ontolex_sense :lend_sense;
    ontolex:evokes :temporary_change_of_possession.
```

</aside>

Similarly, we can link a lexical concept to a reference in the ontology
by means of the [=concept=] property:

<div class="entity" about="ontolex:concept" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Concept</objectProperty>

<div property="rdfs:comment"> The <dfn>concept</dfn> property relates an ontological entity to a lexical concept that represents the corresponding meaning. </div>

<div class="description">
<domain>rdfs:Resource</domain>
<range>[=Lexical Concept=]</range>
<inverse>[=is concept of=]</inverse>
</div>
</div>

The inverse of [=concept=] is <dfn>is concept of</dfn>, which relates a
[=lexical concept=] to the ontology element that it represents.

The combined usage of the properties denotes, sense, evokes, concept and
lexicalized sense is demonstrated in the example below for the case of a
lexical resource such as Princeton WordNet. Roughly, the synsets in a
wordnet correspond to a lexical concept in lemon. The modelling would
thus look as follows:

<aside class="example">
[![no
desc](Examples/ontolex/example15.png)](Examples/ontolex/example15.png){.tn}

```turtle
:cat_lex a ontolex:LexicalEntry ;                                               
  ontolex:canonicalForm :cat_form ;
  ontolex:sense :cat_sense ;
  ontolex:denotes <http://dbpedia.org/resource/Cat> ;
  ontolex:evokes pwn:102124272-n .

:cat_form ontolex:writtenRep "cat"@en .

:cat_sense a ontolex:LexicalSense ;
  ontolex:reference <http://dbpedia.org/resource/Cat> ;
  ontolex:isLexicalizedSenseOf pwn:102124272-n ;
  ontolex:isSenseOf :cat_lex .

<http://dbpedia.org/resource/Cat>
  ontolex:concept pwn:102124272-n ;
  ontolex:isReferenceOf :cat_sense ;
  ontolex:isDenotedBy :cat_lex .

pwn:102124272-n a ontolex:LexicalConcept;
  ontolex:isEvokedBy :cat_lex ;
  ontolex:lexicalizedSense :cat_sense ;
  ontolex:isConceptOf <http://dbpedia.org/resource/Cat> .
```

</aside>

A definition can be added to a [=lexical
concept=] as a *gloss* by using the
[skos:definition](http://www.w3.org/2004/02/skos/core#definition)
property.

In addition to organizing a lexicon by lexical entries, we may
alternatively create a lexicon of concepts, by means of the the [=concept
set=] class, defined as follows:

<div class="entity" about="ontolex:ConceptSet" typeof="owl:Class">
<class property="rdfs:label" lang="en">Concept Set</class>

<div property="rdfs:comment"> A <dfn>concept set</dfn> represents a collection of lexical concepts. </div>

<div class="description">
<subclass>skos:ConceptScheme, void:Dataset</sub>
<equivalentClass>skos:inScheme min 1 [=Lexical Concept=]</equivalentClass>
</div>
</div>

In this way lexicons can be ordered onomasiologically, that is by
meanings rather than by lemmas. The concept set is a special type of
[skos:ConceptScheme](http://www.w3.org/2004/02/skos/core#ConceptScheme).
A [=lexical concept=] is linked to a
ConceptSet using the property
[skos:inScheme](http://www.w3.org/2004/02/skos/core#inScheme)

<aside class="example">
[![no
desc](Examples/ontolex/example17.png)](Examples/ontolex/example17.png){.tn}

```turtle
:conceptLexicon a ontolex:ConceptSet .

:consumption1 a ontolex:LexicalConcept ;
  ontolex:isConceptOf <http://dbpedia.org/resource/Tuberculosis> ;
  skos:definition "Tuberculosis, MTB, or TB (short for tubercle bacillus), in the past also called phthisis, phthisis pulmonalis, or consumption, is a widespread, and in many cases fatal, infectious disease caused by various strains of mycobacteria, usually Mycobacterium tuberculosis. Tuberculosis typically attacks the lungs, but can also affect other parts of the body. It is spread through the air when people who have an active TB infection cough, sneeze, or otherwise transmit respiratory fluids through the air."@en;
  ontolex:isEvokedBy :consumption ;
  skos:inScheme :conceptLexicon .
                                                                                
:consumption2 a ontolex:LexicalConcept ;                                         
  ontolex:isConceptOf <http://dbpedia.org/resource/Consumption_(Economics)> ;
  skos:definition "Consumption is a major concept in economics and is also studied by many other social sciences. Economists are particularly interested in the relationship between consumption and income, and therefore in economics the consumption function plays a major role.";
  ontolex:isEvokedBy :consumption ;
  skos:inScheme :conceptLexicon .
                                                                                
:tuberculosis1 a ontolex:LexicalConcept ;
  ontolex:isConceptOf <http://dbpedia.org/resource/Tuberculosis> ;
  skos:definition "Tuberculosis, MTB, or TB (short for tubercle bacillus), in the past also called phthisis, phthisis pulmonalis, or consumption, is a widespread, and in many cases fatal, infectious disease caused by various strains of mycobacteria, usually Mycobacterium tuberculosis. Tuberculosis typically attacks the lungs, but can also affect other parts of the body. It is spread through the air when people who have an active TB infection cough, sneeze, or otherwise transmit respiratory fluids through the air."@en;
  ontolex:isEvokedBy :tuberculosis ;
  skos:inScheme :conceptLexicon .

:consumption a ontolex:LexicalEntry ;
  ontolex:canonicalForm :consumption_lemma .

:consumption_lemma ontolex:writtenRep "consumption"@en .

:tuberculosis a ontolex:LexicalEntry ;
  ontolex:canonicalForm :tuberculosis_lemma .

:tuberculosis_lemma ontolex:writtenRep "tuberculosis"@en .
```

</aside>

</section>
</section>

<section id="synsem">
## Syntax and Semantics (synsem)

![](Lemon_Syntax_and_Semantics.png "Lemon_Syntax_and_Semantics.png")

<section id="syntactic-frames">
## Syntactic Frames

Most words in a language do not stand by their own, but have a certain
syntactic behavior in the sense that they appear in certain syntactic
structures and require a number of syntactic arguments to be complete.
Examples of this are i) transitive verbs (e.g. to own), which require a
syntactic subject and a syntactic object, ii) relational nouns (e.g.
capital (of), mother (of), son (of), brother (of), etc.), which require
a prepositional object, or iii) adjectives, which require a noun to
modify, etc. The syntactic behavior of a lexical entry is defined in
lemon by a syntactic frame:

<div class="entity" about="synsem:SyntacticFrame" typeof="owl:Class">
<class property="rdfs:label" lang="en">Syntactic Frame</class>

<div property="rdfs:comment"> A <dfn>syntactic frame</dfn> represents the syntactic behavior of an open class word in terms of the (syntactic) arguments it requires. It essentially describes the so called subcategorization structure of the word in question, in particular the syntactic arguments it requires. </div>

<div class="description">
</div>
</div>

In order to relate a lexical entry to one of its various syntactic
behaviors as captured by a syntactic frame, the `synsem`{.cm} module
defines the [=syntactic behavior=] property. Each
lexical entry should have its own syntactic frame instance, generic
behavior such as \'transitive\' should be captured by classes.

<div class="entity" about="synsem:synBehavior" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">SynBehavior</objectProperty>

<div property="rdfs:comment"> The <dfn>syntactic behavior</dfn> property relates a lexical entry to one of its syntactic behaviors as captured by a syntactic frame. </div>

<div class="description">
<domain>[=Lexical Entry=]</domain>
<range>[=Syntactic Frame=]</range>
<inverse>[=is syntactic behavior of=]</inverse>
</div>
</div>

The inverse of [=syntactic behavior=] is
<dfn>is syntactic behavior of</dfn>, which relates a
[=syntactic frame=] to the [=lexical entry=] that has this behavior.

The following example shows how to indicate that the verb *(to) own* can
be used as a transitive verb. This is accomplished by adding a frame
*own_frame_transitive* that is declared as a transitive frame, using the
class
[TransitiveFrame](http://lexinfo.net/ontology/2.0/lexinfo.owl#TransitiveFrame)
defined in the [LexInfo
Ontology](http://lexinfo.net/ontology/2.0/lexinfo.owl).

<aside class="example">
[![no
desc](Examples/synsem/example1.png)](Examples/synsem/example1.png){.tn}

```turtle
:own_lex a ontolex:LexicalEntry ;
  ontolex:canonicalForm :own_form ;
  synsem:synBehavior :own_frame_transitive .

:own_frame_transitive a synsem:SyntacticFrame, lexinfo:TransitiveFrame.

:own_form ontolex:writtenRep "own"@en . 
```

</aside>

Arguments of a syntactic frame are represented by the class [=Syntactic
Argument=]:

<div class="entity" about="synsem:SyntacticArgument" typeof="owl:Class">
<class property="rdfs:label" lang="en">Syntactic Argument</class>

<div property="rdfs:comment"> A <dfn>syntactic argument</dfn> represents a slot that needs to be filled for a certain syntactic frame to be complete. Syntactic arguments typically realize a certain grammatical function (e.g. subject, direct object, indirect object, prepositional object, etc.). </div>

<div class="description">
</div>
</div>

The object property [=synArg=] is used to relate a
(syntactic) frame to one of its syntactic arguments.

<div class="entity" about="synsem:synArg" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">SynArg</objectProperty>

<div property="rdfs:comment"> The <dfn>synArg</dfn> property relates a syntactic frame to one of its syntactic arguments. </div>

<div class="description">
<domain>[=Syntactic Frame=]</domain>
<range>[=Syntactic Argument=]</range>
</div>
</div>

The following example shows how to extend the example for the verb *(to)
own* by specifically indicating the arguments, in this case via two
specific sub-properties of [=synArg=], i.e.
[lexinfo:subject](http://lexinfo.net/ontology/2.0/lexinfo.owl#subject)
or
[lexinfo:directObject](http://lexinfo.net/ontology/2.0/lexinfo.owl#object)
defined in the external [LexInfo
ontology](http://lexinfo.net/ontology/2.0/lexinfo.owl).

<aside class="example">
[![no
desc](Examples/synsem/example2.png)](Examples/synsem/example2.png){.tn}

```turtle
:own_lex a ontolex:LexicalEntry ;
  ontolex:canonicalForm :own_form ;
  synsem:synBehavior :own_frame_transitive .

:own_form ontolex:writtenRep "own"@en. 

:own_frame_transitive a lexinfo:TransitiveFrame;
       lexinfo:subject :own_frame_subj;
       lexinfo:directObject :own_frame_obj.
```

</aside>

Note that if an external ontology is used to describe the type of
arguments in more detail, e.g. indicating the grammatical function as in
the example above, the external property used needs to be a sub-property
of [=synArg=].
</section>

<section id="ontology-mappings">
## Ontology Mappings

At the lexicon-ontology interface, syntactic frames need to be mapped or
bound to ontological structures that represent their meaning. In the
same way that a lexical sense binds a lexical entry to an ontology
entity, the [OntoMap](#OntoMap) maps a syntactic frame onto an ontology
entity.

<div class="entity" about="synsem:OntoMap" typeof="owl:Class">
<class property="rdfs:label" lang="en">Ontology Mapping</class>

<div property="rdfs:comment"> An <dfn data-lt="OntoMap|Onto Map">ontology map</dfn> represents the mapping between a syntactic frame and an ontology entity that represents the meaning of the syntactic frame. </div>

<div class="description">
</div>
</div>

In order to link an [=ontology map=] to a
corresponding sense, the model foresees the property
[=ontoMapping=], which is defined as functional
and inverse functional, that is in exact 1:1 relationship with a lexical
sense. As such, it is recommended that in the case that a lexicon
requires both the [=ontology map=] and the [=lexical
sense=], then these two entities are defined
using the same URI as there is no technical reason to distinguish them
and they have very similar functions.

<div class="entity" about="synsem:ontoMapping" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">OntoMapping</objectProperty>

<div property="rdfs:comment"> The <dfn>ontoMapping</dfn> property relates an ontology mapping to its corresponding lexical sense. </div>

<div class="description">
<domain>[=Ontology Map=]</domain>
<range>[=Lexical Sense=]</range>
<functional/>
<inverse-functional/>
</div>
</div>

The `synsem`{.cm} module introduces the property
[=ontoCorrespondence=] to establish a
mapping between an argument of a predicate defined in the ontology and
the syntactic argument that realizes this predicate argument in a given
syntactic frame:

<div class="entity" about="synsem:ontoCorrespondence" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">OntoCorrespondence</objectProperty>

<div property="rdfs:comment"> The <dfn>ontoCorrespondence</dfn> property binds an argument of a predicate defined in the ontology to a syntactic argument that realizes this predicate argument syntactically. </div>

<div class="description">
<domain>[=Ontology Map=] OR [=Lexical Sense=]</domain>
<range>[=Syntactic Argument=]</range>
</div>
</div>

Without limitation, we assume that an ontology consists of symbols
representing individuals, unary predicates and binary predicates, as
indicated by the following table:

  Type                                      Predicate                       Predicate Logic Notation   RDF Notation
  ----------------------------------------- ------------------------------- -------------------------- -----------------------------
  Class                                     Unary predicate                 *City(x)*                  `?x rdf:type dbo:City`{.cm}
  Object, Datatype or Annotation Property   Binary predicate                *knows(x,y)*,              `?x foaf:knows ?y`{.cm}
  Individual                                Constant (null-ary predicate)   *London*,                  `dbr:London`{.cm}

Predicates with an arity of more than two can be represented by complex
senses (see below). This is due to the fact that this module is aligned
to RDF and OWL, which distinguish between: individuals/resources
(constants), classes (unary predicates) and properties (predicates of
arity \"2\").

In the following, we introduce three sub-properties of the
[=ontoCorrespondence=] property. The first
property [is a](#isA) is used to refer to the single argument of a unary
predicate in the ontology:

<div class="entity" about="synsem:isA" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Is A</objectProperty>

<div property="rdfs:comment"> The <dfn>is a</dfn> property represents the single argument of a class or unary predicate in the ontology. </div>


<div class="description">
<subproperty>[=ontoCorrespondence=]</subproperty>
</div>
</div>

Following the terminology used in RDF/OWL we call the first argument of
a property its **subject** and the second argument the **object**. The
`synsem`{.cm} module defines two properties **subjOfProp** and
**objOfProp** that can be used to refer to the 1st (subject) and 2nd
(object) argument of a property, that is a predicate of arity \"2\".

<div class="entity" about="synsem:subjOfProp" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Subject of Property</objectProperty>

<div property="rdfs:comment"> The <dfn>subjOfProp</dfn> property represents the 1st argument or subject of a binary predicate (property) in the ontology. </div>

<div class="description">
<subproperty>[=ontoCorrespondence=]</subproperty>
</div>
</div>

<div class="entity" about="synsem:objOfProp" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Object of Property</objectProperty>

<div property="rdfs:comment">The <dfn>objOfProp</dfn> property represents the 2nd argument or object of a binary predicate (property) in the ontology. </div>

<div class="description">
<subproperty>[=ontoCorrespondence=]</subproperty>
</div>
</div>

Finally, we can specify the reference
[owner](http://dbpedia.org/ontology/owner) that expresses the meaning of
\"to own\" with respect to the DBpedia ontology, specifying the mapping
between arguments of the property **owner** and the arguments that
realize these arguments syntactically.

<aside class="example">
[![no
desc](Examples/synsem/example3.png)](Examples/synsem/example3.png){.tn}

```turtle
:own_lex a ontolex:LexicalEntry ;
  ontolex:canonicalForm :own_form ;
  synsem:synBehavior :own_frame_transitive ;
  ontolex:denotes <http://dbpedia.org/ontology/owner> .

:own_form ontolex:writtenRep "own"@en. 

:own_frame_transitive a lexinfo:TransitiveFrame;
       lexinfo:subject :own_subj;
       lexinfo:directObject :own_obj.

:own_ontomap a synsem:OntoMap;
         synsem:subjOfProp :own_obj;
         synsem:objOfProp :own_subj.
```

</aside>

As a further example we show a lexical entry for the relational noun
\"father (of)\". The entry indicates that the relation noun \"father
(of)\" can be used to verbalize the DBpedia property
[father](http://dbpedia.org/ontology/father), whereby the subject in a
copula construct such as \"X is father of Y\" (`:arg1`{.cm} below)
corresponds to the 2nd argument of the property
[father](http://dbpedia.org/ontology/father), and the prepositional
argument at position Y (`:arg2`{.cm} below) corresponds to the 1st
argument of the property [father](http://dbpedia.org/ontology/father).
We use the [LexInfo](http://www.lexinfo.net/) vocabulary to provide
linguistic information.

<aside class="example">
[![no
desc](Examples/synsem/example4.png)](Examples/synsem/example4.png){.tn}

```turtle
:father_of a ontolex:LexicalEntry ; 
    lexinfo:partOfSpeech lexinfo:noun ;
    ontolex:canonicalForm :father_form;
    synsem:synBehavior :father_of_nounpp;
    ontolex:sense :father_sense_ontomap.

:father_form a ontolex:Form;
    ontolex:writtenRep "father"@en.

:father_of_nounpp a lexinfo:NounPPFrame;
   lexinfo:subject :arg1;
   lexinfo:prepositionalArg :arg2.

:father_sense_ontomap a synsem:OntoMap, ontolex:LexicalSense;
   synsem:ontoMapping :father_sense_ontomap;
   ontolex:reference <http://dbpedia.org/ontology/father>;
   synsem:subjOfProp :arg2;
   synsem:objOfProp :arg1.

:arg2 synsem:marker :of .
```

</aside>

<div class="entity" about="synsem:marker" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Marker</objectProperty>

<div property="rdfs:comment"> The <dfn>marker</dfn> property indicates the marker of a syntactic argument, which can be a case marker or some other lexical entry such as a preposition or particle. </div>

<div class="description">
<domain>[=Syntactic Argument=]</domain>
<range>rdfs:Resource</range>
</div>
</div>

The following example shows how to specify that the intransitive verb
*operate*, subcategorizing a prepositional phrase introduced by the
preposition *in*, can be used to denote the property
[regionServed](http://dbpedia.org/ontology/regionServed) in DBpedia. The
entry specifies that in a construction such as \`X operates in Y\', the
X refers to the subject of the property `regionServed`{.cm}, and the Y
refers to the object of the property
[regionServed](http://dbpedia.org/ontology/regionServed). Again, we use
the [LexInfo](http://www.lexinfo.net) ontology in our example to provide
linguistic information:

<aside class="example">
[![no
desc](Examples/synsem/example5.png)](Examples/synsem/example5.png){.tn}

```turtle
:operate_in a ontolex:LexicalEntry ; 
    lexinfo:partOfSpeech lexinfo:verb ;
    ontolex:canonicalForm :operate_form;
    synsem:synBehavior :operate_intransitivepp;
    ontolex:sense :operate_sense_ontomap.

:operate_form a ontolex:Form;
   ontolex:writtenRep "operate"@en.

:operate_intransitivepp a synsem:SyntacticFrame;
   lexinfo:subject :operate_subj ;
   lexinfo:prepositionalArg :operate_pobj.

:operate_sense_ontomap a ontolex:LexicalSense, synsem:OntoMap;
   synsem:ontoMapping :operate_sense_ontomap;
   ontolex:reference <http://dbpedia.org/ontology/regionServed>;
   synsem:subjOfProp :operate_subj;
   synsem:objOfProp :operate_pobj.
 
:operate_pobj synsem:marker :in .
```

</aside>
</section>

<section id="complex-ontology-mappings">
## Complex ontology mappings / submappings

In many cases, the meaning of a syntactic frame can not be expressed by
exactly one binary predicate as in the examples given above. Take for
instance the case of a transitive verb *(to) launch*, which
subcategorizes a subject expressing the company that launched a product,
a direct object expressing the launched product, and a prepositional
object introduced by the preposition *in* indicating the year of the
launch of the product in question. The important thing here is that
there are three syntactic arguments (subject, object and prepositional
object, represented as `arg1`{.cm}, `arg2`{.cm} and `arg3`{.cm} below,
respectively) that realize the arguments of a complex predicate that
consist of the sub-predicates
[dbpedia:product](http://dbpedia.org/ontology/product) and
[dbpedia:launchDate](http://dbpedia.org/ontology/launchDate).

Thus, the `synsem`{.cm} module introduces the property
[=submap=] that relates a (complex) ontological map
involving various ontological predicates to a set of less complex
ontological maps that bind the arguments of one of the involved
predicates to a syntactic argument that realizes it.

<div class="entity" about="synsem:submap" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Submap</objectProperty>

<div property="rdfs:comment"> The <dfn>submap</dfn> property relates a (complex) ontological mapping to a set of bindings that together bind the arguments of the involved predicates to a set of syntactic arguments that realize them syntactically. </div>

<div class="description">
<domain>[=Ontology Map=]</domain>
<range>[=Ontology Map=]</range>
</div>
</div>

The following example shows how to use the [=submap=]
property to indicate that the meaning of the phrase *X launched Y in Z*
is a composition of the properties
[dbpedia:product](http://dbpedia.org/ontology/product) and
[dbpedia:launchDate](http://dbpedia.org/ontology/launchDate), which
together express the meaning of the syntactic frame:

<aside class="example">
[![no
desc](Examples/synsem/example6.png)](Examples/synsem/example6.png){.tn}

```turtle
:launch a ontolex:LexicalEntry ;
  lexinfo:partOfSpeech lexinfo:verb ;
  ontolex:canonicalForm :launch_canonical_form;
  synsem:synBehavior :launch_transitive_pp;
  ontolex:sense :launch_sense_ontomap.

:launch_canonical_form ontolex:writtenRep "launch"@en.

:launch_transitive_pp a lexinfo:TransitivePPFrame;
 lexinfo:subject              :arg1 ;
 lexinfo:directObject         :arg2 ;
 lexinfo:prepositionalAdjunct :arg3.

:arg3 synsem:marker :in ;
             synsem:optional "true"^^xsd:boolean .


:launch_sense_ontomap a ontolex:LexicalSense, synsem:OntoMap;
   synsem:ontoMapping :launch_sense_ontomap;
   synsem:submap :launch_submap1;
   synsem:submap :launch_submap2.

:launch_submap1 ontolex:reference <http://dbpedia.org/ontology/product>;
                                 synsem:subjOfProp :arg1;
                                 synsem:objOfProp  :arg2.

:launch_submap2 ontolex:reference <http://dbpedia.org/ontology/launchDate>;
                                 synsem:subjOfProp :arg2;
                                 synsem:objOfProp  :arg3.
```

</aside>

It is possible to specify that a certain argument is not compulsory by
the [=optional=] property. It is generally only
advised to use this property with complex senses. Indicating that an
argument is optional means that it does not have to be realized
syntactically in which case from a semantic point of view the
corresponding argument of the ontological predicate is existentially
quantifier over. In the above example we have indicated that `arg3`{.cm}
is optional, allowing to assign the correct semantics to an expression
such as *X launched Y* by existentially quantifying over the year.

<div class="entity" about="synsem:optional" typeof="owl:DatatypeProperty">
<datatypeProperty property="rdfs:label" lang="en">Optional</datatypeProperty>

<div property="rdfs:comment"> The <dfn>optional</dfn> property indicates whether a syntactic argument is optional, that is, it can be syntactically omitted. </div>

<div class="description">
<domain>[=Syntactic Argument=]</domain>
<range>xsd:boolean</range>
</div>
</div>

The following example shows how we can capture the [diathesis
alternation](https://en.wikipedia.org/wiki/Diathesis_alternation)
between *X gave Y Z* and *X gave Z to Y*, which in our modelling
represent the same ontological meaning:

<aside class="example">
[![no
desc](Examples/synsem/example7.png)](Examples/synsem/example7.png){.tn}

```turtle
:give a ontolex:LexicalEntry ; 
    lexinfo:partOfSpeech lexinfo:verb ;
    ontolex:canonicalForm :give_form;
    synsem:synBehavior :give_ditransitive;
    synsem:synBehavior :give_transitive_pp;
    ontolex:sense :giving_sense_ontomap.

:give_form a ontolex:Form;
   ontolex:writtenRep "give"@en.

:give_transitive_pp a lexinfo:TransitivePPFrame;
   lexinfo:subject :give_subj1 ;
   lexinfo:directObject :give_dobj1; 
   lexinfo:prepositionalArg :give_pobj1.

:give_ditransitive a lexinfo:DitransitiveFrame;
   lexinfo:subject :give_subj2 ;
   lexinfo:indirectObject :give_iobj2;
   lexinfo:directObject :give_dobj2.


:giving_sense_ontomap a ontolex:LexicalSense, synsem:OntoMap;
   synsem:ontoMapping :giving_sense_ontomap;
   ontolex:reference <http://www.ontologyportal.org/SUMO.owl#Giving>;
   synsem:submap :giving_submap1;
   synsem:submap :giving_submap2;
   synsem:submap :giving_submap3.
 
:giving_submap1 ontolex:reference <http://www.ontologyportal.org/SUMO.owl#agent>;
                                 synsem:subjOfProp :giving_event;
                                 synsem:objOfProp  :give_subj1;
                                 synsem:objOfProp  :give_subj2.

:giving_submap2 ontolex:reference <http://www.ontologyportal.org/SUMO.owl#patient>;
                                 synsem:subjOfProp :giving_event;
                                 synsem:objOfProp  :give_dobj2;
                                 synsem:objOfProp :give_dobj1.

:giving_submap3 ontolex:reference <http://www.ontologyportal.org/SUMO.owl#destination>;
                                 synsem:subjOfProp :giving_event;
                                 synsem:objOfProp  :give_iobj2;
                                 synsem:objOfProp :give_pobj1.

:give_pobj1 synsem:marker :to .
```

</aside>

For adjectives a modelling may be as follows:

<aside class="example">
[![no
desc](Examples/synsem/example8.png)](Examples/synsem/example8.png){.tn}

```turtle
:female a ontolex:LexicalEntry; 
  lexinfo:partOfSpeech lexinfo:adjective;
  ontolex:canonicalForm :female_canonical_form;
  synsem:synBehavior :female_syn,:female_syn1;
  ontolex:sense :female_sense_ontomap.

:female_canonical_form ontolex:writtenRep "female"@en.

:female_sense_ontomap ontolex:reference [
    a owl:Restriction;
    owl:onProperty <http://dbpedia.org/ontology/gender> ;
    owl:hasValue <http://dbpedia.org/resource/Female> ] ;
  synsem:ontoMapping :female_sense_ontomap;
  synsem:isA :female_arg .

:female_syn a lexinfo:AdjectivePredicateFrame;
   lexinfo:copulativeSubject :female_arg.
                                                                                
:female_syn1 a lexinfo:AdjectiveAttributiveFrame ;                              
   lexinfo:attributiveArg :female_arg.  
```

</aside>

Note that in the above example the property `synsem:isA`{.cm} property
is used to mark the single argument/variable of the class of all the
things that have female gender. The copulative subject in an expression
such as \"Mary is female\" is bound to this single argument of the
corresponding ontological predicate. The semantics is thus in essence
the characteristic function that for each element decides if it is in
the set denoted by the class.
</section>

<section id="conditions">
## Conditions

Conditions describe precise conditions that must be met by a context in
which a lexical entry can be used to refer to a certain ontological
predicate (reference). These contextual conditions are attached to the
lexical sense that mediates the relation between a lexical entry and the
ontological predicate it can be used to express.

<div class="entity" about="synsem:condition" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Condition</objectProperty>

<div property="rdfs:comment"> The <dfn>condition</dfn> property defines an evaluable constraint that derives from using a certain lexical entry to express a given ontological predicate. </div>

<div class="description">
<domain>[=Lexical Sense=]</domain>
<range>rdfs:Resource</range>
<subproperty>[=usage=]</subproperty>
</div>
</div>

Two special types of conditions are defined in the synsem module, which
formulate constraints on the type of arguments that can be used at the
first or second position of a property when a certain lexical entry is
used to express that property. Take for instance the distinction between
the English verbs *(to) ride* and *(to) drive*. Both express the means
of transportation, but have different implications. Ride implies that
the means of transportation is a bike. Instead of introducing different
ontological predicates and different senses, the modulation can be
captured by specifying restrictions on the values that can fill the 1st
or 2nd argument of the corresponding ontological predicate. This is
illustrated by the example below:

<aside class="example">
[![no
desc](Examples/synsem/example9.png)](Examples/synsem/example9.png){.tn}

```turtle
:ride a ontolex:LexicalEntry ;
  ontolex:sense :ride_sense1 .

:ride_sense1 a ontolex:LexicalSense ;
  ontolex:reference :methodOfTransportation ;
  synsem:propertyRange :Bicycle ;
  synsem:semArg :subj, :obj .

:methodOfTransportation a rdf:Property ;
  rdfs:range :Vehicle .
```

</aside>

It is important to note that the
[=property domain=] or
[=property range=] properties do not modify in
any way the ontological status or commitment of the corresponding
property (here: methodOfTransportation). Instead, they make explicit
certain implications on the type of arguments involved that derive from
the use of a certain lexical entry to express the property in question.

<div class="entity" about="synsem:propertyDomain" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Property Domain</objectProperty>

<div property="rdfs:comment"> The <dfn>property domain</dfn> property specifies a constraint on the type of arguments that can be used at the first position of the property that is referenced by the given sense. </div>

<div class="description">
<domain>[=Lexical Sense=]</domain>
<range>rdfs:Resource</range>
</div>
</div>

<div class="entity" about="synsem:propertyRange" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Property Range</objectProperty>

<div property="rdfs:comment"> The <dfn>property range</dfn> property specifies a constraint on the type of arguments that can be used at the first position of the property that is referenced by the given sense. </div>

<div class="description">
<domain>[=Lexical Sense=]</domain>
<range>rdfs:Resource</range> 
</div>
</div>

</section>
</section>

<section id="decomp">
## Decomposition (decomp)

![](Lemon_Decomposition.png "Lemon_Decomposition.png")

<section id="subterms">
## Subterms

Decomposition is the process of indicating which elements constitute a
multiword or compound lexical entry. The simplest way to do this is by
means of the [=subterm=] property, which indicates
that a [=lexical entry=] is a part of another
entry. This property allows us to specify which lexical entries a
certain compound lexical entry is composed of.

<div class="entity" about="decomp:subterm" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Subterm</objectProperty>

<div property="rdfs:comment"> The <dfn>subterm</dfn> property relates a compound lexical entry to one of the lexical entries it is composed of. </div>

<div class="description">
<domain>[=Lexical Entry=]</domain>
<range>[=Lexical Entry=]</range>
</div>
</div>

The subterm property is used to indicate which terms have been derived
from another term by means of adding or removing words, for example

<aside class="example">
[![no
desc](Examples/decomp/example1.png)](Examples/decomp/example1.png){.tn}

```turtle
:AfricanSwineFever a ontolex:LexicalEntry ;
  decomp:subterm :SwineFever .
```

</aside>

The subterm property may also be used to indicate the decomposition of
compound words. The following example shows how to indicate that the
German compound *Lungenentzündung* (\'pneumonia\' literally \'lung
inflammation\') is decomposed into the lexical entries *Lunge* and
*Entzündung*:

<aside class="example">
[![no
desc](Examples/decomp/example2.png)](Examples/decomp/example2.png){.tn}

```turtle
:Lungenentzündung a ontolex:LexicalEntry ;
  decomp:subterm :Lunge_lex;
  decomp:subterm :Entzündung_lex .
```

</aside>

It is important to mention that the subterm property is a relation
between lexical entries and does neither indicate the specific inflected
word of a lexical entry that appears in the compound nor the position at
which it appears.
</section>

<section id="components">
## Components

The subterm property allows us to indicate which lexical entries a
compound is composed of, but it does not indicate the internal structure
of the compound. This can be achieved by introducing so called
[=components=]. Such components represent a fixed
list of each of the elements that compose a lexical entry. In the most
common case of a multiword expression, the components of the lexical
entry are the individual tokens that compose that entry.

<div class="entity" about="decomp:Component" typeof="owl:Class">
<class property="rdfs:label" lang="en">Component</class>

<div property="rdfs:comment"> A <dfn>component</dfn> represents a particular realization of a lexical entry that forms part of a compound lexical entry. </div>

<div class="description">
</div>
</div>

Each component is said to be a [=constituent=] of
a lexical entry:

<div class="entity" about="decomp:constituent" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Constituent</objectProperty>

<div property="rdfs:comment"> The <dfn>constituent</dfn> property relates a lexical entry or component to a component that it is constituted by. </div>

<div class="description">
<domain>[=Lexical Entry=] OR [=Component=]</domain>
<range>[=Component=]</range>
</div>
</div>

<aside class="example">
[![no
desc](Examples/decomp/example3.png)](Examples/decomp/example3.png){.tn}

```turtle
:AfricanSwineFever a ontolex:MultiwordExpression ;
  decomp:constituent :African_comp , :Swine_comp , :Fever_comp ;
  decomp:subterm :SwineFever .

:African_comp a decomp:Component .

:Swine_comp a decomp:Component .

:Fever_comp a decomp:Component .

:SwineFever a ontolex:MultiwordExpression ;
  decomp:constituent :Swine_comp , :Fever_comp .
```

</aside>

As a component represents a particular realization of a lexical entry
which forms part of a compound lexical entry, we need to link the
component to the corresponding lexical entry it is a realization of.
This is done by the property [=corresponds to=]:

<div class="entity" about="decomp:correspondsTo" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Corresponds To</objectProperty>

<div property="rdfs:comment"> The <dfn>corresponds to</dfn> property links a component to a corresponding lexical entry or argument. </div>

<div class="description">
<domain>[=Component=]</domain>
<range>[=Lexical Entry=] OR [=Syntactic Argument=]</range>
</div>
</div>

It may be necessary to add inflectional properties to the component to
uniquely determine the actual form of the lexical entry. This
inflectional information can be attached to the component as shown in
the following example for the Spanish term \'comunidad autónoma\'
(federal state), whose second word is the singular feminine form
*autónoma* instead of the canonical form *autónomo*.

<aside class="example">
[![no
desc](Examples/decomp/example4.png)](Examples/decomp/example4.png){.tn}

```turtle
:comunidad_autonoma_lex a ontolex:LexicalEntry ;
  decomp:constituent :comunidad_component;
  decomp:constituent :autonoma_component .

:comunidad_component a decomp:Component;
     decomp:correspondsTo :comunidad_lex.

:autonoma_component a decomp:Component;
     decomp:correspondsTo :autonomo_lex;
     lexinfo:gender lexinfo:feminine;
     lexinfo:number lexinfo:singular.
```

</aside>

If we want to specify the order of the components, we can use the RDF
properties `rdf:_1`{.cm}, `rdf:_2`{.cm}, etc. as in the following
example to specify the absolute order, in addition to the
[=constituent=] properties. Note that the
property *constituent* alone is not sufficient to specify the order of
components.

<aside class="example">
[![no
desc](Examples/decomp/example5.png)](Examples/decomp/example5.png){.tn}

```turtle
:comunidad_autonoma_lex a ontolex:LexicalEntry ;
  decomp:constituent :comunidad_component;
  rdf:_1             :comunidad_component; 
  decomp:constituent :autonoma_component;
  rdf:_2             :autonoma_component;
  ontolex:denotes <http://dbpedia.org/ontology/federalState>;
  ontolex:canonicalForm :comunidad_autonoma_lex_canonical_form.

:comunidad_autonoma_lex_canonical_form ontolex:writtenRep "comunidad autónoma"@es.

:comunidad_component a decomp:Component;
     decomp:correspondsTo :comunidad_lex.

:autonoma_component a decomp:Component;
     decomp:correspondsTo :autonomo_lex;
     lexinfo:gender lexinfo:feminine;
     lexinfo:number lexinfo:singular.
```

</aside>
</section>

<section id="phrase-structure">
## Phrase structure

The constituent property can also be used to specify the structure of a
phrase, by means of showing some components as being constituted of
further components. In this way, each of the components represents a
node in the phrase structure tree and may be annotated with a phrase tag
as in the following example:

<aside class="example">
[![no
desc](Examples/decomp/example6.png)](Examples/decomp/example6.png){.tn}

```turtle
:AfricanSwineFever_root a decomp:Component ;
  decomp:correspondsTo :AfricanSwineFever ;
  decomp:constituent :African_node, :SwineFever_node ;
  rdf:_1 :African_node;
  rdf:_2 :SwineFever_node;
  olia:hasTag penn:NP .

:African_node a decomp:Component ;
  decomp:correspondsTo :African ;
  olia:hasTag penn:JJ .

:SwineFever_node a decomp:Component ;
  decomp:constituent :Swine_node, :Fever_node ;
  rdf:_1 Swine_node;
  rdf:_2 Fever_node;
  olia:hasTag penn:NP .

:Swine_node a decomp:Component ; 
  decomp:correspondsTo :Swine ;
  olia:hasTag penn:NN .

:Fever_node a decomp:Component ; 
  decomp:correspondsTo :Fever ;
  olia:hasTag penn:NN .
```

</aside>

The syntactic categories of the phrases are indicated using the property
olia:hasTag from the [OLiA
vocabulary](http://nachhalt.sfb632.uni-potsdam.de/owl/) using the [Penn
TreeBank
tagset](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html).

The following example shows how to use the synsem module in conjunction
with the decomp module to indicate the phrase structure tree of a frame.
This is done by making the frame the target of the *correspondsTo*
property and including components in the tree that correspond to
individual arguments. As such it is possible to represent modelling of
lexicalized grammars within the lexicon.

<aside class="example">
[![no
desc](Examples/decomp/example7.png)](Examples/decomp/example7.png){.tn}

```turtle
:know a ontolex:Word ;
  synsem:synBehavior :know_frame .

:know_frame a synsem:SyntacticFrame ;
  lexinfo:subject :subject ;
  lexinfo:directObjet :directObject .

:know_root a decomp:Component ;
  decomp:correspondsTo :know_frame ;
  decomp:constituent :X_node, :knowY_node ;
  olia:hasTag penn:S .

:X_node a decomp:Component ;
  decomp:correspondsTo :subject ;
  olia:hasTag penn:NP .

:knowY_node a decomp:Component ;
  decomp:constituent :know_node, :Y_node ;
  olia:hasTag penn:VP .

:know_node a decomp:Component ;
  decomp:correspondsTo :know ;
  olia:hasTag penn:V .

:Y_node a decomp:Component ;
  decomp:correspondsTo :directObject ;
  olia:hasTag penn:NP .
```

</aside>
</section>
</section>

<section id="vartrans">
## Variation & Translation (vartrans)

The variation and translation module introduces vocabulary needed to
represent relations between lexical entries and lexical senses that are
variants of each other. The following diagram provides an overview of
the vocabulary introduced by the module:

![](Lemon_Variation_and_Translation.png "Lemon_Variation_and_Translation.png")

<section id="lexico-semantic-relations">
## Lexico-Semantic Relations

The model defines a generic class [=lexico-semantic
relation=] that allows us to
relate two lexical entries or two lexical senses to each other, this is
done principally by means of two properties
[=lexicalRel=] and
[=senseRel=] that allow to directly link two lexical
entries / lexical senses that are related.

<div class="entity" about="vartrans:lexicalRel" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Lexical Relation</objectProperty>

<div property="rdfs:comment"> The <dfn>lexicalRel</dfn> property relates two lexical entries that stand in some lexical relation. </div>

<div class="description">
<domain>[=Lexical Entry=]</domain>
<range>[=Lexical Entry=]</range>
</div>
</div>

<div class="entity" about="vartrans:senseRel" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Sense Relation</objectProperty>

<div property="rdfs:comment"> The <dfn>senseRel</dfn> property relates two lexical senses that stand in some sense relation. </div>

<div class="description">
<domain>[=Lexical Sense=]</domain>
<range>[=Lexical Sense=]</range>
</div>
</div>

In general, these properties should not be used directly but instead a
sub-property should be introduced, for example:

<aside class="example">
[![no
desc](Examples/vartrans/example3.png)](Examples/vartrans/example3.png){.tn}

```turtle
:fao lexinfo:initialismFor :food_and_agriculture_organization.

:surrogate_mother lexinfo:hypernym :mother.

lexinfo:initialismFor rdfs:subProperty vartrans:lexicalRel.
lexinfo:hypernym rdfs:subProperty vartrans:senseRel.
    
```

</aside>

In the case that further information about the relationship needs to be
represented it is possible to create an individual that \'reifies\' the
relationship.

<div class="entity" about="vartrans:LexicoSemanticRelation" typeof="owl:Class">
<class property="rdfs:label" lang="en">Lexico-Semantic Relation</class>

<div property="rdfs:comment"> A <dfn>lexico-semantic relation</dfn> represents the relation between two lexical entries or lexical senses that are related by some lexical or semantic relationship. </div>

<div class="description">
<subclass>[=relates=] exactly 2 [=Lexical Entry=] OR [=Lexical Sense=] OR [=Lexical Concept=]</subclass>
</div>
</div>

The object property [=relates=] links a
[=lexico-semantic relation=] to the
lexical entries or lexical senses between which it establishes the
relation:

<div class="entity" about="vartrans:relates" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Relates</objectProperty>

<div property="rdfs:comment"> The <dfn>relates</dfn> property links a lexico-semantic relation to the two lexical entries or lexical senses between which it establishes the relation. </div>

<div class="description">
<domain>[=Lexico-Semantic Relation=]</domain>
<range>[=Lexical Entry=] OR [=Lexical Sense=] OR [=Lexical Concept=]</range>
</div>
</div>


As many lexico-semantic relations are asymmetric, it is necessary to
distinguish the [=source=] from the
[=target=]:

<div class="entity" about="vartrans:source" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Source</objectProperty>

<div property="rdfs:comment"> The <dfn>source</dfn> property indicates the lexical sense or lexical entry involved in a lexico-semantic relation as a \'source\'. </div>

<div class="description">
<subproperty>[=relates=]</subproperty>
</div>
</div>

<div class="entity" about="vartrans:target" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Target</objectProperty>

<div property="rdfs:comment"> The <dfn>target</dfn> property indicates the lexical sense or lexical entry involved in a lexico-semantic relation as a \'target\'. </div>

<div class="description">
<subproperty>[=relates=]</subproperty>
</div>
</div>

The class [=lexico-semantic relation=] is specialized into the
following two subclasses: [=lexical relation=] and [=sense relation=], which relate two lexical entries
or two lexical senses, respectively:

<div class="entity" about="vartrans:LexicalRelation" typeof="owl:Class">
<class property="rdfs:label" lang="en">Lexical Relation</class>

<div property="rdfs:comment"> A <dfn>lexical relation</dfn> is a lexico-semantic relation that represents the relation between two lexical entries the surface forms of which are related grammatically, stylistically or by some operation motivated by linguistic economy. </div>

<div class="description">
<subclass>[=Lexico-Semantic Relation=], [=relates=] exactly 2 [=Lexical Entry=]</subclass>
</div>
</div>

By lexical relations we understand those relations at the surface forms,
mainly motivated by grammatical requirements, style (Wortklang), and
linguistic economy (helping to avoid excessive denominative repetition
and improving textual coherence). Examples of lexical relations are the
following:

-   Derivational relation (e.g., adjective → adverb variation: quick vs.
    quickly)
-   Morphosyntactic relation (e.g. ecological tourism vs. eco-tourism)
-   Abbreviation relation (including acronyms, e.g., peer to peer and
    p2p; WYSWYG, FAO, UNO)

The specific type of lexical or sense relation can be specified via the
object property [=category=], which is defined as
follows:

<div class="entity" about="vartrans:category" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Category</objectProperty>

<div property="rdfs:comment"> The <dfn>category</dfn> property indicates the specific type of relation by which two lexical entries or two lexical senses are related. </div>

<div class="description">
<domain>[=Lexico-Semantic Relation=]</domain>
<functional/>
</div>
</div>

The following example shows how to model the relation between \"Food and
Agriculture Organization\" and its initialism \"FAO\" as one example of
a lexical relation:

<aside class="example">
[![no
desc](Examples/vartrans/example1.png)](Examples/vartrans/example1.png){.tn}

```turtle
:fao a ontolex:LexicalEntry ;
     ontolex:sense :fao_sense; 
     ontolex:lexicalForm :fao_form.

:fao_sense ontolex:reference <http://dbpedia.org/resource/Food_and_Agriculture_Organization> .

:food_and_agriculture_organization a ontolex:LexicalEntry;
     ontolex:sense :food_and_agriculture_organization_sense ;
     ontolex:lexicalForm :food_and_agriculture_organization_form.

:food_and_agriculture_organization_sense ontolex:reference <http://dbpedia.org/resource/Food_and_Agriculture_Organization> .

:fao_form ontolex:writtenRep "FAO"@en .
:food_and_agriculture_organization_form ontolex:writtenRep "Food and Agriculture Organization"@en .

:fao_initialism a vartrans:LexicalRelation ;
      vartrans:source :food_and_agriculture_organization ; 
      vartrans:target :fao ;
      vartrans:category :initialism.
```

</aside>

<div class="entity" about="vartrans:SenseRelation" typeof="owl:Class">
<class property="rdfs:label" lang="en">Sense Relation</class>

<div property="rdfs:comment"> A <dfn>sense relation</dfn> is a lexico-semantic relation that represents the relation between two lexical senses the meanings of which are related. </div>

<div class="description">
<subclass>[=Lexico-Semantic Relation=], [=relates=] exactly 2 [=Lexical Sense=]</sub>
</div>
</div>

Examples of semantic relations are the equivalence relation between two
senses, hypernymy and hyponymy relations, synonymy, antonymy,
translations, etc.

The following example gives an example of a sense relation:

<aside class="example">
[![no
desc](Examples/vartrans/example2.png)](Examples/vartrans/example2.png){.tn}

```turtle
:surrogate_mother_lex a ontolex:LexicalEntry ;
     ontolex:sense :surrogate_mother_sense ;
     ontolex:canonicalForm :surrogate_mother_form.

:surrogate_mother_sense ontolex:reference <http://dbpedia.org/ontology/surrogate_mother>.

:surrogate_mother_form ontolex:writtenRep "surrogate mother"@en .

:mother_lex a ontolex:LexicalEntry ;
     ontolex:sense :mother_sense ;
     ontolex:canonicalForm :mother_form.

:mother_sense ontolex:reference <http://dbpedia.org/ontology/mother>.

mother_form ontolex:writtenRep "mother"@en .

:senseRelation a vartrans:SenseRelation ;
      vartrans:source :surrogate_mother_sense ;
      vartrans:target :mother_sense ; 
      vartrans:category lexinfo:hypernym .
```

</aside>

Further, we consider [=terminological
relations=], which are defined as
follows:

<div class="entity" about="vartrans:TerminologicalRelation" typeof="owl:Class">
<class property="rdfs:label" lang="en">Terminological Relation</class>

<div property="rdfs:comment"> A <dfn>terminological relation</dfn> is a sense relation that relates two lexical senses of terms that are semantically related in the sense that they can be exchanged in most contexts, but their surface forms are not directly related. The variants vary along dimensions that are not captured by the given ontology and are intentionally (pragmatically) caused. </div>

<div class="description">
<subclass>[=Sense Relation=]</subclass>
</div>
</div>

Examples of categories of terminological relations include:

-   Diatopic (dialectal or geographical variants) (e.g., gasoline vs.
    petrol)
-   Diaphasic (register) (e.g., headache vs. cephalalgia; swine flu vs.
    pig flu vs. H1N1 vs. Mexican pandemic flu)
-   Diachronic (or chronological variants) (e.g., tuberculosis vs.
    phthisis)
-   Diastratic (discursive or stylistic variants) (e.g., man vs. bloke)
-   Dimensional variants: the terms point to the same concept but
    highlight a different property or dimension of the concept (e.g.,
    *bio-sanitary waste* vs. *hospital waste*; *Novel Coronavirus* vs.
    *Middle East Respiratory Syndrome Coronavirus*; *obsolete
    technology* vs. *dangerous technology*; *madre de alquiler* (rental
    mother) vs. *vientre de alquiler* (womb mother), in Spanish).

We illustrate the use of terminological relations with the following
example of a diachronic variant:

<aside class="example">
[![no
desc](Examples/vartrans/example4.png)](Examples/vartrans/example4.png){.tn}

```turtle
:tuberculosis a ontolex:LexicalEntry ;
       ontolex:lexicalForm :tuberculosis_form ; 
       ontolex:sense :tuberculosis_sense.

:tuberculosis_form ontolex:writtenRep "tuberculosis"@en .

:tuberculosis_sense ontolex:reference <http://dbpedia.org/resource/Tuberculosis>.

:phthisis a ontolex:LexicalEntry ;
       ontolex:lexicalForm :phthisis_form ; 
       ontolex:sense :phthisis_sense.

:phthisis_form ontolex:writtenRep "phthisis"@en .

:phtisis_sense ontolex:reference <http://dbpedia.org/resource/Tuberculosis>;
               dct:subject <http://dbpedia.org/resource/Medicine> .

:phtisis_diachronic_relation a vartrans:TerminologicalRelation ;
      vartrans:source :phthisis_sense ;
      vartrans:target :tuberculosis_sense ; 
      vartrans:category :diachronic.
```

</aside>

Finally, it is also possible to give relationships between concepts, and
this is useful for modelling relations between synsets in wordnets and
other similar resources

<div class="entity" about="vartrans:conceptRel" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Concept Relation</objectProperty>

<div property="rdfs:comment"> The <dfn>conceptRel</dfn> property relates two lexical concepts that stand in some sense relation. </div>

<div class="description">
<domain>[=Lexical Concept=]</domain>
<range>[=Lexical Concept=]</range>
</div>
</div>

<div class="entity" about="vartrans:ConceptualRelation" typeof="owl:Class">
<class property="rdfs:label" lang="en">Conceptual Relation</class>

<div property="rdfs:comment"> A <dfn>conceptual relation</dfn> is a relationship between two lexical concepts</div>

<div class="description">
<subclass>[=Lexico-Semantic Relation=], [=relates=] exactly 2 [=Lexical Concept=]</sub>
</div>
</div>

</section>

<section id="translation">
## Translation

Translation relates two lexical entries from different languages the
meaning of which is \'equivalent\'. This \'equivalence\` can be
expressed at three different levels:

-   **Ontological Equivalence (Shared reference):** The simplest case is
    to have two entries in different languages that denote the same
    ontology entity. In this case they are clearly translations as they
    have the same interpretation.

<!-- -->

-   **Translation:** In these cases, the lexical entries might not
    denote exactly the same concept, but their lexical meanings (senses)
    be equivalent in that they can be exchanged for each other in most
    contexts. Translation in this case is a subclass of [=sense
    relation=].

<!-- -->

-   **Translatable as**: In this case, we underspecify the exact
    involved meanings of the two lexical entries that are said to be
    translations of each other, essentially specifying that, in some
    contexts, one lexical entry in a source language can be replaced by
    an entry in the target language, depending on the senses of these
    lexical entries in the given context.

</section>

<section id="translation-shared-reference">
## Translation as shared reference

In order to express that the lexical senses of two lexical entries are
ontologically equivalent, we do not need other machinery than the one
introduced already in the ontolex section above:

<aside class="example">
[![no
desc](Examples/vartrans/example5.png)](Examples/vartrans/example5.png){.tn}

```turtle
:surrogate_mother a ontolex:LexicalEntry;
      dct:language <http://id.loc.gov/vocabulary/iso639-2/eng>, <http://lexvo.org/id/iso639-1/en> ;
      ontolex:sense :surrogate_mother_sense.

:surrogate_mother_sense ontolex:reference ontology:SurrogateMother.

:madre_de_alquiler a ontolex:LexicalEntry;
      dct:language <http://id.loc.gov/vocabulary/iso639-2/es>, <http://lexvo.org/id/iso639-1/es> ;
      ontolex:sense :madre_de_alquiler_sense.

:madre_de_alquiler_sense ontolex:reference ontology:SurrogateMother.

:leihmutter a ontolex:LexicalEntry;
      dct:language <http://id.loc.gov/vocabulary/iso639-2/de>, <http://lexvo.org/id/iso639-1/de> ;
      ontolex:sense :leihmutter_sense.

:leihmutter_sense ontolex:reference ontology:SurrogateMother.
```

</aside>

By this, the corresponding senses of the lexical entries *surrogate
mother*, *madre de alquiler* and *Leihmutter* are said to be equivalent
in that they denote the same class in the ontology.
</section>

<section id="translation-as-relation-between-lexical-senses">
## Translation as a relation between lexical senses

The second alternative mentioned above can be realized through the class
[=translation=], which relates two senses that
can be regarded as equivalent in that they can be exchanged for each
other.

<div class="entity" about="vartrans:Translation" typeof="owl:Class">
<class property="rdfs:label" lang="en">Translation</class>

<div property="rdfs:comment"> A <dfn>translation</dfn> is a sense relation expressing that two lexical senses corresponding to two lexical entries in different languages can be translated to each other without any major meaning shifts. </div>

<div class="description">
<subclass>[=Sense Relation=]</subclass>
</div>
</div>

<aside class="example">
[![no
desc](Examples/vartrans/example6.png)](Examples/vartrans/example6.png){.tn}

```turtle
:zip_code a ontolex:LexicalEntry;
      dct:language <http://id.loc.gov/vocabulary/iso639-2/eng>, <http://lexvo.org/id/iso639-1/en> ;
      ontolex:sense :zip_code_sense.

:zip_code_sense ontolex:reference <http://dbpedia.org/ontology/zipCode>.

:postleitzahl a ontolex:LexicalEntry;
      dct:language <http://id.loc.gov/vocabulary/iso639-2/de>, <http://lexvo.org/id/iso639-1/de> ;
      ontolex:sense :postleitzahl_sense.

:postleitzahl_sense ontolex:reference <http://de.dbpedia.org/resource/Postleitzahl>.


:trans a vartrans:Translation;
       vartrans:source :zip_code_sense;
       vartrans:target :postleitzahl_sense;
       vartrans:category <http://purl.org/net/translation-categories#directEquivalent>.
```

</aside>

Thus, in spite of using having different denotations, both
*Postleitzahl* and *zip code* can be seen as cross-lingual equivalents
and thus as translations of each other.

Besides the class [=Translation=], which reifies
the translation relation between two lexical senses, as a shortcut the
model also allows us to directly express the relation of translation
between lexical senses by the 
[=translation property=] that is regarded as equivalent to
the reification:

<div class="entity" about="vartrans:translation" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Translation</objectProperty>

<div property="rdfs:comment"> The <dfn>translation property</dfn> relates two lexical senses of two lexical entries that stand in a translation relation to one another. </div>

<div class="description">
<subproperty>[=Sense Relation=]</sub>
</div>
</div>

With the translation property, the above example can be replaced with:

<aside class="example">
[![no
desc](Examples/vartrans/example7.png)](Examples/vartrans/example7.png){.tn}

```turtle
:zip_code a ontolex:LexicalEntry;
      dct:language <http://id.loc.gov/vocabulary/iso639-2/eng>, <http://lexvo.org/id/iso639-1/en> ;
      ontolex:sense :zip_code_sense.

:zip_code_sense ontolex:reference <http://dbpedia.org/ontology/zipCode>.

:postleitzahl a ontolex:LexicalEntry;
      dct:language <http://id.loc.gov/vocabulary/iso639-2/de>, <http://lexvo.org/id/iso639-1/de> ;
      ontolex:sense :postleitzahl_sense.

:postleitzahl_sense ontolex:reference <http://de.dbpedia.org/resource/Postleitzahl>.

:zip_code_sense vartrans:translation :postleitzahl_sense.
```

</aside>
</section>

<section id="translatable-as">
## Translatable As

The third option foreseen in the `vartrans`{.cm} model is one where we
say that a lexical entry can be translated into some other entry in some
contexts, underspecifying the exact lexical senses involved and the
exact contextual conditions under which this translation is valid. For
this, the model introduces the property
[=translatableAs=]:

<div class="entity" about="vartrans:translatableAs" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Translatable As</objectProperty>

<div property="rdfs:comment"> The <dfn>translatableAs</dfn> property relates a lexical entry in some language to a lexical entry in another language that it can be translated as depending on the particular context and specific senses of the involved lexical entries. </div>

<div class="description">
<domain>[=Lexical Entry=]</domain>
<range>[=Lexical Entry=]</range>
<symmetric/>
<subproperty>[=is sense of=] o [=translation=] o [=sense=]</subproperty>
</div>
</div>

The following example shows how to use the relation
`translatableAs`{.cm} to specify that *corner* (which can mean street
intersection or intersection of two inside walls) can be translated as
the Spanish *rincón* (intersection of two inside walls) or *esquina*
(street intersection), depending on the particular sense involved.

<aside class="example">
[![no
desc](Examples/vartrans/example8.png)](Examples/vartrans/example8.png){.tn}

```turtle
:corner a ontolex:LexicalEntry;
      dct:language <http://id.loc.gov/vocabulary/iso639-2/eng>, <http://lexvo.org/id/iso639-1/en> .
 
:rincón a ontolex:LexicalEntry;
       dct:language <http://id.loc.gov/vocabulary/iso639-2/es>, <http://lexvo.org/id/iso639-1/es> .

:esquina a ontolex:LexicalEntry;
       dct:language <http://id.loc.gov/vocabulary/iso639-2/es>, <http://lexvo.org/id/iso639-1/es> .

:corner vartrans:translatableAs :rincón.
:corner vartrans:translatableAs :esquina.
```

</aside>
</section>

<section id="translation-set">
## Translation Set

We can group translations into a set by using the class [=translation
set=], for instance if they come from the
same language resource, or belonging to the same organisation, etc.:

<div class="entity" about="vartrans:TranslationSet" typeof="owl:Class">
<class property="rdfs:label" lang="en">Translation Set</class>

<div property="rdfs:comment"> A <dfn>translation set</dfn> is a set of translations that have some common source, e.g., a language resource or an organisation. </div>

<div class="description">
</div>
</div>

In order to relate a translation set to one of the translations
contained in it, the model defines a property
[=trans=]:

<div class="entity" about="vartrans:TranslationSet" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">trans</objectProperty>


<div property="rdfs:comment">The <dfn>trans</dfn> property relates a TranslationSet to one of its
translations.</div>

<div class="description">
<domain>[=Translation Set=]</domain>
<range>[=Translation=]</range>
</div>
</div>

<aside class="example">
[![no
desc](Examples/vartrans/example10.png)](Examples/vartrans/example10.png){.tn}

```turtle
:study a ontolex:LexicalEntry ;
  ontolex:sense :study_sense ;
  dct:language iso639:en .

:Studium a ontolex:LexicalEntry ;
  ontolex:sense :Studium_sense ;
  dct:language iso639:de .

:Untersuchung a ontolex:LexicalEntry ;
  ontolex:sense :Untersuchung_sense ;
  dct:language iso639:de .

:staidear a ontolex:LexicalEntry ;
  ontolex:ense :staidear_sense ;
  dct:language iso639:ga .

:t1 a vartrans:Translation ;
  vartrans:source :study_sense ;
  vartrans:target :Studium_sense .

:t2 a vartrans:Translation ;
  vartrans:source :study_sense ;
  vartrans:target :staidear_sense .

:t3 a vartrans:Translation ;
  vartrans:source :study_sense ;
  vartrans:target :Untersuchung_sense .

:ts1 a vartrans:TranslationSet ;
  vartrans:trans :t1, :t3 ;
  dc:source "Automatically translated"@en .

:ts2 a vartrans:TranslationSet ;
  vartrans:trans :t2 ;
  dc:source "Wiktionary"@en .
```

</aside>
</section>
</section>

<section id="lime">
## Metadata (lime)

![](Lemon_Lime_Metadata.png "Lemon_Lime_Metadata.png")

The LInguistic MEtadata (*lime*) module allows for describing metadata
at the level of the lexicon-ontology interface. This module is intended
to complement existing metadata schemas such as [Dublin
Core](http://purl.org/dc/terms), [the PROV
ontology](http://www.w3.org/TR/prov-o/),
[DCAT](http://www.w3.org/TR/vocab-dcat/) or
[VoID](http://www.w3.org/TR/void/), as *lime* provides a profile to
describe metadata as related to the lexicon-ontology interface.

Following the conceptual model of the lexicon-ontology interface, *lime*
distinguishes three main metadata entities:

1.  the reference dataset (describing the semantics of the domain, e.g.,
    the ontology),
2.  the lexicon (being a collection of lexical entries),
3.  the concept set (an optional set of lexical concepts, bearing a
    conceptual backbone to a lexicon)

*Note: the reference dataset here is not limited to OWL vocabularies,
but includes any RDF dataset which contains references to objects of a
domain of discourse.*

As a metadata vocabulary, *lime* focuses on summarizing quantitative and
qualitative information about these entities and the relations among
them.

Metadata is attached in particular to three types of sets that *lime*
distinguishes:

1.  the **set of lexicalizations**, containing the bindings between
    logical predicates in the ontology and lexical entries in the
    lexicon
2.  the **set of conceptualizations**, containing the bindings between
    lexical concepts in the concept set and entries in the lexicon
3.  the **set of lexical links**, linking lexical concepts from a
    concept set to references in an ontology

In the following sections, we provide detailed descriptions for the
*lime* vocabulary to describe metadata for the lexicon as a whole as
well as for the three types of sets described above. Metadata about
ontologies (and domain datasets as well) and lexical concept sets can be
provided by means of the already mentioned existing metadata
vocabularies.

<section id="lexicon-metadata">
## Lexicon and Lexicon Metadata

The main metadata-bearing entity in lemon is a lexicon object that
represents a collection of lexical entries for a particular language. A
small example lexicon consisting of four lexical entries for *cat*,
*marry*, *high* and *intangible assets* would look as follows:

<aside class="example">
[![no
desc](Examples/lime/example1.png)](Examples/lime/example1.png){.tn}

```turtle
:lexicon a lime:Lexicon;
   lime:language "en";
   lime:entry :lex_high;
   lime:entry :lex_cat;
   lime:entry :lex_marry;
   lime:entry :lex_intangible_assets.
```

</aside>

A lexicon is expected to consist of at least one [=lexical
entry=] and is defined as a subclass of
void:Dataset:

<div class="entity" about="lime:Lexicon" typeof="owl:Class">
<class property="rdfs:label" lang="en">Lexicon</class>

<div property="rdfs:comment"> A <dfn>lexicon</dfn> is a collection of lexical entries for a particular language or domain. </div>

<div class="description">
<subclass>[=entry=] min 1, [=language=] exactly 1, void:Dataset</subclass>
</div>
</div>

The property linking a lexicon to a lexical entry is the property entry:

<div class="entity" about="lime:entry" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Entry</objectProperty>

<div property="rdfs:comment"> The <dfn>entry</dfn> property relates a lexicon to one of the lexical entries contained in it. </div>

<div class="description">
<domain>[=Lexicon=]</domain>
<range>[=Lexical Entry=]</range>
</div>
</div>

The language property can be stated on either a lexicon or a lexical
entry (note that all entries in the same lexicon should be in the same
language and that the language of the lexicon and entry should be
consistent with the language tags used on all forms) and its value
should be a literal representing the language.

<div class="entity" about="lime:language" typeof="owl:DatatypeProperty">
<datatypeProperty property="rdfs:label" lang="en">Language</datatypeProperty>

<div property="rdfs:comment"> The <dfn>language</dfn> property indicates the language of a lexicon, a lexical entry, a concept set or a lexicalization set. </div>

<div class="description">
<domain>[=Lexicon=] OR [=Lexical Entry=] OR [=Concept Set=] OR [=Lexicalization Set=]</domain>
<range>xsd:language</range>
</div>
</div>

Beyond using the *lime:language* property, which has a Literal as a
range, it is recommended to use the Dublin Core *language* property with
reference to either [Lexvo.org](http://www.lexvo.org/) or [The Library
of Congress Vocabulary](http://id.loc.gov/vocabulary/iso639-1.html)

-   Lexvo.org codes should be of the form
    `http://www.lexvo.org/id/iso639-3/xxx` where xxx is the 3-Letter ISO
    639-3 code
-   Library of Congress codes should be of the form
    `http://id.loc.gov/vocabulary/iso639-1/xx` where xx is the 2-Letter
    ISO 639-1 code

The property [=lexical entries=] indicates the
number of lexical entries contained in a lexicon. The property is also
used for lexicalization and conceptualization sets, indicating in this
case the number of lexical entries involved in these sets.

<div class="entity" about="lime:lexicalEntries" typeof="owl:DatatypeProperty">
<datatypeProperty property="rdfs:label" lang="en">Lexical Entries</datatypeProperty>

<div property="rdfs:comment"> The <dfn>lexical entries</dfn> property indicates the number of distinct lexical entries contained in a lexicon, lexicalization set or conceptualization set. </div>

<div class="description">
<domain>[=Lexicon=] OR [=Lexicalization Set=] OR [=Conceptualization Set=]</domain>
<range>xsd:integer</range>
</div>
</div>

The model also allows us to specify the linguistic (annotation) model
used to describe characteristics of lexical entries via the
[=linguistic catalog=] property:

<div class="entity" about="lime:linguisticCatalog" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Linguistic Catalog</objectProperty>

<div property="rdfs:comment"> The <dfn>linguistic catalog</dfn> property indicates the catalog of linguistic categories used in a lexicon to define linguistic properties of lexical entries. </div>

<div class="description">
<domain>[=Lexicon=]</domain>
<range>voaf:Vocabulary</range>
</div>
</div>

As an example we may describe a simple lexicon using the above
introduced properties in addition to Dublin Core properties. The
part-of-speech of the four lexical entries is indicated using the
lexinfo vocabulary, so that the value of
[=linguistic catalog=] is set to
`http://www.lexinfo.net/ontologies/2.0/lexinfo`. In the example, there
is one (RDF) resource that represents both the lexicon itself and its
metadata:

<aside class="example">
[![no
desc](Examples/lime/example2.png)](Examples/lime/example2.png){.tn}

```turtle
:lexicon a lime:Lexicon;
   lime:language "en";
   dct:language <http://id.loc.gov/vocabulary/iso639-2/eng>, <http://lexvo.org/id/iso639-1/en> ;
   lime:lexicalEntries "4"^^xsd:integer;                                               
   lime:linguisticCatalog <http://www.lexinfo.net/ontologies/2.0/lexinfo> ;
   dct:description "This is an example lexicon"@en;                              
   dct:description "Questo è un lessico di esempio"@it;                          
   dct:creator <http://john.mccr.ae/>;                                           
   void:triples "29"^^xsd:integer ;                                                       
   lime:entry :lex_high;                                                     
   lime:entry :lex_cat;                                                      
   lime:entry :lex_marry;                                                    
   lime:entry :lex_intangible_assets.                                        

                                                                                
:lex_cat a ontolex:LexicalEntry, lexinfo:Noun;                                                
   ontolex:canonicalForm :form_cat.
:form_cat ontolex:writtenRep "cat"@en.                                          
                                                                                
:lex_marry a ontolex:LexicalEntry, lexinfo:Verb;                                              
   ontolex:canonicalForm :form_marry.                    
:form_marry ontolex:writtenRep "marry"@en .                                     
                                                                                
:lex_high a ontolex:LexicalEntry, lexinfo:Adjective;                                               
   ontolex:canonicalForm :form_high.                   
:form_high ontolex:writtenRep "high"@en .                                       
                                                                                
:lex_intangible_assets a ontolex:LexicalEntry, lexinfo:Noun;                               
  ontolex:canonicalForm :form_intangible_assets.               
:form_intangible_assets ontolex:writtenRep "intangible assets"@en.
```

</aside>
</section>

<section id="lexicalization-set">
## Lexicalization Set

A [=lexicalization set=] is a
[void:Dataset](http://vocab.deri.ie/void#Dataset) that comprises a
collection of so called *lexicalizations*, which we understand as pairs
of a lexical entry and an associated reference in the ontology.

<div class="entity" about="lime:LexicalizationSet" typeof="owl:Class">
<class property="rdfs:label" lang="en">Lexicalization Set</class>

<div property="rdfs:comment"> A <dfn>lexicalization set</dfn> is a dataset that comprises a collection of lexicalizations, that is pairs of lexical entry and corresponding reference in the associated ontology/vocabulary/dataset. </div>

<div class="description">
<subclass>void:Dataset, [=lexicon dataset=] max 1 [=Lexicon=], [=reference dataset=] exactly 1 void:Dataset, [=partition=] only [=Lexicalization Set=], [=lexicalization model=] exactly 1</subclass>
</div>
</div>

The lexicalization set is linked to the ontology and the lexicon by
means of the properties [=reference dataset=] and [=lexicon dataset=], respectively.

<div class="entity" about="lime:referenceDataset" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Reference Dataset</objectProperty>

<div property="rdfs:comment"> The <dfn>reference dataset</dfn> property indicates the dataset that contains the domain objects or vocabulary elements that are either referenced by a given lexicon, providing the grounding vocabulary for the meaning of the lexical entries, or linked to lexical concepts in a concept set by means of a lexical link set. </div>

<div class="description">
<domain>[=Lexicalization Set=] OR [=Lexical Linkset=]</domain>
<range>void:Dataset</range>
</div>
</div>

<div class="entity" about="lime:lexiconDataset" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Lexicon Dataset</objectProperty>

<div property="rdfs:comment"> The <dfn>lexicon dataset</dfn> property indicates the lexicon that contains the entries referred to in a lexicalization set or a conceptualization set. </div>

<div class="description">
<domain>[=Lexicalization Set=] OR [=Conceptualization Set=]</domain>
<range>[=Lexicon=]</range>
</div>
</div>

The optionality of the *lexicon dataset* property is required to support
other lexicalization models (e.g. RDFS, SKOS, SKOS-XL) that do not
introduce a separate notion of lexicon, since lexical entries only exist
implicitly being part of a lexicalization. The property [=lexicalization
model=] indicates the specific
lexicalization model used.

<div class="entity" about="lime:lexicalizationModel" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Lexicalization Model</objectProperty>

<div property="rdfs:comment"> The <dfn>lexicalization model</dfn> property indicates the model used for representing lexical information. Possible values include (but are not limited to) <http://www.w3.org/2000/01/rdf-schema>\# (for the use of rdfs:label), <http://www.w3.org/2004/02/skos/core> (for the use of skos:pref/alt/hiddenLabel), <http://www.w3.org/2008/05/skos-xl> (for the use of skosxl:pref/alt/hiddenLabel) and [http://www.w3.org/ns/lemon/ontolex](http://www.w3.org/ns/lemon/all){.uri} for lemon.</div>

<div class="description">
<domain>[=Lexicalization Set=]</domain>
<range>rdfs:Resource</range>
<subpropertyOf>void:vocabulary</subpropertyOf>
</div>
</div>

The model defines the property [=references=],
which indicates the number of vocabulary elements lexicalized by at
least one lexical entry. This number can be obviously smaller than the
number of entities in the ontology (in case some vocabulary elements are
not lexicalized) and the number of lexical entries in the lexicon (in
case that several lexical entries refer to the same ontology element),
respectively.

<div class="entity" about="lime:references" typeof="owl:DatatypeProperty">
<datatypeProperty property="rdfs:label" lang="en">References</datatypeProperty>

<div property="rdfs:comment"> The <dfn>references</dfn> property indicates the number of distinct ontology or vocabulary elements that are either associated with lexical entries via a lexicalization set or linked to lexical concepts via a lexical link set. </div>

<div class="description">
<domain>[=Lexicalization Set=] OR [=Lexical Linkset=]</domain>
<range>xsd:integer</range>
</div>
</div>

In the following example, we describe a lexicalization set expressing
how elements of an ontology can be verbalized in Japanese by means of
entries from a supplied lexicon. The metadata clearly tells which
ontology and lexicon are involved in the lexicalization set, that is
<http://www.example.com/ontology> and <http://www.example.com/lexicon>,
respectively, as well as the relevant natural language. The knowledge of
these facts about a lexicalization set allows us to assess its
usefulness for a given task as well to discover relevant lexicalization
sets, when we are constrained by the choice of an ontology, lexicon or
natural language.

The ontology is modelled as an instance of the class
[voaf:Vocabulary](http://purl.org/vocommons/voaf#Vocabulary) that is a
kind of [void:Dataset](http://vocab.deri.ie/void#Dataset) representing
vocabularies (both RDFS Schemas and OWL Ontologies). We benefit from the
more specific distinctions made by VOAF, by breaking down the total
number of entities in the ontology (held by the property
[void:entities](http://vocab.deri.ie/void#entities)) into separate
counts for the classes and properties (held by
[voaf:classNumber](http://vocab.deri.ie/void#entities) and
[voaf:propertyNumber](http://vocab.deri.ie/void#entities),
respectively).

Similarly, terms from the *lime* vocabulary are used to represent
statistics about the linguistic content of the lexicon and the
lexicalization set. Overall, the ontology defines 100 entities and the
lexicon 80 lexical entries; however, only 20 entities from the target
ontology have been associated with a total of 50 lexical entries. In
this sense, only 20 references from the ontology have been actually
lexicalized by linking them to a lexical entry.

When counting the entities in the ontology or, in general, in the
reference dataset, we recommend to ignore the resources describing the
ontology itself (that is an instance of the class *owl:Ontology*) as
well as other metadata entities.

<aside class="example">
[![no
desc](Examples/lime/example3.png)](Examples/lime/example3.png){.tn}

```turtle
:Lexicalization a lime:LexicalizationSet ;
  lime:language "ja";
  dct:language  <http://id.loc.gov/vocabulary/iso639-1/ja>, <http://lexvo.org/id/iso639-3/jpn> ;
  lime:lexicalizationModel <http://www.w3.org/ns/lemon/all> ;
  lime:referenceDataset <http://www.example.com/ontology> ;
  lime:lexiconDataset <http://www.example.com/lexicon> ;
  lime:references 20 ;
  lime:lexicalEntries 50 .

<http://www.example.com/ontology> a owl:Ontology, voaf:Vocabulary, void:Dataset ;
  void:entities 100 ;
  voaf:classNumber 60 ;
  voaf:propertyNumber 40 .

<http://www.example.com/lexicon> a lime:Lexicon ;
  lime:language "ja" ;
  dct:language  <http://id.loc.gov/vocabulary/iso639-1/ja>, <http://lexvo.org/id/iso639-3/jpn> ;
  lime:lexicalEntries 80 .
```

</aside>

A [=lexicalization set=] comprises a set of
pairs of a lexical entry and the corresponding reference that the
lexical entry denotes. These pairs are expressed differently depending
on the lexical model adopted:

-   In lemon, the pairs are indicated by relating a lexical entry to a
    reference through the [=denotes=] property or via
    the chain [=sense=] o
    [=reference=]

<!-- -->

-   In RDFS, a lexicalization is expressed via the property
    `rdfs:label`{.cm}.

<!-- -->

-   In SKOS(-XL), a lexicalization is expressed via the
    `skos(-xl):{pref,alt,hidden}Label`{.cm} properties.

In addition to specifying the number of entities in the ontology
lexicalized, it is also possible to give the total number of
*lexicalizations*, that is the total connections between lexical entries
and references. This number should in most cases be the same as the
total number of lexical senses defined in the lexicon. The value may be
given by the absolute number of lexicalizations:

<div class="entity" about="lime:lexicalizations" typeof="owl:DatatypeProperty">
<datatypeProperty property="rdfs:label" lang="en">Lexicalizations</datatypeProperty>

<div property="rdfs:comment"> The <dfn>lexicalizations</dfn> property indicates the total number of lexicalizations in a lexicalization set, that is the number of unique pairs of lexical entry and denoted ontology element. </div>

<div class="description">
<domain>[=Lexicalization Set=]</domain>
<range>xsd:integer</range>
</div>
</div>

In addition or alternatively to the absolute number of lexicalizations,
the model also supports the indication of the average number of
lexicalizations per ontology element:

<div class="entity" about="lime:avgNumOfLexicalizations" typeof="owl:DatatypeProperty">
<datatypeProperty property="rdfs:label" lang="en">Average Number of Lexicalizations</datatypeProperty>

<div property="rdfs:comment"> The <dfn data-lt="avgNumOfLexicalizations">average number of lexicalizations</dfn> property indicates the average number of lexicalizations per ontology element in a lexicalization set. </div>

<div class="description">
<domain>[=Lexicalization Set=]</domain>
<range>xsd:decimal</range>
</div>
</div>

The average number of lexicalizations is calculated as specified by the
following formula:

![](Formula_avgNumOfLexicalizations-v1.png "Formula_avgNumOfLexicalizations-v1.png"){style="max-width:30%;"}

The following example describes an ontology consisting of 30 ontology
elements. The corresponding lexicalization set contains 20
lexicalizations involving 15 lexical entries (so some entries have
multiple meanings in the ontology). On average, for each element in the
ontology there are thus 20/30 = 0.66 lexicalizations.

<aside class="example">
[![no
desc](Examples/lime/example4.png)](Examples/lime/example4.png){.tn}

```turtle
:Lexicalization a lime:LexicalizationSet ;
  lime:lexicalizations 20 ;
  lime:references 20 ;
  lime:lexicalEntries 15 ;
  lime:avgNumOfLexicalizations 0.66 ;
  lime:referenceDataset <http://www.example.com/ontology> ;
  lime:lexiconDataset <http://www.example.com/lexicon> .

<http://www.example.com/ontology> a owl:Ontology, void:Dataset ;
  void:entities 30 .
```

</aside>

Finally, the percentage property may be used to express the percentage
of entities in an ontology which are lexicalized, formally:

![](percentage.png "percentage.png"){style="max-width:50%;"}

<div class="entity" about="lime:percentage" typeof="owl:DatatypeProperty">
<datatypeProperty property="rdfs:label" lang="en">Percentage</datatypeProperty>

<div property="rdfs:comment"> The <dfn>percentage</dfn> property expresses the percentage of entities in the reference dataset which have at least one lexicalization in a lexicalization set or are linked to a lexical concept in a lexical linkset. </div>

<div class="description">
<domain>[=Lexicalization Set=] OR [=Lexical Linkset=]</domain>
<range>xsd:decimal</range>
</div>
</div>

</section>

<section id="partitions">
## Partitions

In many cases, we want to provide descriptive metadata about a subset of
a lexicalization set, that is for the subset representing all the
lexicalizations for a certain type of ontology entity (class, property,
etc.). To logically partition a lexicalization set, the lime module
introduces the property [=partition=]:

<div class="entity" about="lime:partition" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Partition</objectProperty>

<div property="rdfs:comment"> The <dfn>partition</dfn> property relates a lexicalization set or lexical linkset to a logical subset that contains lexicalizations for a given ontological type only. </div>

<div class="description">
<domain>[=Lexicalization Set=] OR [=Lexical Linkset=]</domain>
<range>[=Lexicalization Set=] OR [=Lexical Linkset=]</range>
<subproperty>void:subset</subproperty>
</div>
</div>

<div class="entity" about="lime:resourceType" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Resource Type</objectProperty>

<div property="rdfs:comment"> The <dfn>resource type</dfn> property indicates the type of ontological entity of a lexicalization set or lexical linkset.</div>

<div class="description">
<domain>[=Lexicalization Set=] OR [=Lexical Linkset=]</domain>
<range>rdfs:Class</range>
<functional/>
</div>
</div>

For example, we may limit our metadata about lexicalizations to a
particular class, e.g. restricting the metadata to the logical partition
of lexicalizations that denote an element in the extension of the
corresponding class:

<aside class="example">
[![no
desc](Examples/lime/example5.png)](Examples/lime/example5.png){.tn}

```turtle
:Lexicalization a lime:LexicalizationSet ;
  lime:partition :CountryPartition ;
  lime:references 2000 .

:CountryPartition
  lime:resourceType ontology:Country ;
  lime:references 50 .
```

</aside>

In addition, it is also possible to give RDF(S) or OWL types as the
target of the *resource type* property. This allows us to state the
number of classes that are lexicalized by at least one lexical entry:

<aside class="example">
[![no
desc](Examples/lime/example6.png)](Examples/lime/example6.png){.tn}

```turtle
:Lexicalization a lime:LexicalizationSet ;
  lime:partition :ClassPartition .

:ClassPartition
  lime:resourceType owl:Class ;
  lime:references 50 .
```

</aside>
</section>

<section id="lexical-linkset">
## Lexical Linkset

Lexical linksets are similar in many ways to the [=lexicalization
sets=] above in the sense that they
connect a concept set to an ontology. The primary purpose of this is to
describe the linking of a concept set such as the synsets in a wordnet
to an ontology.

<div class="entity" about="lime:LexicalLinkset" typeof="owl:Class">
<class property="rdfs:label" lang="en">Lexical Linkset</class>

<div property="rdfs:comment"> A <dfn>lexical linkset</dfn> is a dataset that comprises a collection of links between lexical concepts in a concept set and entities in a reference dataset. </div>

<div class="description">
<subclass>void:Dataset, [=conceptual dataset=] exactly 1 [=Concept Set=], [=reference dataset=] exactly 1 void:Dataset, [=partition=] only [=Lexical Linkset=]</subclass>
</div>
</div>

The lexical linkset is linked to a [=concept set=]
by means of the [=conceptual dataset=]
property:

<div class="entity" about="lime:conceptualDataset" typeof="owl:ObjectProperty">
<objectProperty property="rdfs:label" lang="en">Conceptual Dataset</objectProperty>

<div property="rdfs:comment"> The <dfn>conceptual dataset</dfn> property indicates the concept set that contains the lexical concepts referred to in a lexical linkset or a conceptualization set. </div>

<div class="description">
<domain>[=Lexical Linkset=] OR [=Conceptualization Set=]</domain>
<range>[=Concept Set=]</range>
</div>
</div>

There are several properties that are analogous to properties defined
for a [=lexicalization set=]. For example
[=concepts=] indicates the number of concepts in a
concept set:

<div class="entity" about="lime:concepts" typeof="owl:DatatypeProperty">
<objectProperty property="rdfs:label" lang="en">Concepts</objectProperty>

<div property="rdfs:comment"> The <dfn>concepts</dfn> property indicates the number of lexical concepts defined in a concept set or involved in either a lexical linkset or conceptualization set. </div>

<div class="description">
<domain>[=Concept Set=] OR [=Lexical Linkset=] OR [=Conceptualization Set=]</domain>
<range>xsd:integer</range>
</div>
</div>

Similarly, the [=links=] and
[=avgNumOfLinks=] properties are analogous to
the properties [=lexicalizations=] and
[=avgNumOfLexicalizations=].

<div class="entity" about="lime:links" typeof="owl:DatatypeProperty">
<datatypeProperty property="rdfs:label" lang="en">Links</datatypeProperty>

<div property="rdfs:comment"> The <dfn>links</dfn> property indicates the number of links between concepts in the concept set and entities in the reference dataset. </div>

<div class="description">
<domain>[=Lexical Linkset=]</domain>
<range>xsd:integer</range>
</div>
</div>

<div class="entity" about="lime:avgNumOfLinks" typeof="owl:DatatypeProperty">
<datatypeProperty property="rdfs:label" lang="en">Average Number of Links</datatypeProperty>

<div property="rdfs:comment"> The <dfn data-lt="avgNumOfLinks">average number of links</dfn> property indicates the average number of links to lexical concepts for each ontology element in the reference dataset. </div>

<div class="description">
<domain>[=Lexical Linkset=]</domain>
<range>xsd:decimal</range>
</div>
</div>

Finally, we note that the [=references=],
[=percentage=] and
[=partition=] properties apply to the [=lexical
linkset=] in the same way as to the
[=lexicalization set=].
</section>

<section id="conceptualization-set">
## Conceptualization Set

A [=conceptualization set=] is analogous
to a [=lexicalization set=], but associates
a [=concept set=] with a
[=lexicon=] and consists of *conceptualizations*,
that is pairs formed by a single lexical entry and its associated
lexical concept.

<div class="entity" about="lime:ConceptualizationSet" typeof="owl:Class">
<class property="rdfs:label" lang="en">Conceptualization Set</class>

<div property="rdfs:comment"> A <dfn>conceptualization set</dfn> is a dataset that comprises a collection of links between lexical entries in a lexicon and lexical concepts in a concept set they evoke. </div>

<div class="description">
<subclass>void:Dataset, [=lexicon dataset=] exactly 1 [=Lexicon=], [=conceptual dataset=] exactly 1 [=concept set=]</subclass>
</div>
</div>

A number of properties already described for other metadata entities can
also be used in the description of a conceptualization set.

-   the two properties indicating the lexicon dataset and the conceptual
    dataset, that is lime:lexiconDataset and lime:conceptualDataset.
-   lexicalEntries: indicating the number of distinct lexical entries
-   concepts: indicating the number of distinct lexical concepts

Additional properties have been defined specifically to characterize a
given set of conceptualizations:

<div class="entity" about="lime:conceptualizations" typeof="owl:DatatypeProperty">
<datatypeProperty property="rdfs:label" lang="en">Conceptualizations</datatypeProperty>

<div property="rdfs:comment"> The <dfn>conceptualizations</dfn> property indicates the number of distinct conceptualizations in a conceptualization set. </div>

<div class="description">
<domain>[=Conceptualization Set=]</domain>
<range>xsd:integer</range>
</div>
</div>

<div class="entity" about="lime:avgAmbiguity" typeof="owl:DatatypeProperty">
<datatypeProperty property="rdfs:label" lang="en">Average Ambiguity</datatypeProperty>

<div property="rdfs:comment"> The <dfn>average ambiguity</dfn> property indicates the average number of lexical concepts evoked by each lemma/canonical form in the lexicon. </div>

<div class="description">
<domain>[=Conceptualization Set=]</domain>
<range>xsd:decimal</range>
</div>
</div>

<div class="entity" about="lime:avgSynonymy" typeof="owl:DatatypeProperty">
<datatypeProperty property="rdfs:label" lang="en">Average Synonymy</datatypeProperty>

<div property="rdfs:comment"> The <dfn>average synonymy</dfn> property indicates the average number of lexical entries evoking each lexical concept in the concept set. </div>

<div class="description">
<domain>[=Conceptualization Set=]</domain>
<range>xsd:decimal</range>
</div>
</div>

The following example shows how to describe the metadata of a version of
[WordNet 3.0](http://wordnet.princeton.edu/) transformed into RDF. The
example illustrates how to describe the main components of the resource
(a lexicon, a concept set and a conceptualization relating them). The
transformation to RDF is based on a straightforward mapping between the
WordNet meta-model and the ontolex model:

-   *synsets* -\> [=lexical concepts=]
-   *words* -\> [=lexical entries=]
-   *senses* -\> conceptualizations

By having this mapping in mind, it should be clear how some of the
[statistics about WordNet
3.0](https://wordnet.princeton.edu/wordnet/man/wnstats.7WN.html) would
be specified by means of the vocabulary introduced by the *lime* module:

<aside class="example">
[![no
desc](Examples/lime/example7.png)](Examples/lime/example7.png){.tn}

```turtle
:WnConceptualizationSet a lime:ConceptualizationSet ;
  lime:conceptualDataset :WnConceptSet ;
  lime:lexiconDataset :WnLexicon ;
  lime:lexicalEntries "155287"^^xsd:integer ;
  lime:concepts "117659"^^xsd:integer ;
  lime:conceptualizations "206941"^^xsd:integer ;
  lime:avgAmbiguity "1.33"^^xsd:decimal ;
  lime:avgSynonymy "1.76"^^xsd:decimal
  .

:WnConceptSet a ontolex:ConceptSet ;
  lime:concepts "117659"^^xsd:integer .

:WnLexicon a lime:Lexicon ;
  lime:lexicalEntries "155287"^^xsd:integer .
```

</aside>
</section>

<section id="formal-definition">
## Formal definition of properties

The lime module essentially provides vocabulary to describe the relation
between three sets:

-   *L*: the set of lexical entries
-   *O*: the set of ontology elements
-   *C*: the set of concepts

The model considers binary relations over these sets as follows:

-   R~lex~ ⊆ *O* × *L*: the set of **lexicalizations**, that is the set
    of pairs (*o*,*l*), with *o* ∈ *O*, *l* ∈ *L*.
-   R~con~ ⊆ *L* × *C*: the set of **conceptualizations**, that is the
    set of pairs (*l*,*c*), with *l* ∈ *L*, *c* ∈ *C*
-   R~links~ ⊆ *O* × *C*: the set of **links** between ontology
    references and concepts, that is the set of pairs (*o*,*c*), with
    *o* ∈ *O*, *c* ∈ *C*

For each R~i~, it holds that the relation is a subset of the Cartesian
product of the involved sets, i.e. R~i~ ⊆ *A* × *B*

For each of these relations R~i~ ⊆ *A* × *B*, we define the following
counts:

-   \'\'cardinality(R~i~) \'\': the total number of pairs in the
    relation R~i~
-   *count(π~A~(R~i~))*: the *a*\'s that occur in at least one pair in R
    = \|{*a* ∈ *A* \| ∃ *b* ∈ *B* . (*a*,*b*) ∈ R}\|
-   *count(π~B~(R~i~))*: the *b*\'s that occur in at least one pair in R
    = \|{*b* ∈ *B* \| ∃ *a* ∈ *A* . (*a*,*b*) ∈ R}\|

and ratios:

-   *coverage~A~(R~i~)*: ratio between the elements in A that
    participate in at least one (*a*,*b*) pair, and the total number of
    elements in A, that is *coverage~A~(R~i~)* = \|{*a* ∈ A \| ∃ *b* ∈ B
    . (*a*,*b*) ∈ R}\| / \|A\|
-   *average~A~(R~i~)*: average number of *b*'s in B related with each
    *a* in A, that is *average~A~(R~i~)* = \|R\| / \|A\|
-   *average~B~(R~i~)*: average number of *a*'s in A related with each
    *b* in B, that is *average~B~(R~i~)* = \|R\| / \|B\|

The lime model does not introduce all the properties to express all of
the above counts for all three relations, but has selected to model the
following relations:

  Relation              Related Dataset                                                 cardinality(R~i~)         count(π~A(R~i~)~)     count(π~B(R~i~)~)     coverage~A~(R~i~)     average~A~(R~i~)          average~B~(R~i~)
  --------------------- --------------------------------------------------------------- ------------------------- --------------------- --------------------- --------------------- ------------------------- ---------------------
  R~lex~ ⊆ *O* × *L*    [=Lexicalization Set=]         lime:lexicalizations      lime:references       lime:lexicalEntries   percentage            avgNumOfLexicalizations   \-\-\-- N/A \-\-\--
  R~con~ ⊆ *L* × *C*    [=Conceptualization Set=]   lime:conceptualizations   lime:lexicalEntries   lime:concepts         \-\-\-- N/A \-\-\--   avgAmbiguity              avgSynonymy
  R~link~ ⊆ *O* × *C*   [=Lexical Linkset=]               lime:links                lime:references       lime:concepts         percentage            avgNumOfLinks             \-\-\-- N/A \-\-\--


</section>


<section id="publication-scenarios">
## Publication Scenarios

In this section, we describe different publication scenarios for lemon
models. The lexicon ontology model essentially describes three types of
entities:

-   **lexicons**: represented by a [=Lexicon=]
-   **lexicalizations**: relating lexical entries to vocabulary
    elements; represented by a
    [=Lexicalization Set=]
-   **reference dataset or ontology vocabulary**: represented by a [VoID
    Dataset](http://rdfs.org/ns/void#Dataset) or some other subclass
    such as [VOAF
    Vocabulary](http://purl.org/vocommons/voaf#Vocabulary).

Irrespective of their logical dependencies, all of the entities above
can be published as physically independent data sources. At the other
end of the set of options, the entities can be published together as one
data source.

We highlight four common publication scenarios:

1.  **Independent resources:** A reference dataset, a lexicon and a
    lexicalization set are published as independent data sources. This
    scenario is very common in case of independently developed
    resources. A reference dataset and a general-purpose (i.e. not
    tailored towards that dataset) lexicon exist and are published
    separately (possibly by different publishers). A third party then
    decides to link these datasets by a [=lexicalization
    set=] and publishes it as a third
    entity and advertises it through proper lime metadata.
2.  **Linking to 3rd party lexicon:** A general-purpose lexicon is
    published as an independent resource. Then, in developing a
    reference dataset/ontology, its authors decide to publish it
    together with a lexicalization set based on the lexical entries from
    the existing lexicon.
3.  **Linking to 3rd party ontology:** A lexicon tailored to an existing
    reference dataset is published together with a lexicalization set.
    This is the opposite scenario to scenario 2 above. In this case the
    reference dataset or ontology vocabulary is the pre-existing
    resource developed by some 3rd party, and a lexicon is created ad
    hoc for it, with the associated lexicalizations.
4.  **Integrated:** Reference dataset, dataset-specific lexicon and
    lexicalization set are combined into a single data source: this
    scenario corresponds to closed environments where a single party is
    in control of the ontology, the lexicon and the lexicalizations and
    publishes the three as one dataset. In this scenario, the reference
    dataset is created and lexicalized with lexical elements created
    specifically for it. This scenario is the typical setting of
    ontology vocabularies/datasets naturally lexicalized by means of
    `rdfs:label`{.cm}, `skos`{.cm} or `skosxl`{.cm} labeling properties.

Similarly, there is *Concept Set* for a collection of lexical concepts
and `ConceptualizationSet`{.cm} for the triples expressing how lexical
concepts relate to lexical entries from a given lexicon. Similar
considerations to the ones above apply to these datasets.

Identifying a Concept Set as an independent dataset allows reusing the
same lexical concepts across different conceptualization sets. For
example, this allows us to reuse the same lexical concepts from an
existing wordnet to conceptualize a lexicon in a different natural
language than the one for which the resource was initially conceived.
Otherwise, it is possible to define different concept sets, one for each
conceptualization set, and then to relate them via a VoID
`Linkset`{.cm}.
</section>
</section>

<section id="linguistic-description">
## Linguistic Description

An important goal of a lexicon is to record linguistic properties of the
lexical entries defined in the lexicon such as its part-of-speech,
gender, aspect, inflectional pattern, etc. The lemon model does not
prescribe any vocabulary for doing so, but leaves it at the discretion
of the user of the model to select an appropriate vocabulary that is in
line with a given theoretical linguistic framework or grammar. We show
below how third party category systems can be reused to describe the
properties of lexical entires in a lemon lexicon. We will use the
\[<http://lexinfo.net/ontology/2.0/lexinfo>\# lexinfo\] ontology in our
examples as such as third party ontology describing relevant linguistic
categories and properties.

<section id="morphosyntactic-description">
## Morphosyntactic Description

A lexicon typically indicates the part-of-speech of a given lexical
entry. We can specify the part of speech of a word as follows using the
lexinfo vocabulary:

<aside class="example">
[![no
desc](Examples/description/example1.png)](Examples/description/example1.png){.tn}

```turtle
:cat a ontolex:Word ;
  lexinfo:partOfSpeech lexinfo:noun .
```

</aside>

When defining categories, it is crucial to link these categories to
other models to establish coherence. The **partOfSpeech** property is
defined as follows in lexinfo:

<aside class="example">
[![no
desc](Examples/description/example2.png)](Examples/description/example2.png){.tn}

```turtle
lexinfo:partOfSpeech 
  rdfs:label "part of speech"@en ;
  rdfs:comment "A category assigned to a word based on its grammatical and semantic properties."@en ;
  dcr:datcat <http://www.isocat.org/datcat/DC-1345> ,
             <http://www.isocat.org/datcat/DC-396> ;
  rdfs:range lexinfo:PartOfSpeech ;
  rdfs:subPropertyOf lexinfo:morphosyntacticProperty .
```

</aside>

The concrete part of speech \"noun\" is defined as follows and linked to
the ISOcat category DC-1333.

<aside class="example">
[![no
desc](Examples/description/example2b.png)](Examples/description/example2b.png){.tn}

```turtle
lexinfo:noun
  a lexinfo:PartOfSpeech, lexinfo:NounPOS ;
  rdfs:label "noun"@en ;
  rdfs:comment "Part of speech used to express the name of a person, place, action or thing."@en ;
  dcr:datcat <http://www.isocat.org/datcat/DC-1333> .
```

</aside>

The following morpho-syntactic properties are defined in the lexinfo
ontology:

-   **Animacy**: indicating whether a word denotes something animate
    (human or animal)
-   **Aspect**: indicating the grammatical aspect (e.g. perfect or
    imperfect for verbs)
-   **Case**: indicating the grammatical case (e.g. nominative,
    accusative, dative, genitive, etc.)
-   **Cliticness**: indicating whether the word acts as a clitic
-   **Definiteness**: indicating whether the word refers to a particular
    element in a set
-   **Degree**: indicating whether an adjective is comparative or
    superlative
-   **Finiteness**: indicating whether the form is finite
-   **Gender**: indicating the grammatical gender of a word (e.g.
    female, masculine, neuter etc.)
-   **Modification Type**: indicating whether a modifier precedes or
    follows a word
-   **Mood**: indicating the modality (imperative, conditional, etc.) of
    a verb
-   **Negative**: indicating the negative form of verbs (e.g. in
    Japanese)
-   **Number**: indicating the grammatical number of a word (e.g.
    singular, plural, etc.)
-   **Part of speech**: indicating the syntactic category of the word in
    question (e.g. noun, verb, adjective, etc.)
-   **Person**: indicating whether a noun or pronoun refers to the
    speaker (first person) or listener (second person) or other entity
    (third person) and agreeing forms of verbs
-   **Tense**: indicating whether a word makes a temporal reference to
    the past, present or future
-   **Voice**: indicating the type of sentence (active vs. passive
    voice)

When using these properties, care should be taken to distinguish between
linguistic properties of the entry itself and properties of any of the
forms. By default, it should be assumed that a property of a lexical
entry also holds for all its forms. For example, in many languages
gender is an entry property for nouns, but a form property for
adjectives, for example:

<aside class="example">
[![no
desc](Examples/description/example3.png)](Examples/description/example3.png){.tn}

```turtle
:spiaggia a ontolex:Word ;
  ontolex:canonicalForm :spiaggia_lemma ;
  ontolex:otherForm spiaggia_plural ;
  lexinfo:partOfSpeech lexinfo:noun ;
  lexinfo:gender lexinfo:feminine .

:spiaggia_lemma 
  ontolex:writtenRep "spiaggia"@it ;
  lexinfo:number lexinfo:singular .

:spiaggia_plural
  ontolex:writtenRep "spiagge"@it ;
  lexinfo:number lexinfo:plural .

:famoso a ontolex:Word ;
  ontolex:canonicalForm :famoso_lemma ;
  ontolex:otherForm :famosa_form, :famose_form, famosi_form ;
  lexinfo:partOfSpeech lexinfo:adjective .

:famoso_lemma
  ontolex:writtenRep "famoso"@it ;
  lexinfo:number lexinfo:singular ;
  lexinfo:gender lexinfo:masculine .

:famosa_form 
  ontolex:writtenRep "famosa"@it ;
  lexinfo:number lexinfo:singular ;
  lexinfo:gender lexinfo:feminine .
```

</aside>

For convenience, lexinfo also introduces specific classes for each part
of speech so that the part of speech of a word can be specified by a
rdf:type statement. For example, the part of speech Noun is defined as
follows:

*Noun* ≡ ∃ partOfSpeech.NounPOS

It is recommended to use both the rdf:type statement as well as the
**lexinfo:partOfSpeech** to maximize interoperability in spite of the
small redundancy:

<aside class="example">
[![no
desc](Examples/description/example4.png)](Examples/description/example4.png){.tn}

```turtle
:geneesmiddel a lexinfo:Noun ;
  lexinfo:partOfSpeech lexinfo:noun .
```

</aside>
</section>

<section id="pragmatic-paradigmatic-description">
## Paradigmatic Description

Pragmatic aspects related to the usage of a lexical entry as well as the
paradigmatic relationships between lexical entries can also be described
using the lemon model by resorting to some external vocabulary. As for
the case of the description of the morphosyntactic properties of lexical
entries and their forms, lemon does not prescribe any vocabulary but
encourages the use of external vocabularies to describe aspects related
to the temporal use of a lexical entry, e.g. to indicate whether the use
of the lexical entry is modern or anachronic or to specify
lexico-semantic relationships between lexical senses. Examples of such
paradigmatic or lexico-semantic relationships are: synonymy, antonymy,
holonymy, hypernymy, meronymy, etc.
</section>

<section id="arguments">
## Arguments

When describing syntactic frames it is important to specify the
grammatical role or function played by different syntactic arguments. We
might want to specify, for instance, which argument plays the
grammatical role of subject and which argument plays the role of a
direct object, etc. LexInfo distinguishes the following types of
arguments:

-   **Subject**: indicating the syntactic subject of a sentence. The
    subject typically expresses the agent of the action denoted by the
    verb, but this need not to be so in all cases. In a passive
    construction, the subject actually expresses the patient or
    beneficiary of the action denoted by the verb.
-   **Object:** distinguishing between direct, indirect, prepositional
    (a non-optional object marked with a preposition) and genitive
    objects
-   **Adjunct**: adjuncts are optional arguments. Lexinfo distinguishes
    between *prepositional*, *possessive*, *comparative* and
    *superlative* arguments.
-   **Copulative**: a copulative argument indicates one argument
    involved in a so called [copula
    construction](https://en.wikipedia.org/wiki/Copula_(linguistics))
    involving a copulative verb. Lexinfo distinguishes the copulative
    subject and the copula predicate.
-   **Clausal**: certain verbs also subcategorize a whole clause or
    sentence as an argument (e.g. the verb (to) claim). In this case
    lexinfo talks about a clausal argument and distinguishes between
    declarative, gerundive, infinitive, interrogative (infinitive),
    possessive infinitive, prepositional gerund/interrogative,
    sentential or subjunctive clausal arguments.
-   **Attributive**: The word modified by an an adjective in an
    [attributive construction](https://en.wikipedia.org/wiki/Adjective)

Each argument is associated with a specific property indicating the
grammatical role to the actual object representing the syntactic
argument.

<aside class="example">
[![no
desc](Examples/description/example6.png)](Examples/description/example6.png){.tn}

```turtle
:father a lexinfo:Noun ;
  synsem:synBehavior :father_frame.

:father_frame a lexinfo:NounPredicateFrame ;
  rdfs:label "X is the father of Y" , "X is Y's father" ;
  lexinfo:copulativeArg :father_frame_arg1 ;
  lexinfo:possessiveAdjunct :father_frame_arg2 .

:father_frame_arg1 a lexinfo:CopulativeArg .

:father_frame_arg2 a lexinfo:PossessiveAdjunct .
```

</aside>
</section>

<section id="frames">
## Frames

Syntactic or subcategorization frames describe which syntactic arguments
a certain lexical entry (verb, noun etc.) requires to be complete. A
verb that requires a subject and a direct object is called a *transitive
verb*. The corresponding frame that generalizes across particular verbs
is called *transitive* frame or *transitive construction* (in
construction grammar theories).

In lexinfo, frames can be axiomatized by describing which type of
arguments they subcategorize. A transitive frame would be axiomatized as
follows in lexinfo:

` TransitiveFrame ≡ VerbFrame ⊓ (=1 subject ⊓ =1 directObject)`{.cm}
</section>

<section id="other-properties">
## Other properties

In addition, it is possible to define other properties in an external
resource, that may be difficult to translate across resources. An
example of such a property is translation confidence as shown below:

<aside class="example">
[![no
desc](Examples/vartrans/example9.png)](Examples/vartrans/example9.png){.tn}

```turtle
:bench a ontolex:LexicalEntry ;
        ontolex:lexicalForm [ ontolex:writtenRep "bench"@en].

:bench-sense a ontolex:LexicalSense ;
        ontolex:isSenseOf :bench .

:banco a ontolex:LexicalEntry ;
        ontolex:lexicalForm [ ontolex:writtenRep "banco"@es].

:banco-sense a ontolex:LexicalSense ;       
        ontolex:isSenseOf :banco .


:tranSetEN-ES a vartrans:TranslationSet ;
        dc:source <http://hdl.handle.net/10230/17110> ;
        vartrans:trans :bench_banco-trans .

:bench_banco-trans a vartrans:Translation ;
        vartrans:source :bench-sense ;
        vartrans:target :banco-sense .


:tranSetEN-ES a prov:Entity .  
:bench_banco-trans a prov:Entity .
    
:humanTranslationActivity a prov:Activity .
:executionOfMyAlgorithm a prov:Activity .

:bench_banco-trans prov:qualifiedGeneration [
     a prov:Generation ;
     prov:activity :humanTranslationActivity ;
     lexinfo:translationConfidence 1.0 ;
] .

:bench_banco-trans prov:qualifiedGeneration [
     a prov:Generation ;
     prov:activity :executionOfMyAlgorithm ;
     lexinfo:translationConfidence 0.3 ;
] .
```

</aside>
</section>
</section>

<section id="lexical-nets">
## Lexical Nets

Lexical nets, so called wordnets in particular, are an important type of
lexical resource used very often in natural language processing
applications. Lexical nets organize the senses of words into groups of
equivalent meaning, so called *synsets*. Further, synsets are related to
each other using lexico-semantic relationships so that the the resource
can be regarded as a \"net\". We discuss below how lexical nets can be
represented using the lemon vocabulary using Princeton wordnet as an
example.

<section id="wordnet">

## Lexical nets in OntoLex-lemon {#lexical-nets-in-lemon}

As mentioned above, lexical nets indicate the different lexical senses
that a word has and groups these senses into sets of equivalent senses
(so called synsets). Below we state how the main entities of a lexical
net (words, lemmas, senses and synsets) can be represented in lemon:

-   **Synset**: Lexical Concept
-   **Word**: Lexical Entry
-   **(Word) Sense**: Lexical Sense
-   **Lemma**: Canonical Form

Lexico-semantic relations should be represented between lexical
concepts. The WordNet-RDF ontology defines some of these lexico-semantic
relations:

[`http://globalwordnet.github.io/schemas/wn#`{.cm}](http://globalwordnet.github.io/schemas/wn#)

An full description of the Global WordNet Association extension of
OntoLex-lemon is available
[here](http://globalwordnet.github.io/schemas/#rdf), and an example of
modelling is given here:

<aside class="example">
[![no
desc](Examples/wordnet/example1.png)](Examples/wordnet/example1.png){.tn}

```turtle
<#example-en> a lime:Lexicon ;
  rdfs:label "Example wordnet (English)"@en ;
  dc:language "en" ;
  schema:email "john@mccr.ae" ;
  cc:license <https://creativecommons.org/publicdomain/zero/1.0/> ;
  owl:versionInfo "1.0" ;
  schema:citation "CILI: the Collaborative Interlingual Index. Francis Bond, Piek Vossen, John P. McCrae and Christiane Fellbaum, Proceedings of the Global WordNet Conference 2016, (2016)." ;
  schema:url "http://globalwordnet.github.io/schemas/" ;
  dc:publisher "Global Wordnet Association" ;
  lime:entry <#w1>, <#w2>, <#w3> .

<#w1> a ontolex:LexicalEntry ;
  ontolex:canonicalForm [
    ontolex:writtenRep "grandfather"@en 
  ] ;
  wn:partOfSpeech wn:noun ;
  ontolex:sense <#example-10161911-n-1> .

<#example-10161911-n-1>  a ontolex:LexicalSense ;
  ontolex:reference <#example-10161911-n> .

<#w2> a ontolex:LexicalEntry ;
  ontolex:canonicalForm [
    ontolex:writtenRep "paternal grandfather"@en 
  ] ;
  wn:partOfSpeech wn:noun ;
  ontolex:sense <#example-1-n-1> .

<#example-1-n-1> a ontolex:LexicalSense ;
  ontolex:reference <#example-1-n> .

[] a vartrans:SenseRelation ;
  vartrans:source <#example-1-n-1> ;
  vartrans:category wn:derivation ;
  vartrans:target <#example-10161911-n-1> ;
  dc:creator "John McCrae"@en .
          
<#w3> a ontolex:LexicalEntry ;
  ontolex:canonicalForm [
    ontolex:writtenRep "pay"@en
  ] ;
  wn:partOfSpeech wn:verb ;
  synsem:synBehavior [
    rdfs:label "Sam cannot %s Sue" @en
  ], [
    rdfs:label "Sam and Sue %s"@en
  ], [
    rdfs:label "The banks %s the check"@en
  ] .

<#example-10161911-n> a ontolex:LexicalConcept ;
  skos:inScheme <#example-en> ;
  wn:ili ili:i90287 ;
  wn:definition [
    rdf:value "the father of your father or mother"@en
  ] .

[] 
  vartrans:source <#example-10161911-n> ;
  vartrans:category wn:hypernym ; 
  vartrans:target <#example-10162692-n> .
          
<#example-1-n> a ontolex:LexicalConcept ;
  skos:inScheme <#example-en> ;
  wn:definition [
    rdf:value "the father of your father or mother"@en 
  ] ;
  wn:iliDefinition [
    rdf:value "the father of your father or mother"@en ;
    dc:source "https://en.wiktionary.org/wiki/farfar"
  ] .

[]
  vartrans:source <#example-1-n> ;
  vartrans:category wn:hypernym ;
  vartrans:target <#example-10162692-n> .

<#example-sv> a lime:Lexicon ;
  rdfs:label "Example wordnet (Swedish)"@sv ;
  dc:language "sv" ;
  schema:email "john@mccr.ae" ;
  cc:license <https://creativecommons.org/publicdomain/zero/1.0/> ;
  owl:versionInfo "1.0" ;
  schema:citation "CILI: the Collaborative Interlingual Index. Francis Bond, Piek Vossen, John P. McCrae and Christiane Fellbaum, Proceedings of the Global WordNet Conference 2016, (2016)." ;
  schema:url "http://globalwordnet.github.io/schemas" ;
  dc:publisher "Global Wordnet Association" ;
  lime:entry <#w4> .

<#w4> a ontolex:LexicalEntry ;
  ontolex:canonicalForm [
    ontolex:writtenRep "farfar"@sv 
  ] ;
  ontolex:otherForm [
    ontolex:writtenRep "farfäder"@sv ;
    wn:tag "NNS" 
  ] ;
  wn:partOfSpeech wn:noun ;
  wn:sense <#example-2-n-1> .

<#example-2-n-1> a ontolex:LexicalSense ;
  ontolex:reference <#example-1-n> ;
  wn:example [
    rdf:value "Jag vill berätta för er att min farfar var svensk beredskapssoldat vid norska gränsen under andra världskriget, ett krig som Sverige stod utanför"@sv ;
    dc:source "Europarl Corpus"
  ] .
```

</aside>
</section>
</section>

<section id="relation-to-other-models">
## Relation to Other Models

In this section, we informally clarify the relation to other models, in
particular SKOS, the Lexical Markup Model (LMF), and the Open Annotation
standard.

<section id="relation-to-skos">
## SKOS(-XL)

SKOS is a vocabulary used to represent so called *knowledge organization
systems* (KOS), comprising taxonomies, classification schemes, thesauri
etc. SKOS thus addresses an orthogonal use case to lemon. lemon was
designed to provide detailed information about the linguistic grounding
of an ontological vocabulary, specifying in particular by which lexical
entries a class or property can be verbalized. SKOS has only a very
rudimentary way of doing this, that is by means of SKOS labels and the
properties (prefLabel, altLabel and hiddenLabel). This is by no means a
criticism of SKOS, but merely to make clear that SKOS and lemon have
been designed with a different purpose and use case in mind.

Nevertheless, SKOS and lemon can be used in conjunction to provide more
detailed information about the \"labels\". We recommend to use the
property [=evokes=] and its inverse isEvokedBy to
relate a skos:Concept to a [=lexical entry=].
This is shown in the following example:

The use case we address is one where a thesaurus or other taxonomic
resource or classification system in SKOS needs to be enriched with more
detailed linguistic information.

<aside class="example">
[![no
desc](Examples/other/example-skos1.png)](Examples/other/example-skos1.png){.tn}

```turtle
:financial_assets a skos:Concept;
                ontolex:lexicalizedSense :financial_assets_lex.

:financial_assets_lex a ontolex:LexicalEntry;
                 ontolex:evokes :financial_assets;
                 ontolex:canonicalForm :financial_assets_form. 

:financial_assets_form ontolex:writtenRep "financial assets".
```

</aside>

The above represents the recommended way of linking a SKOS concept to a
lexical entry in the lexicon ontology model.

To show how to make statements about preferred lexicalizations akin to
the properties `prefLabel`{.cm}, `altLabel`{.cm} and `hiddenLabel`{.cm}
as used in SKOS, the following example shows how to attach such
preference information via the lexical senses:

<aside class="example">
[![no
desc](Examples/other/example-skos2.png)](Examples/other/example-skos2.png){.tn}

```turtle
:tuberculosis a skos:Concept;
     ontolex:isEvokedBy :tuberculosis_lex;
     ontolex:isEvokedBy :consumption_lex.

:tuberculosis_lex a ontolex:LexicalEntry;
      ontolex:sense :tuberculosis_sense;
      ontolex:evokes :tuberculosis.
   
:tuberculosis_sense a ontolex:LexicalSense;
      ontolex:isLexicalizedSenseOf :tuberculosis; 
      ontolex:usage [ rdf:value "preferred" ].

:consumption_lex a ontolex:LexicalEntry;
       ontolex:sense :consumption_sense;
       ontolex:evokes :tuberculosis.

:consumption_sense a ontolex:LexicalSense;
        ontolex:isLexicalizedSenseOf :tuberculosis;
        ontolex:usage [ rdf:value "outdated" ]. 
```

</aside>

In case you are using reified labels as in SKOS-XL, it is possible to
have forms or lexical entries in the range of the
`skosxl:prefLabel`{.cm}, `skosxl:altLabel`{.cm} and
`skosxl:hiddelLabel`{.cm} properties. However, we note that from this it
would follow that lexical entries and forms would be inferred to be
`skosxl:Label`{.cm}s, which does not correspond to the understanding of
forms and lexical entries of this community as linguistic objects rather
than mere \`labels\'.
</section>

<section id="relation-to-lmf">
## LMF

The Lexical Markup Framework (LMF) (ISO-24613:2008) is a standard for
representing machine readable lexicons. The model is not suited,
however, to publish lexica on the web as linked data as it only knows a
serialization in XML rather than in RDF. Further, LMF does not address
the interface between lexica and ontologies as lemon does.

Nevertheless, the lemon model draws heavy inspiration from the LMF
model. lemon has imported many classes/entities from LMF and adopted its
core ontology. On the other hand, lemon has added vocabulary to describe
the syntax-semantics interface with respect to an ontology and remove a
number of classes that create syntactic overhead. A complete description
of the relationship between LMF and the original lemon model is provided
[here](http://lemon-model.net/lemon-cookbook/node46.html). The main
differences are summarized here:

-   lemon defines the meaning of a term by reference to an ontology
    element defined by the OWL model.
-   lemon provides a more compact description than LMF to describe the
    syntax-semantics interface
-   lemon relies on external category system and linguistic ontologies
    to describe linguistic properties of lexical entries instead of
    proposing an own category system
-   lemon does not include a module for describing inflectional
    morphology patterns (called intentional morphology in LMF). Further,
    it does not allow to define global constraints on the lexicon. This
    can be done using OWL axioms, but not in lemon itself.
</section>

<section id="relation-to-open-annotation">
## OpenAnnotation

In many uses cases the need arises to annotate a text corpus with links
to entities defined in a lexicon, e.g. lexical entries, forms, lexical
senses, lexical concepts etc. lemon does not support this annotation per
se, as there are other models that are dedicated exactly to this. This
is the case for the [Open Annotation](http://openannotation.org/)
standard. In both models an element of the lexicon may be the target of
an annotation. This target may be a form, lexical entry, lexical sense
or lexical concept and it is important to give the class to make clear
what the target of the annotation is.

We will now give an example of annotating a word \"cat\" occurring at
character 7 in a file at the URL [2](http://www.example.com/doc.txt),
where the *lemon* element is given as the body of an annotation. For
example

<aside class="example">
[![no
desc](Examples/other/example-oa.png)](Examples/other/example-oa.png){.tn}

```turtle
@prefix dctypes: <http://purl.org/dc/dcmitype/> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix ontolex: <http://www.w3.org/ns/lemon/ontolex#> .

:annotation a oa:Annotation ;
  oa:hasBody :cat ;
  oa:hasTarget <anno#target> .

:annotation#target a dctypes:Text ;
  oa:hasSelector <http://www.example.com/doc.txt#char=7,10> .

<http://www.example.com/doc.txt#char=7,10> a oa:FragmentSelector .

<cat> a ontolex:LexicalEntry .
```

</aside>
</section>
</section>

<section id="acknowledgements">
## Acknowledgements

The following persons have contributed to the creation of this document
and are gratefully acknowledged.

-   Guadalupe Aguado-de-Cea, Ontology Engineering Group, Universidad
    Politécnica de Madrid, Spain
-   Manuel Fiorelli, Università degli Studi di Roma Tor Vergata, Italy
-   Francesca Frontini, Institute for Computational Linguistics «A.
    Zampolli», Italian National Research Council, Italy
-   Aldo Gangemi, Laboratoire d\'Informatique de Paris Nord, Université
    Paris 13, France
-   Jorge Gracia, Ontology Engineering Group, Universidad Politécnica de
    Madrid, Spain
-   Thierry Declerck, Deutsches Forschungszentrum für Künstliche
    Intelligenz GmbH, Germany
-   Anas Fahad Khan, Institute for Computational Linguistics «A.
    Zampolli», Italian National Research Council, Italy
-   Elena Montiel Ponsoda, Ontology Engineering Group, Universidad
    Politécnica de Madrid, Spain
-   Armando Stellato, Università degli Studi di Roma Tor Vergata, Italy
</section>
