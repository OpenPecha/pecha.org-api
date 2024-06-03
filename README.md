
# API for Pecha.org 

## Overview
The Pecha.org API is a tool designed to facilitate the uploading and management of textual and reference data. This API supports a structured approach to managing texts, translations, web links, commentaries, references, and additional notes, ensuring that the data is well-organized and easily accessible.

### Key Features:
1. **Texts/Articles**: Allows uploading and categorizing complex or simple texts, including multiple levels of content and language-specific details.
2. **Translations**: Supports adding translations of texts, ensuring multilingual accessibility.
3. **Web Links**: Facilitates the inclusion of web links that reference specific sections and sentences within texts.
4. **Commentaries and References**: Enables the addition of commentaries and references that provide deeper insights and connections between texts.
5. **Sheets for Additional Notes**: Allows for the addition of extra notes related to specific sections of the texts.

### Supported File Types:
- **Texts/Articles**: JSON files containing the primary texts and their hierarchical structure.
- **Translations**: JSON files with translations of the texts.
- **Web Links**: JSON files linking to external resources related to specific text sections.
- **Commentaries and References**: JSON files with commentary and reference details.
- **Sheets**: JSON files for additional notes and annotations.

### Usage Workflow:
1. **Prepare JSON Files**: Ensure that the data files follow the specific formats required by the API.
2. **Organize Files**: Place book json data files in /jsondata/texts and links data files in /jsondata/refs.
3. **Execute Scripts**: Run the commentaryToJson.py script to create links, followed by executing pechaAPI.py to upload the data to Pecha.org.

## Useful links
- 


## File Types 

### 1) Texts/Article

Put your JSON files (file name is arbitrary) into `/jsondata/texts` and execute pechaAPI.py

