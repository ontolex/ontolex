9 Sept 2025 14:00 | Ontolex v2 open discussion at LDK’25 
========================================================

Attendees (Ontolex members and guests): 

Jorge Gracia, 
Katerina Gkirtzou,
David Lindemann,
Max Ionov,
Marco Passarotti,
Theodorus Fransen,
Patricia Martín-Chozas,
Elena Montiel-Ponsoda,
Alik Kirillovich,
John McCrae,
Philipp Cimiano,
Fahad Khan,
Armando Stellato,
Gilles Sérasset,
Matteo Pellegrini,
Francesco Mambrini,
Frank Abromeit,
Arbresha Meha,
Slavko Zitnik,
Marieke van Erp,
Lorenzo Augello

Relevant links: 

- Ontolex model github https://github.com/ontolex/ontolex 
- Ontolex minutes and requirements https://github.com/ontolex/ontolex/tree/master/notes 
- Ontolex issues https://github.com/ontolex/ontolex/issues 

## Agenda
1. Review merged requirements
2. Review and discuss open issues
3. Practical issues:
- One document (report) with all the modules or one document per module? 
- Full/partial/none integration between core and lexicog module?

## Minutes

1. Review merged requirements

See [here](https://github.com/ontolex/ontolex/blob/master/notes/requirements_all.md) for the merged requirements

2. Review and discuss open issues

See [here](https://github.com/ontolex/ontolex/issues) for open issues 


3. Practical issues:
One document (report) with all the modules or one document per module? The ontologies will be different files anyway.
In the first case, future modules will need update of the unified document (and increment the version)

- Fahad> TEI works very well as a single document
- Philipp> Technically it is okay to have a single document, but can be overwhelming for the new users. Can we create separate documents for different profiles (e.g. those who want to represent terminology)? Possibly represent everything in a single document but separate documents for their interplay for adopters (i.e. “cookbooks”)
- Gilles> potential problems with versions if separate documents
- Armando> Mixed approach could be good. Problem with the single document: if we want to update just one module, we need to update the whole document.
→ Single document, separate sections, pointers to “plugins” that in the future could be promoted to the main document
- Jorge> We can continue as we were doing: Develop new modules separately to have their own space
- John> Different documents will make it more difficult for people to find it. Many established models have one big document (TEI, DMLex)
- Fahad> TEI Lex-0 is a separate document (while it is being developed). One problem with versioning and updating is that we don’t have a designated person to keep track and update
- Jorge> That probably should not be a problem since while the modules are being developed, the ones who are developing it are updating everything.
- Katerina> Would it not be better to have a big index page pointing to all modules and versions? With some additional info and information on modules and versions.
- Elena> There would be unity if there is only one document. But it is important to keep the modularised architecture (even if it is described in one place) so that people can use only what they need.

**ISSUE** to vote: separate developments of new modules, later integrated into a unique specification after CG approval 
**DECISION** no objection, approved

**PENDING** to discuss authorship
- Philipp> short list of authors (maybe ontolex CG) and then the detailed list in acknowledgment (separate per modules)
- Fahad> potential problem with visibility of authors, people might be reluctant to contribute

**ACTION** check other W3C documents to see how they deal with this: full list of authors or in acknowledgments.


Full/partial/none integration between core and lexicog module? 
See issue #62

