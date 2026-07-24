# OntoLex Meeting - 22nd July 2026

Present: John, Ilan, Matteo, Alik, Jorge, Eleonora, Patricia, Fahad, Max, Elena

- Issue #59 - Agreed to transfer to LexInfo [AP: John to implement]
- Issue #51 - Merge issue and create new issue based on Fahad's comment (https://github.com/ontolex/ontolex/issues/51#issuecomment-4868347331) [AP: John]
- Issue #48 - Ilan: Do we want to treat monosemous senses differently? John: No due to open-world assumption
  - Matteo: Also allow on forms?
  - [AP: John] Decision to allow usage examples on forms, lexical senses and entries, then merge
- Issue #50 - [AP: John] revise to use `rdf:_n`
  - Document how deep nesting can be achieved here
- Issue #60/#55 - [AP: John] Document `partOfSpeechLabel` as clearly secondary and merge
- Issue #56 - Matteo: also allow usage on forms?
  - [AP: John] update PR to reflect updated domain
  - Discussion on allowing usages on lexical concepts. Group decided against this
- Issue #58 - Group notes that confidence is a subjective and domain-specific property; spec reflects this
  - [AP: John] consider if the domain should be wider and update PR
  - Discussed value of including confidence property in core; decided in favour
- Issue #47 - Will lexicographic component from lexicog be imported? Not under current spec
  - John: lexicog will need to be revised after the 1.1 update
  - [AP: Matteo] Add comment or new issue describing use case
 
