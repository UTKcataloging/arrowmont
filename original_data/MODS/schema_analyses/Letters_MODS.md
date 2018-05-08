# Arrowmont Letters Schema Analysis

## About

This includes a schema analysis of Arrowmont letters.

## Schema Analysis

| key                                                                   | types    | occurrences | percents |
| --------------------------------------------------------------------- | -------- | ----------- | -------- |
| _id                                                                   | ObjectId |          66 |    100.0 |
| metadata                                                              | Object   |          66 |    100.0 |
| metadata.mods                                                         | Object   |          66 |    100.0 |
| metadata.mods.@xmlns                                                  | String   |          66 |    100.0 |
| metadata.mods.@xmlns:xlink                                            | String   |          66 |    100.0 |
| metadata.mods.@xmlns:xsi                                              | String   |          66 |    100.0 |
| metadata.mods.@xsi:schemaLocation                                     | String   |          66 |    100.0 |
| metadata.mods.abstract                                                | String   |          66 |    100.0 |
| metadata.mods.accessCondition                                         | Object   |          66 |    100.0 |
| metadata.mods.accessCondition.#text                                   | String   |          66 |    100.0 |
| metadata.mods.accessCondition.@type                                   | String   |          66 |    100.0 |
| metadata.mods.genre                                                   | Object   |          66 |    100.0 |
| metadata.mods.genre.#text                                             | String   |          66 |    100.0 |
| metadata.mods.genre.@authority                                        | String   |          66 |    100.0 |
| metadata.mods.identifier                                              | Array    |          66 |    100.0 |
| metadata.mods.identifier.XX.#text                                     | String   |          66 |    100.0 |
| metadata.mods.identifier.XX.@type                                     | String   |          66 |    100.0 |
| metadata.mods.language                                                | Object   |          66 |    100.0 |
| metadata.mods.language.languageTerm                                   | Object   |          66 |    100.0 |
| metadata.mods.language.languageTerm.#text                             | String   |          66 |    100.0 |
| metadata.mods.language.languageTerm.@authority                        | String   |          66 |    100.0 |
| metadata.mods.language.languageTerm.@type                             | String   |          66 |    100.0 |
| metadata.mods.location                                                | Object   |          66 |    100.0 |
| metadata.mods.location.physicalLocation                               | Array    |          66 |    100.0 |
| metadata.mods.location.physicalLocation.XX.#text                      | String   |          66 |    100.0 |
| metadata.mods.location.physicalLocation.XX.@displayLabel              | String   |          66 |    100.0 |
| metadata.mods.location.url                                            | String   |          66 |    100.0 |
| metadata.mods.name                                                    | Object   |          66 |    100.0 |
| metadata.mods.name.namePart                                           | String   |          66 |    100.0 |
| metadata.mods.name.role                                               | Object   |          66 |    100.0 |
| metadata.mods.name.role.roleTerm                                      | Object   |          66 |    100.0 |
| metadata.mods.name.role.roleTerm.#text                                | String   |          66 |    100.0 |
| metadata.mods.name.role.roleTerm.@authority                           | String   |          66 |    100.0 |
| metadata.mods.note                                                    | Object   |          66 |    100.0 |
| metadata.mods.note.#text                                              | String   |          66 |    100.0 |
| metadata.mods.note.@displayLabel                                      | String   |          66 |    100.0 |
| metadata.mods.originInfo                                              | Object   |          66 |    100.0 |
| metadata.mods.originInfo.dateCreated                                  | Object   |          66 |    100.0 |
| metadata.mods.originInfo.dateCreated.#text                            | String   |          66 |    100.0 |
| metadata.mods.originInfo.dateCreated.@encoding                        | String   |          66 |    100.0 |
| metadata.mods.originInfo.dateCreated.@keyDate                         | String   |          66 |    100.0 |
| metadata.mods.originInfo.dateCreated.@qualifier                       | String   |          66 |    100.0 |
| metadata.mods.originInfo.publisher                                    | String   |          66 |    100.0 |
| metadata.mods.physicalDescription                                     | Object   |          66 |    100.0 |
| metadata.mods.physicalDescription.extent                              | String   |          66 |    100.0 |
| metadata.mods.physicalDescription.internetMediaType                   | String   |          66 |    100.0 |
| metadata.mods.recordInfo                                              | Object   |          66 |    100.0 |
| metadata.mods.recordInfo.languageOfCataloging                         | Object   |          66 |    100.0 |
| metadata.mods.recordInfo.languageOfCataloging.languageTerm            | Object   |          66 |    100.0 |
| metadata.mods.recordInfo.languageOfCataloging.languageTerm.#text      | String   |          66 |    100.0 |
| metadata.mods.recordInfo.languageOfCataloging.languageTerm.@authority | String   |          66 |    100.0 |
| metadata.mods.recordInfo.languageOfCataloging.languageTerm.@type      | String   |          66 |    100.0 |
| metadata.mods.recordInfo.recordContentSource                          | String   |          66 |    100.0 |
| metadata.mods.relatedItem                                             | Object   |          66 |    100.0 |
| metadata.mods.relatedItem.@displayLabel                               | String   |          66 |    100.0 |
| metadata.mods.relatedItem.@type                                       | String   |          66 |    100.0 |
| metadata.mods.relatedItem.identifier                                  | Object   |          66 |    100.0 |
| metadata.mods.relatedItem.identifier.#text                            | String   |          66 |    100.0 |
| metadata.mods.relatedItem.identifier.@type                            | String   |          66 |    100.0 |
| metadata.mods.relatedItem.titleInfo                                   | Object   |          66 |    100.0 |
| metadata.mods.relatedItem.titleInfo.title                             | String   |          66 |    100.0 |
| metadata.mods.subject                                                 | Array    |          66 |    100.0 |
| metadata.mods.subject.XX.@authority                                   | String   |          66 |    100.0 |
| metadata.mods.subject.XX.topic                                        | String   |          66 |    100.0 |
| metadata.mods.titleInfo                                               | Object   |          66 |    100.0 |
| metadata.mods.titleInfo.title                                         | String   |          66 |    100.0 |
| metadata.mods.typeOfResource                                          | String   |          66 |    100.0 |
| record_id                                                             | Object   |          66 |    100.0 |
| record_id.#text                                                       | String   |          66 |    100.0 |
| record_id.@type                                                       | String   |          66 |    100.0 |

