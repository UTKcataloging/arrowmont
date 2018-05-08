# Arrow Articles Schema Analysis

## About

Below is a Schema Analysis of the Arrow Articles

## Analysis

| key                                                                   | types                    | occurrences | percents |
| --------------------------------------------------------------------- | ------------------------ | ----------- | -------- |
| _id                                                                   | ObjectId                 |         320 | 100.0000 |
| metadata                                                              | Object                   |         320 | 100.0000 |
| metadata.mods                                                         | Object                   |         320 | 100.0000 |
| metadata.mods.@xmlns                                                  | String                   |         320 | 100.0000 |
| metadata.mods.@xmlns:xlink                                            | String                   |         320 | 100.0000 |
| metadata.mods.@xmlns:xsi                                              | String                   |         320 | 100.0000 |
| metadata.mods.@xsi:schemaLocation                                     | String                   |         320 | 100.0000 |
| metadata.mods.accessCondition                                         | Object                   |         320 | 100.0000 |
| metadata.mods.accessCondition.#text                                   | String                   |         320 | 100.0000 |
| metadata.mods.accessCondition.@type                                   | String                   |         320 | 100.0000 |
| metadata.mods.genre                                                   | String                   |         320 | 100.0000 |
| metadata.mods.identifier                                              | Array                    |         320 | 100.0000 |
| metadata.mods.identifier.XX.#text                                     | String                   |         320 | 100.0000 |
| metadata.mods.identifier.XX.@type                                     | String                   |         320 | 100.0000 |
| metadata.mods.language                                                | Object                   |         320 | 100.0000 |
| metadata.mods.language.languageTerm                                   | Object                   |         320 | 100.0000 |
| metadata.mods.language.languageTerm.#text                             | String                   |         320 | 100.0000 |
| metadata.mods.language.languageTerm.@authority                        | String                   |         320 | 100.0000 |
| metadata.mods.language.languageTerm.@type                             | String                   |         320 | 100.0000 |
| metadata.mods.location                                                | Object                   |         320 | 100.0000 |
| metadata.mods.location.physicalLocation                               | Array                    |         320 | 100.0000 |
| metadata.mods.location.physicalLocation.XX.#text                      | String                   |         320 | 100.0000 |
| metadata.mods.location.physicalLocation.XX.@displayLabel              | String                   |         320 | 100.0000 |
| metadata.mods.location.url                                            | String                   |         320 | 100.0000 |
| metadata.mods.note                                                    | Object (297),Array (23)  |         320 | 100.0000 |
| metadata.mods.originInfo                                              | Object                   |         320 | 100.0000 |
| metadata.mods.originInfo.dateIssued                                   | Object                   |         320 | 100.0000 |
| metadata.mods.originInfo.dateIssued.#text                             | String                   |         320 | 100.0000 |
| metadata.mods.originInfo.dateIssued.@keyDate                          | String                   |         320 | 100.0000 |
| metadata.mods.originInfo.publisher                                    | String                   |         320 | 100.0000 |
| metadata.mods.physicalDescription                                     | Object                   |         320 | 100.0000 |
| metadata.mods.physicalDescription.extent                              | String                   |         320 | 100.0000 |
| metadata.mods.physicalDescription.internetMediaType                   | String                   |         320 | 100.0000 |
| metadata.mods.recordInfo                                              | Object                   |         320 | 100.0000 |
| metadata.mods.recordInfo.languageOfCataloging                         | Object                   |         320 | 100.0000 |
| metadata.mods.recordInfo.languageOfCataloging.languageTerm            | Object                   |         320 | 100.0000 |
| metadata.mods.recordInfo.languageOfCataloging.languageTerm.#text      | String                   |         320 | 100.0000 |
| metadata.mods.recordInfo.languageOfCataloging.languageTerm.@authority | String                   |         320 | 100.0000 |
| metadata.mods.recordInfo.languageOfCataloging.languageTerm.@type      | String                   |         320 | 100.0000 |
| metadata.mods.recordInfo.recordContentSource                          | String                   |         320 | 100.0000 |
| metadata.mods.relatedItem                                             | Array                    |         320 | 100.0000 |
| metadata.mods.relatedItem.XX.@displayLabel                            | String                   |         320 | 100.0000 |
| metadata.mods.relatedItem.XX.@type                                    | String                   |         320 | 100.0000 |
| metadata.mods.relatedItem.XX.identifier                               | Object                   |         320 | 100.0000 |
| metadata.mods.relatedItem.XX.identifier.#text                         | String                   |         320 | 100.0000 |
| metadata.mods.relatedItem.XX.identifier.@type                         | String                   |         320 | 100.0000 |
| metadata.mods.relatedItem.XX.part                                     | Object                   |         320 | 100.0000 |
| metadata.mods.relatedItem.XX.part.extent                              | Object                   |         320 | 100.0000 |
| metadata.mods.relatedItem.XX.part.extent.@unit                        | String                   |         320 | 100.0000 |
| metadata.mods.relatedItem.XX.part.extent.list                         | String                   |         320 | 100.0000 |
| metadata.mods.relatedItem.XX.titleInfo                                | Object                   |         320 | 100.0000 |
| metadata.mods.relatedItem.XX.titleInfo.partNumber                     | String                   |         320 | 100.0000 |
| metadata.mods.relatedItem.XX.titleInfo.title                          | String                   |         320 | 100.0000 |
| metadata.mods.subject                                                 | Array                    |         320 | 100.0000 |
| metadata.mods.subject.XX.@authority                                   | String                   |         320 | 100.0000 |
| metadata.mods.subject.XX.temporal                                     | String                   |         320 | 100.0000 |
| metadata.mods.subject.XX.topic                                        | String                   |         320 | 100.0000 |
| metadata.mods.titleInfo                                               | Object                   |         320 | 100.0000 |
| metadata.mods.titleInfo.title                                         | String                   |         320 | 100.0000 |
| metadata.mods.typeOfResource                                          | String                   |         320 | 100.0000 |
| record_id                                                             | Object                   |         320 | 100.0000 |
| record_id.#text                                                       | String                   |         320 | 100.0000 |
| record_id.@type                                                       | String                   |         320 | 100.0000 |
| metadata.mods.note.#text                                              | String                   |         297 |  92.8125 |
| metadata.mods.note.@displayLabel                                      | String                   |         297 |  92.8125 |
| metadata.mods.name                                                    | Object (128),Array (147) |         275 |  85.9375 |
| metadata.mods.tableOfContents                                         | Object                   |         220 |  68.7500 |
| metadata.mods.tableOfContents.#text                                   | String                   |         220 |  68.7500 |
| metadata.mods.tableOfContents.@displayLabel                           | String                   |         220 |  68.7500 |
| metadata.mods.originInfo.dateIssued.@encoding                         | String                   |         213 |  66.5625 |
| metadata.mods.name.XX.namePart                                        | Array                    |         147 |  45.9375 |
| metadata.mods.name.XX.namePart.XX.#text                               | String                   |         147 |  45.9375 |
| metadata.mods.name.XX.namePart.XX.@type                               | String                   |         147 |  45.9375 |
| metadata.mods.name.XX.role                                            | Object                   |         147 |  45.9375 |
| metadata.mods.name.XX.role.roleTerm                                   | Object                   |         147 |  45.9375 |
| metadata.mods.name.XX.role.roleTerm.#text                             | String                   |         147 |  45.9375 |
| metadata.mods.name.XX.role.roleTerm.@authority                        | String                   |         147 |  45.9375 |
| metadata.mods.name.namePart                                           | Array                    |         128 |  40.0000 |
| metadata.mods.name.namePart.XX.#text                                  | String                   |         128 |  40.0000 |
| metadata.mods.name.namePart.XX.@type                                  | String                   |         128 |  40.0000 |
| metadata.mods.name.role                                               | Object                   |         128 |  40.0000 |
| metadata.mods.name.role.roleTerm                                      | Object                   |         128 |  40.0000 |
| metadata.mods.name.role.roleTerm.#text                                | String                   |         128 |  40.0000 |
| metadata.mods.name.role.roleTerm.@authority                           | String                   |         128 |  40.0000 |
| metadata.mods.originInfo.dateIssued.@qualifier                        | String                   |         107 |  33.4375 |
| metadata.mods.note.XX.#text                                           | String                   |          23 |   7.1875 |
| metadata.mods.note.XX.@displayLabel                                   | String                   |          23 |   7.1875 |

