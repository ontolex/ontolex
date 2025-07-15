# Requirements for OntoLex Core 2.0 
Last update: 15/05/2025

## Introduction
This is a unified relation of the requirements for OntoLex core model v2, grouped in three different topics, as thery were identified and reported by the community. The list is complete but the different requirements are not described in full in detail. For this, please refer to the source documents: 
* Lexicography (see https://github.com/ontolex/ontolex/blob/master/notes/Lexicographic_Requirements.md)
* Terminology (see https://github.com/ontolex/ontolex/blob/master/notes/terminology-requirements.md)
* Alignment with DMLex model (see https://github.com/ontolex/ontolex/blob/master/notes/dmlex-requirements.md)

## Lexicography requirements 
- **RL1**. Need to **associate a lexical sense to a particular form** of a lexical entry, e.g., game, games [^2] (not limited to lexicographic resources but is common in them) 
- **RL2**. Need to have entry **elements with different parts of speech** (frequent in dictionaries, creation of different entries in this case creates disparity with original source in case of retrodigitization)
- **RL3**. Need to include **usage examples** (common in dictionaries) 
- **RL4**. Need to associate **diachronic/diatopic information**, e.g., _fanny_ in UK v. US English [^3] (common in dictionaries)
- **RL5**. Need to **organise senses**, both by ordering as well as nesting them 
- **RL6**. Need to represent **order of lexical entries**, since not all languages use alphabetical order [^4] (as well as other layout information, e.g., which page is an entry on in an original source dictionary)
- **RL7**. Need to describe **senses that may not have corresponding ontological references** associated with them, or where it may not make sense [^5]. Semantics by reference isn’t always suitable for dictionary senses, see cases with nested senses above and also dictionaries where what is listed as one sense listing includes different concepts (a dictionary such as the Clark Hall Concise Anglo-Saxon dictionary is full of these, e.g.,  _ealh_ is defined as ‘sheltering place, city, palace, temple’ [^6]); I shouldn’t necessarily have to work out (make a work of interpretation) what the separate sense/concepts in each definition are to encode a dictionary: because of the assumption each sense refers to one single concept in an ontology  [retro]
- **RL8**. Need to distinguish when to use **lexicog Entry vs. Lexical Entry** (this will be resolved with the Entry superclass solution which is being tentatively proposed)
- **RL9**. Need to include **definitions of dictionary senses** (using SKOS:Concept as previously recommended, assumes every dictionary sense is a SKOS:Concept, which may not be appropriate, see RL7) [retro]
- **RL10**. Need to include **see also entries** which only point to other entries as well as entries which give a single form (in the case of e.g., suppletive forms, common in a language with strong verbs such as Old English, e.g., _writan_ vs _wrat_) or spelling variations [retro]
- **RL11**. Need to include **exact wording or representation of Part of Speech or grammatical information** [retro]    

## Terminology requirements

- **RT1**. The need to have a **class for definitions**. A single triple does not suffice to capture all the key information of terminological definitions, since definition may contain additional elements such as definition references or notes about the definition. 
- **RT2**: The need to have a **class for notes**. Notes are key elements of traditional term records, providing additional information, such as usage recommendations, domain data and references; they are considered valuable pieces of knowledge for language professionals. 
This type of information is still present in authoritative resources. 
- **RT3**. The need to have a **class for usage information**. This need is derived from the observation of language level notes on different IATE entries, that contain usage recommendations of the different terms that denote the concept. 
Such usage recommendations can be expressed as string of text and links to related resources, meaning that there are different pieces of information that need to be represented. 
- **RT4**. The need to have a **class for sources**. Like definitions, sources play a very important role in this modelling approach. Especially when terminologies are generated from multiple resources, it is crucial to maintain the traceability of the different terminological data (may they be definitions, term notes, term contexts, etc.). With the automation of the terminology creation process, we may distinguish between two types of sources: Intermediate Sources: not direct sources but information providers, such as existing linguistic resources from which information is retrieved (IATE, for instance) or applications (a Definition Extractor) and Original Sources: direct sources, meaning corpora (i.e. European Legislation), organisations (i.e. European Commission) or individuals (i.e. John Doe, European terminologist).

  Checked FraC (https://github.com/ontolex/frequency-attestation-corpus-information/blob/master/index.md#citations): properties such as "citation" and "observedIn" have domain "Observation" while we need to declare sources for various types of classes, including notes and definitions.

  Checked Prov (https://www.w3.org/TR/prov-o/): property "qualifiedPrimarySource" has domain Entity.

- **RT5**. The need to have a (standardised) **class for the reliability** of a term. Previous work on the representation of terminologies as Linked Data (Cimiano, et al. 2015) proposed an ontology based on the TBX specification which used the property tbx:reliabilityCode to represent this kind confidence rating that terminologists assign to terms. However, the domain is ontolex:LexicalEntry, and the property admits any type of rating. Following the guidelines of IATE, we propose a class ReliabilityCode with a fixed set of values 1-4, to standardise this rating.
Resources with other scales for the reliability/acceptability of a term: **Termium** <https://www.btb.termiumplus.gc.ca/tpv2alpha/alpha-eng.html?lang=eng>, or **Wikiwords** <https://wikiwords.org/wikiwords>.

- **RT6**. The need to represent **record status**. Some resources include an indicator that reflects the finalization of a term entry. Some entries may be fully validated and contain all necessary information, while others might still be under review or incomplete. A dedicated class or property for record status would help users distinguish between finalized, provisional, or work-in-progress entries
In some resources, such as TERMDAT, this indicator is stricly correlated to the realiability code. https://www.termdat.bk.admin.ch/search

## DMLex requirements

- **RD1**. The need to have `partOfSpeech`: OntoLex does not have a **core part-of-speech property** unlike DMLex. This may be useful also for defining lexical entries in our model
- **RD2**. Need oto have an **inflected form** `inflectedForm`: OntoLex has `otherForm` that is similar but seems slightly broader in interpretation
- **RD3**. The need to have **example**: We probably need a property to give examples by entry and sense as well
- **RD4**. Need to represent **bilingual and multilingual dictionaries**. `headwordTranslation`, `headwordExplanation`: These give lemmas and glosses for an entry in another language. This differs from OntoLex modelling which would instead link entries/forms in two different lexicons. `exampleTranslation`: If examples are introduced, we may want to give translations (especially for historical languages)
- **RD5**. Need to align with DMLex Annotation Module. This module allows inline markup of entries in order to mark placeholders, headwords and collocates. This would be quite tricky to support in RDF, as there is no easy way to do inline markup. Perhaps, this use case could be consider in the context of the _FrAC_ module?. An example:

```xml
<text>The coroner <collocateMarker lemma="perform">performed</collocateMarker> an
      <headwordMarker>autopsy</headwordMarker>.</text>
```




 -----------
[^1]:<https://www.w3.org/community/ontolex/wiki/Lexicography>
[^2]:<https://en.wiktionary.org/wiki/game>
[^3]:<https://en.wiktionary.org/wiki/fanny>
[^4]:Of course not all languages use alphabets.
[^5]:Pardoning the pun. 
[^6]:See  also https://en.wiktionary.org/wiki/regretter
