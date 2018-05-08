# Arrowmont Simple Images Schema Analysis

## About

This contatins information about the schema analysis for Simple Images.

## Schema Analysis

| key                                                                   | types                  | occurrences | percents             |
| --------------------------------------------------------------------- | ---------------------- | ----------- | -------------------- |
| _id                                                                   | ObjectId               |         460 | 100.0000000000000000 |
| metadata                                                              | Object                 |         460 | 100.0000000000000000 |
| metadata.mods                                                         | Object                 |         460 | 100.0000000000000000 |
| metadata.mods.@xmlns                                                  | String                 |         460 | 100.0000000000000000 |
| metadata.mods.@xmlns:xlink                                            | String                 |         460 | 100.0000000000000000 |
| metadata.mods.@xmlns:xsi                                              | String                 |         460 | 100.0000000000000000 |
| metadata.mods.@xsi:schemaLocation                                     | String                 |         460 | 100.0000000000000000 |
| metadata.mods.accessCondition                                         | Object                 |         460 | 100.0000000000000000 |
| metadata.mods.accessCondition.#text                                   | String                 |         460 | 100.0000000000000000 |
| metadata.mods.accessCondition.@type                                   | String                 |         460 | 100.0000000000000000 |
| metadata.mods.genre                                                   | String                 |         460 | 100.0000000000000000 |
| metadata.mods.identifier                                              | Array                  |         460 | 100.0000000000000000 |
| metadata.mods.identifier.XX.#text                                     | String                 |         460 | 100.0000000000000000 |
| metadata.mods.identifier.XX.@type                                     | String                 |         460 | 100.0000000000000000 |
| metadata.mods.language                                                | Object                 |         460 | 100.0000000000000000 |
| metadata.mods.language.languageTerm                                   | Object                 |         460 | 100.0000000000000000 |
| metadata.mods.language.languageTerm.#text                             | String                 |         460 | 100.0000000000000000 |
| metadata.mods.language.languageTerm.@authority                        | String                 |         460 | 100.0000000000000000 |
| metadata.mods.language.languageTerm.@type                             | String                 |         460 | 100.0000000000000000 |
| metadata.mods.location                                                | Object                 |         460 | 100.0000000000000000 |
| metadata.mods.location.physicalLocation                               | Array                  |         460 | 100.0000000000000000 |
| metadata.mods.location.physicalLocation.XX.#text                      | String                 |         460 | 100.0000000000000000 |
| metadata.mods.location.physicalLocation.XX.@displayLabel              | String                 |         460 | 100.0000000000000000 |
| metadata.mods.location.url                                            | String                 |         460 | 100.0000000000000000 |
| metadata.mods.name                                                    | Object                 |         460 | 100.0000000000000000 |
| metadata.mods.name.namePart                                           | String                 |         460 | 100.0000000000000000 |
| metadata.mods.name.role                                               | Object                 |         460 | 100.0000000000000000 |
| metadata.mods.name.role.roleTerm                                      | String                 |         460 | 100.0000000000000000 |
| metadata.mods.note                                                    | Object                 |         460 | 100.0000000000000000 |
| metadata.mods.note.#text                                              | String                 |         460 | 100.0000000000000000 |
| metadata.mods.note.@displayLabel                                      | String                 |         460 | 100.0000000000000000 |
| metadata.mods.originInfo                                              | Object (458),null (2)  |         460 | 100.0000000000000000 |
| metadata.mods.physicalDescription                                     | Object                 |         460 | 100.0000000000000000 |
| metadata.mods.physicalDescription.internetMediaType                   | String                 |         460 | 100.0000000000000000 |
| metadata.mods.recordInfo                                              | Object                 |         460 | 100.0000000000000000 |
| metadata.mods.recordInfo.languageOfCataloging                         | Object                 |         460 | 100.0000000000000000 |
| metadata.mods.recordInfo.languageOfCataloging.languageTerm            | Object                 |         460 | 100.0000000000000000 |
| metadata.mods.recordInfo.languageOfCataloging.languageTerm.#text      | String                 |         460 | 100.0000000000000000 |
| metadata.mods.recordInfo.languageOfCataloging.languageTerm.@authority | String                 |         460 | 100.0000000000000000 |
| metadata.mods.recordInfo.languageOfCataloging.languageTerm.@type      | String                 |         460 | 100.0000000000000000 |
| metadata.mods.recordInfo.recordContentSource                          | String                 |         460 | 100.0000000000000000 |
| metadata.mods.relatedItem                                             | Object (454),Array (6) |         460 | 100.0000000000000000 |
| metadata.mods.subject                                                 | Array                  |         460 | 100.0000000000000000 |
| metadata.mods.subject.XX.@authority                                   | String                 |         460 | 100.0000000000000000 |
| metadata.mods.subject.XX.topic                                        | String                 |         460 | 100.0000000000000000 |
| metadata.mods.titleInfo                                               | Object                 |         460 | 100.0000000000000000 |
| metadata.mods.titleInfo.title                                         | String                 |         460 | 100.0000000000000000 |
| metadata.mods.typeOfResource                                          | String                 |         460 | 100.0000000000000000 |
| record_id                                                             | Object                 |         460 | 100.0000000000000000 |
| record_id.#text                                                       | String                 |         460 | 100.0000000000000000 |
| record_id.@type                                                       | String                 |         460 | 100.0000000000000000 |
| metadata.mods.originInfo.dateCreated                                  | Object                 |         458 |  99.5652173913043441 |
| metadata.mods.originInfo.dateCreated.#text                            | String                 |         458 |  99.5652173913043441 |
| metadata.mods.originInfo.dateCreated.@encoding                        | String                 |         458 |  99.5652173913043441 |
| metadata.mods.originInfo.dateCreated.@keyDate                         | String                 |         458 |  99.5652173913043441 |
| metadata.mods.originInfo.dateCreated.@point                           | String                 |         458 |  99.5652173913043441 |
| metadata.mods.relatedItem.@displayLabel                               | String                 |         454 |  98.6956521739130466 |
| metadata.mods.relatedItem.@type                                       | String                 |         454 |  98.6956521739130466 |
| metadata.mods.relatedItem.identifier                                  | Object                 |         454 |  98.6956521739130466 |
| metadata.mods.relatedItem.identifier.#text                            | String                 |         454 |  98.6956521739130466 |
| metadata.mods.relatedItem.identifier.@type                            | String                 |         454 |  98.6956521739130466 |
| metadata.mods.relatedItem.titleInfo                                   | Object                 |         454 |  98.6956521739130466 |
| metadata.mods.relatedItem.titleInfo.title                             | String                 |         454 |  98.6956521739130466 |
| metadata.mods.subject.XX.geographic                                   | String                 |         393 |  85.4347826086956559 |
| metadata.mods.abstract                                                | String                 |         348 |  75.6521739130434838 |
| metadata.mods.subject.XX.name                                         | Object                 |         221 |  48.0434782608695627 |
| metadata.mods.subject.XX.name.namePart                                | String                 |         221 |  48.0434782608695627 |
| metadata.mods.relatedItem.XX.@displayLabel                            | String                 |           6 |   1.3043478260869565 |
| metadata.mods.relatedItem.XX.@type                                    | String                 |           6 |   1.3043478260869565 |
| metadata.mods.relatedItem.XX.identifier                               | Object                 |           6 |   1.3043478260869565 |
| metadata.mods.relatedItem.XX.identifier.#text                         | String                 |           6 |   1.3043478260869565 |
| metadata.mods.relatedItem.XX.identifier.@type                         | String                 |           6 |   1.3043478260869565 |
| metadata.mods.relatedItem.XX.titleInfo                                | Object                 |           6 |   1.3043478260869565 |
| metadata.mods.relatedItem.XX.titleInfo.title                          | String                 |           6 |   1.3043478260869565 |

