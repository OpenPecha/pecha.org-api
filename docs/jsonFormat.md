# This documantation is for OPF

## text/book json file description:


1. ### Root text
   Content of the books/text in pecha.org is prepared according to complexity of text. That is, 
    some text can have multiple level/node and sub-levels and some have only one level/node.

- Simple text: text having one level/node:
```
    "books": [
            {
                "title": "ཀུན་བཟང་སྨོན་ལམ།",
                "language": "bo",
                "author": "author name"
                "versionSource": " ",
                "content": [
                    [
                        "༄༅། །དཔལ་ཀུན་ཏུ་བཟང་པོའི་སྨོན་ལམ་བཞུགས་སོ། ། <br>",
                        "ཧོ༔ སྣང་སྲིད་འཁོར་འདས་ཐམས་ཅད་ཀུན༔  <br>  གཞི་གཅིག་ལམ་གཉིས་འབྲས་བུ་གཉིས༔ <br>",
                        "རིག་དང་མ་རིག་ཆོ་འཕྲུལ་ཏེ༔ <br>",
                        "ཀུན་ཏུ་བཟང་པོའི་སྨོན་ལམ་གྱིས༔  <br>  ཐམས་ཅད་ཆོས་དབྱིངས་ཕོ་བྲང་དུ༔  <br>  མངོན་པར་རྫོགས་ཏེ་འཚང་རྒྱ་ཤོག༔ <br>",
                    ]
                ],
                "direction": "ltr"
            }
    ]
```


2. ### Commentary text

- **Simple text: text having one level/node**:
```
    "books": [
            {
                "title": "contentary text title",
                "language": "bo",
                "author": "author name"
                "versionSource": " ",
                "base_text_titles": "root text title"
                "content": [
                    [
                        "<1><1>༄༅། །དཔལ་ཀུན་ཏུ་བཟང་པོའི་སྨོན་ལམ་བཞུགས་སོ། ། <br>",
                        "<1><2>ཧོ༔ སྣང་སྲིད་འཁོར་འདས་ཐམས་ཅད་ཀུན༔  <br>  གཞི་གཅིག་ལམ་གཉིས་འབྲས་བུ་གཉིས༔ <br>",
                        "<1><2>རིག་དང་མ་རིག་ཆོ་འཕྲུལ་ཏེ༔ <br>",
                        "<1><2>ཀུན་ཏུ་བཟང་པོའི་སྨོན་ལམ་གྱིས༔  <br>  ཐམས་ཅད་ཆོས་དབྱིངས་ཕོ་བྲང་དུ༔  <br>,
                        "རིག་དང་མ་རིག་ཆོ་འཕྲུལ་ཏེ༔ <br>", // does not have alignment to root text
                        "<1><3>ཀུན་ཏུ་བཟང་པོའི་སྨོན་ལམ་གྱིས༔  <br>  ཐམས་ཅད་ཆོས་དབྱིངས་ཕོ་བྲང་དུ༔  <br>,
                        "<1><3>རིག་དང་མ་རིག་ཆོ་འཕྲུལ་ཏེ༔ <br>",
                        "<1><4>ཀུན་ཏུ་བཟང་པོའི་སྨོན་ལམ་གྱིས༔  <br>  ཐམས་ཅད་ཆོས་དབྱིངས་ཕོ་བྲང་དུ༔  <br>,
                    ]
                ],
                "direction": "ltr"
            }
    ]
```

- **complex text_: text having multiples level/node and sub-levels**. 
```
    {
    "books": [
            {
                "title": "book title",
                "language": "bo",
                "versionSource": "",
                "base_text_titles": "root text title"
                "content": {
                    "1supche title": {
                        "data": [
                            "<1><2>intro data to parent node/level",
                            "some text"
                        ],
                        "1.1supche title": {
                            "data": [
                                "<1><2>text content1",
                                "<1><2>text content2",
                                "<1><2>text content3",
                                "<1><4>text content4",
                                "<1><5>text content5"
                            ]
                        },
                        "2supche title": {
                            "data": [
                                "intro to parent level/node"
                            ],
                            "2.1supche title": {
                                "data": [
                                    "<1><5>text content1",
                                    "text content2" // does not have alignment with root text
                                ]
                            }
                        }
                    }
                }
            }
        ]
    }
```