**The sample/example file description for complext text**:
```
{
    "source": {
        "categories": [
            {
                "name": "category1",
                "enDesc": "category1 long description",
                "enShortDesc": "category1 short description"
            },
            {
                "name": "category2",
                "enDesc": "category2 long description",
                "enShortDesc": "category2 short description"
            },
            {
                "name": "book title",
                "enDesc": "book title long description",
                "enShortDesc": "book title short description"
            }
        ],
        "books": [
            {
                "title": "book title",
                "language": "en|he(ie. tibetan)|fr etc.",
                "versionSource": "",
                "content": {
                    "book title": {
                        "level1": {
                            "data": [
                                [
                                    "section 1, sentence 1 (corresponds to the position in the "target>book>level1" data)",
                                    "section 1, sentence 2",
                                    "section 1, sentence 3"
                                ],
                                [
                                    "section 2, sentence 1",
                                    "section 2, sentence 2",
                                ]
                            ]
                        },
                        "level2": {
                            "The actual benefits of listening to and reading the words of the Great Perfection as they are intended applied and recited by a yogin who has attained stability on the path of the Great Perfection": {
                                "data": [ 
                                    "section 1, sentence 1 (corresponds to the position in the "target>book>level2" data)",
                                    "section 1, sentence 2",
                                    "section 1, sentence 3",
                                ]
                            },
                            "The Key Points of Time": {
                                "data": [
                                    "section 1, sentence 1 (corresponds to the position in the "target>book>level1" data)",
                                    "section 1, sentence 2",
                                ]
                            },
                            "data": [.
                                "section 1, sentence 1 (corresponds to the position in the "target>book>data"data)",
                                        "section 1, sentence 2",
                                        "section 1, sentence 3",
                            ]
                        },
                        "data": [
                            "section 1, sentence 1 (corresponds to the position in the "target>book>data"data)",
                                    "section 1, sentence 2",
                        ]
                    }
                }
            },
            {
                # version for above book
                "title": "book title",
                "language": "en|he(ie. tibetan)|fr etc.",
                "versionSource": "",
                "content": {
                    "same structure as above book"
                }
            }
        ]
    },
    # for tibetan
    "target": {
        "categories": [
            {
                "name": "category1 in tibetan (bo)",
                "enDesc": "category1 long description in tibetan (bo)",
                "enShortDesc": "category1 short description in tibetan (bo)"
            },
            {
                "name": "category2 in tibetan (bo)",
                "enDesc": "category2 long description in tibetan (bo)",
                "enShortDesc": "category2 short description in tibetan (bo)"
            },
            {
                "name": "book title in tibetan (bo)",
                "enDesc": "book title long description in tibetan (bo)",
                "enShortDesc": "book title short description in tibetan (bo)"
            }
        ],
        "books": [
            {
                "title": "book title in tibetan (bo)",
                "language": "bo",
                "versionSource": "",
                "content": {
                    "book title in tibetan (bo)": {
                        "level1 book title in tibetan (bo)": {
                            "data": [
                                [
                                    "section 1, sentence 1 (corresponds to the position in the "target>book>level1" data)",
                                    "section 1, sentence 2",
                                    "section 1, sentence 3",
                                    "section 1, sentence 4",
                                    "section 1, sentence 5"
                                ],
                                [
                                    "section 2, sentence 1",
                                    "section 2, sentence 2",
                                    "section 2, sentence 3",
                                    "section 2, sentence 4",
                                    "section 2, sentence 5"
                                ]
                            ]
                        },
                        "སྨོན་ལམ་ཀློག་པ་དང་ཐོས་པའི་ཕན་ཡོན་བསྟན་པ།": {
                            "རྫོགས་ཆེན་གྱི་ལམ་ལ་བརྟན་པ་ཐོབ་པའི་རྣལ་འབྱོར་པས་བསམ་པས་ཇི་ལྟར་སྨོན་པ་དང་སྦྱོར་བ་ཚིག་ཉན་ཀློག་བྱས་པའི་ཕན་ཡོན་དངོས།": {
                                "data": [ 
                                    "section 1, sentence 1 (corresponds to the position in the "target>book>level2" data)",
                                    "section 1, sentence 2",
                                    "section 1, sentence 3",
                                    "section 1, sentence 4",
                                    "section 1, sentence 5"
                                ]
                            },
                            "དུས་གནད་བསྟན་པ།": {
                                "data": [ 
                                    "section 1, sentence 1 (corresponds to the position in the "target>book>level2" data)",
                                    "section 1, sentence 2",
                                    "section 1, sentence 3",
                                    "section 1, sentence 4",
                                    "section 1, sentence 5"
                                ]
                            },
                            "data": [ 
                                    "section 1, sentence 1 (corresponds to the position in the "target>book>level2" data)",
                                    "section 1, sentence 2",
                                    "section 1, sentence 3",
                                    "section 1, sentence 4",
                                    "section 1, sentence 5"
                                ]
                        },
                        "data": [ 
                                    "section 1, sentence 1 (corresponds to the position in the "target>book>level2" data)",
                                    "section 1, sentence 2",
                                    "section 1, sentence 3",
                                    "section 1, sentence 4",
                                    "section 1, sentence 5"
                                ]
                    }
                }
            }
        ]
    }
}

```
A sample file for simple text (ie. booking having only one level): 
```
{
    "source": {
        "categories": [
            {
                "name": "Liturgy",
                "enDesc": "",
                "enShortDesc": "Prayers and rituals"
            },
            {
                "name": "Prayers",
                "enDesc": "",
                "enShortDesc": ""
            },
            {
                "name": "Prayer of Kuntuzangpo",
                "enDesc": "",
                "enShortDesc": "The Powerful Aspiration"
            }
        ],
        "books": [
            {
                "title": "Prayer of Kuntuzangpo",
                "language": "en",
                "versionSource": " ",
                "content": [
                    [ 
                        "section 1, sentence 1 (corresponds to the position in the "target>book>" content)",
                        "section 1, sentence 2",
                        "section 1, sentence 3",
                        "section 1, sentence 4",
                        "section 1, sentence 5"
                    ]
                ],
                "direction": "ltr"
            }
        ]
    },
    "target": {
        "categories": [
            {
                "name": "ཆོ་ག",
                "heDesc": "",
                "heShortDesc": "ཆོ་ག་དང་འདོན་ཆ།"
            },
            {
                "name": "སྨོན་ལམ།",
                "heDesc": "",
                "heShortDesc": ""
            },
            {
                "name": "ཀུན་བཟང་སྨོན་ལམ།",
                "heDesc": "",
                "heShortDesc": "སྨོན་ལམ་སྟོབས་པོ་ཆེ།"
            }
        ],
        "books": [
            {
                "title": "ཀུན་བཟང་སྨོན་ལམ།",
                "language": "bo",
                "versionSource": " ",
                "content": [
                    [ 
                        "section 1, sentence 1 (corresponds to the position in the "target>book>" content)",
                        "section 1, sentence 2",
                        "section 1, sentence 3",
                        "section 1, sentence 4",
                        "section 1, sentence 5"
                    ]
                ],
                "direction": "ltr"
            }
        ]
    }
}
```
#### Note:

