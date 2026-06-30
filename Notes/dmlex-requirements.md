# Requirements on OntoLex 2.0 from DMLex

In order to improve the interoperability of OntoLex with the DMLex model and its modules, we should consider making improvements to the core that better align with this model

## DMLex Core

* `partOfSpeech`: OntoLex does not have a core part-of-speech property unlike DMLex. This may be useful also for defining lexical entries in our model
* `inflectedForm`: OntoLex has `otherForm` that is similar but seems slightly broader in interpretation
* `example`: We probably need a property to give examples by entry and sense as well

## DMLex Crosslingual Module

This extends DMLex to represent bilingual and multilingual dictionaries

* `headwordTranslation`, `headwordExplanation`: These give lemmas and glosses for an entry in another language. This differs from OntoLex modelling which would instead link entries/forms in two different lexicons.
* `exampleTranslation`: If examples are introduced, we may want to give translations (especially for historical languages)

## DMLex Controlled Vocabulary Module

This allows the DMLex standard to extend with new terms such as part-of-speech. This is already well-captured by our RDF/OWL modelling so there is no need to import anything.

## DMLex Linking Module

This is well captured by the _vartrans_ module and no changes are necessary

## DMLex Annotation Module

This allows inline markup of entries in order to mark placeholders, headwords and collocates.

```xml
<text>The coroner <collocateMarker lemma="perform">performed</collocateMarker> an
      <headwordMarker>autopsy</headwordMarker>.</text>
```

This would be quite tricky to support in RDF, as there is no easy way to do inline markup. Perhaps, this use case could be consider in the context of the _FrAC_ module? 

## DMLex Etymology Module

OntoLex has no support for etymology and this work will be done in a new module, so this will not affect the core.
