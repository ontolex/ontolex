# Lexicographic Requirements for OntoLex Core 2.0 (and Related Observations)
## Introduction
We make the distinction between lexical resources and lexicographic resources on the basis of the following definitions:
- Lexical resources are broader in scope and are often designed for computational applications, such as natural language processing (NLP), linguistic research, or language technology development.
- Lexicographic resources are structured according to the principles of dictionary-making and are traditionally human-oriented.
  
Our recommendation (agreed upon in the dedicated meeting of 11th of December) is that we should maintain a separate and dedicated module for lexicographic resources in future: since there are numerous things that are specific to lexicographic resources that may not fit within a core module which deals with lexical resources in general. We therefore include in our list of requirements those which led to the definition of the original module. 

Given the strong likelihood that the new core module will include an Entry class which is not restricted to one part of speech, and which is a superclass of the already existing Lexical Entry, a number of the requirements for the original module [^1] are listed here in an altered form.  Moreover, some of the following requirements are marked as [retro], in these cases we are concerned with retrodigitized dictionaries in RDF or electronic editions of traditionally formatted dictionaries, where we might want to include information on the visual appearance or exact wording of e.g., part of speech information, but not just, see R7. It should be decided the extent to which we want to deal with these (more philological) cases in an OntoLex module. Leaving them out runs the risk of putting a heavy burden of pre-processing a dictionary (to put it in an OntoLex compliant form) on anyone wishing to create an RDF version of a retrodigitized dictionary -- or it means the creation of a new RDF vocabulary dealing with such kinds of information (how much does DMLex already cover?) which should be aligned with OntoLex.

### Requirements
- R1. Need to associate a lexical sense to a particular form of a lexical entry, e.g., game, games [^2] (not limited to lexicographic resources but is common in them) 
- R2. Need to have entry elements with different parts of speech (frequent in dictionaries, creation of different entries in this case creates disparity with original source in case of retrodigitization)
- R3. Need to include usage examples (common in dictionaries) 
- R4. Need to associate diachronic/diatopic information, e.g., _fanny_ in UK v. US English [^3] (common in dictionaries)
- R5. Need to organise senses, both by ordering as well as nesting them 
- R6. Need to represent order of lexical entries, since not all languages use alphabetical order [^4] (as well as other layout information, e.g., which page is an entry on in an original source dictionary)
- R7. Need to describe senses that may not have corresponding ontological references associated with them, or where it may not make sense [^5]. Semantics by reference isn’t always suitable for dictionary senses, see cases with nested senses above and also dictionaries where what is listed as one sense listing includes different concepts (a dictionary such as the Clark Hall Concise Anglo-Saxon dictionary is full of these, e.g.,  _ealh_ is defined as ‘sheltering place, city, palace, temple’ [^6]); I shouldn’t necessarily have to work out (make a work of interpretation) what the separate sense/concepts in each definition are to encode a dictionary: because of the assumption each sense refers to one single concept in an ontology  [retro]
- R8. Need to distinguish when to use lexicog Entry vs. Lexical Entry (this will be resolved with the Entry superclass solution which is being tentatively proposed)
- R9. Need to include definitions of dictionary senses (using SKOS:Concept as previously recommended, assumes every dictionary sense is a SKOS:Concept, which may not be appropriate, see R7) [retro]
- R10. Need to include see also entries which only point to other entries as well as entries which give a single form (in the case of e.g., suppletive forms, common in a language with strong verbs such as Old English, e.g., _writan_ vs _wrat_) or spelling variations [retro]
- R11. Need to include exact wording or representation of Part of Speech or grammatical information [retro]    
 
[^1]:<https://www.w3.org/community/ontolex/wiki/Lexicography>
[^2]:<https://en.wiktionary.org/wiki/game>
[^3]:<https://en.wiktionary.org/wiki/fanny>
[^4]:Of course not all languages use alphabets.
[^5]:Pardoning the pun. 
[^6]:See  also https://en.wiktionary.org/wiki/regretter
