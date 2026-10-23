# OntoLex Meeting 16/10/26

Present: John, Christian, Jorge, Max, Alik, Philipp, Patricia, Elena, Edmond

## #66 
- Agree to merge PR

## #47
Christian: Link forms to lexicographic entries?
Max: Don't allow this, it's cleaner
Alik/Christian: Better this way and allows backwards compatibility
Max: Less frequent solution

Name: 
- `EntryGroup` (Christian, Elena, Philipp? in favour)
- `LexicographicEntry` (Max, Alik, Jorge, Matteo in favour)

Christian: Suggests just using LexicographicComponent
Jorge: LC is not an "entry" in a dictionary

Decisions: Use `LexicographicEntry` with modelling as in PR (#77)

[AP: John] implement and merge

## #50:

All agree to use container membership properties

Add  documentation on senses (+1: Jorge, Christian)

[AP: John] implement and merge

## #54:

[AP] John to query with Fahad

## #56:

[AP] John to post to list

## #58:

Christian: Isn't this just from LexInfo

[AP: John] Associate issue in LexInfo for linking axioms

Agree to merge!

## #61:

Inflected from as a new other form

Alik: Can an inflected form not be a canonical form?

[AP: John] Make `inflectedForm` a direct subproperty of `lexicalForm` (not `otherForm`) and merge

Christian: Use case for this? Max: Old English

## #63:

Range of `describes` (see also PR #77)
- Option 1: Lexical Entry or Lexical Sense
- Option 2: Lexical Entry or Lexical Sense or Lexical Concept or Form
- Option 3: No range
- Option 4: Observable
- Option 5: Describable

[AP: John] to bring to mailing list
