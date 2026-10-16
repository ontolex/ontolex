# OntoLex Core Meeting Minutes - 24th Jan 2025

Requirements documents
* Terminology based on https://www.w3.org/community/ontolex/wiki/Terminology [PMC to add to Wiki]
* Lexicography (pending)
* DMLex interoperability https://github.com/ontolex/ontolex/blob/master/notes/dmlex-requirements.md

Discussion of Requirements
* DMLex
  * Add part of speech property? Move `lexinfo:partOfSpeech` to Core
  * Is an inflected form the same as an other form
  * Do we need headword translations and headword explanations
    * Current modelling is probably sufficient if not easy
    * This would probably affect the VarTrans module rather than the core
  * Example Translation - potentially useful for some dictionaries
  * Inline markup
    * Probably already captured by FrAC but requires more anlysis
* Terminology
  * Definitions - certainly useful
  * Notes - also useful
  * Usage Information - useful, but consider if this can be merged into a single modelling
  * Sources
    * Maybe already captured by PROV-O and FrAC
    * Distinction between attestation and provenance may be important
  * Term Reliability
    * Need more examples
  * Terminological concept - agreed to remove requirement in previous meeting
  * I7 no longer a requirement (dependent on terminological concept)
* Other
  * Variant forms that are not inflectional variants
    * Add to lexicographic requirements
   
Next meeting end of Feb to close requirements phase.