1. The level of category can be reduced or increased.

2. source>Category1 corresponding to target>Category1' will be regarded by the system as a unique key value and source>Category2 to target>Category2' and so on. If Category1 to Category X shows in a new file, this file can not be imported into the database.

4. "The Title of Texts" and "The Version Title of the Texts" follow the same unique key rule as Categories. And "Categories", "Titles", and "Version Titles" can not be empty.

5. The section and sentence can be empty like this:
    "The Version Title of the Texts'": []

6. Although the default setting divides "categories" and "texts" into two major classes, English("source") and Tibetan("target"), they can also be regarded as a main category and a parallel category, and texts in the same language or various languages ​​can be included as needed.

### 2) Translation

Put your JSON files (file name is arbitrary) into `/jsondata/texts` and execute pechaAPI.py

The sample file description:
```
{
    "source": {
        "categories": [...],
        "books": [
            {
                "title": "book title",
                "language": "two charecters language code (e.g fr | es | zh etc.)",
                "versionSource": "",
                "content": [
                    [ 
                        "section 1, sentence 1 (corresponds to the position in the "target>book>" content)",
                        "section 1, sentence 2",
                        "section 1, sentence 3",
                        "section 1, sentence 4",
                        "section 1, sentence 5"
                    ]
                ],
                "direction": "ltr"
            }
        ]
    }
    },
    "target": {
        "categories": [...],
        "books": [
            {
                "title": "book title",
                "language": "two charecters language code (e.g fr | es | zh etc.)",
                "versionSource": "",
                "content": [
                    [ 
                        "section 1, sentence 1 (corresponds to the position in the "target>book>" content)",
                        "section 1, sentence 2",
                        "section 1, sentence 3",
                        "section 1, sentence 4",
                        "section 1, sentence 5"
                    ]
                ],
                "direction": "ltr"
            }
        ]
    }
}

```

#### Note:
Sentences in diferent version will display on the Resource List erea.

### 3) Web Link for Sentence

Put your JSON files (file name is arbitrary) into `/jsondata/webpages` and execute pechaAPI.py

A sample file:

    [
        {
            "siteName": "CBETA Online Reader",
            "url": "https://cbetaonline.dila.edu.tw/zh/T11n0310_p0623b05",
            "title": "CBETA: T0310",
            "refs": [
                "Prayer of Kuntuzangpo 1:2"
            ],
            "lastUpdated": "2023-11-11"
        },
        {
            "siteName": "CBETA Online Reader",
            "url": "https://cbetaonline.dila.edu.tw/zh/T11n0310_p0623b06",
            "title": "CBETA: T0310",
            "refs": [
                "Prayer of Kuntuzangpo 1:74"
            ],
            "lastUpdated": "2023-11-11"
        },
    ]

#### Note:
In "refs": [ "[The Title of Texts] [section_number]:[sentence_number]" ], the [section_number]:[sentence_number] refers to the content of "The Version Title of the Texts" under [The Title of Texts].

### 4) Commentary, Reference, Summary

Put your JSON files (file name is arbitrary) into `/jsondata/refs` and execute pechaAPI.py

A sample file:

    [
        {
            "refs": [
                "[A The Title of Texts] [section_number]:[sentence_number]",
                "[A The Title of Texts] [section_number]:[sentence_number-sentence_number]"
            ],
            "type": "reference",
        },
        {
            "refs": [
                "Prayer of Kuntuzangpo 1:2", 
                "The short path of Samantabhadra the lamp that illuminates with light 1:1-6"
        
            ],
            "type": "commentary",
        }
    ]

#### Note:
1. In the case of "[The Title of Texts] 2:1-3", "2:1-3" stands for the first 3 sentences in the second section.

2. The reference links will display on the Resource List.

### 5) Sheet for Additional Notes

Put your JSON files (file name is arbitrary) into `/jsondata/sheets` and execute pechaAPI.py

A sample file:

    {
    "title": "Sheet Title",
    "sheet": [
        {
            "ref": "[The Title of Texts] 2:1",
            "heRef": "[The Title of Texts] 2:1",
            "text": {
                "en": "<p>Notes we want to add for the ref above</p>",
                "he": "<p>Notes we want to add for the heRef above</p>"
            }
        },
        {
            "ref": "[The Title of Texts] 2:1",
            "heRef": "[The Title of Texts] 2:1",
            "text": {
                "en": "<p>Notes we want to add for the ref above</p>",
                "he": "<p>Notes we want to add for the heRef above</p>"
            }
        }
    ]
}
