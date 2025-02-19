# Requirements on OntoLex 2.0 from Terminology use cases
This document collects doubts and issues that arose when working with Ontolex to model terminological resources.

## I1: The need to have a class for definitions

A single triple does not suffice to capture all the key information of terminological definitions, since definition may contain additional elements such as definition references or notes about the definition.
Considering that the specification of skos:definition does not restrict the object to be a literal, we recommend definitions to be given as resources with further attributed properties.
The current spec of Ontolex-lemon (“A definition can be added to a lexical concept as a gloss by using the skos:definition property”) was somewhat nonspecific, and we believe the specification should make explicit that implementors of Ontolex-lemon should expect the text definitions to be given either as literals or as the rdf:value attributed to the definition object.
See example below. Source:https://iate.europa.eu/entry/result/1443648/.
<img width="459" alt="image" src="https://github.com/user-attachments/assets/f48714fd-74aa-4b3f-ab8b-601c92fab8f3" />

## I2: The need to have a class for notes
Notes are key elements of traditional term records, providing additional information, such as usage recommendations, domain data and references; they are considered valuable pieces of knowledge for language professionals. 
This type of information is still present in authoritative resources. See example below. Source https://iate.europa.eu/entry/result/1620578/.

<img width="521" alt="image" src="https://github.com/user-attachments/assets/ef6eb23c-e92a-4be3-af8c-72a0963117f8" />

## I3. The need to have a class for usage information

This need is derived from the observation of language level notes on different IATE entries, that contain usage recommendations of the different terms that denote the concept. 
Such usage recommendations can be expressed as string of text and links to related resources, meaning that there are different pieces of information that need to be represented. 
See example below. Source: https://iate.europa.eu/entry/result/1443648/.

<img width="437" alt="image" src="https://github.com/user-attachments/assets/73860e88-149b-4180-bd11-26e72544f367" />

## I4. The need to have a class for sources

Like definitions, sources play a very important role in this modelling approach. Especially when terminologies are generated from multiple resources, it is crucial to maintain the traceability of the different terminological data (may they be definitions, term notes, term contexts, etc.). With the automation of the terminology creation process, we may distinguish between two types of sources: Intermediate Sources: not direct sources but information providers, such as existing linguistic resources from which information is retrieved (IATE, for instance) or applications (a Definition Extractor) and Original Sources: direct sources, meaning corpora (i.e. European Legislation), organisations (i.e. European Commission) or individuals (i.e. John Doe, European terminologist).

<img width="776" alt="image" src="https://github.com/user-attachments/assets/a61186e1-928c-4232-81eb-c635caca41f6" />

## I5. The need to have a (standardised) class for the reliability of a term

Previous work on the representation of terminologies as Linked Data (Cimiano, et al. 2015) proposed an ontology based on the TBX specification which used the property tbx:reliabilityCode to represent this kind confidence rating that terminologists assign to terms. However, the domain is ontolex:LexicalEntry, and the property admits any type of rating. Following the guidelines of IATE, we propose a class ReliabilityCode with a fixed set of values 1-4, to standardise this rating.

