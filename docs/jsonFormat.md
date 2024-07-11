# This documantation is for OPF

## text/book json file description:



1. **categories**: Categories define the location of book in pecha.org. <br>
    For example: In pecha.org, if we want to access book "Prayer of kuntuzangpo", we have to click `"Liturgy" > "Prayers" > "Prayer of Kuntuzangpo"`.So each and every book need categories to defines its location and each category has its own name, short and long description. 
    ```
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
    ```
2. **books**:<br>
    Content of the books/text in pecha.org is prepared according to complexity of text. That is, 
    some text can have multiple level/node and sub-levels and some have only one level/node.
- _complex text_: text having multiples level/node and sub-levels. 
    ```
    "books": [
            {
                "title": "བྱང་གཏེར་དགོངས་པ་ཟང་ཐལ་གྱི་རྒྱུད་ཆེན་ལས་བྱུང་བའི་ཀུན་བཟང་སྨོན་ལམ་གྱི་རྣམ་བཤད། ཀུན་བཟང་ཉེ་ལམ་འོད་སྣང་གསལ་བའི་སྒྲོན་མ།",
                "language": "bo",
                "versionSource": ""
                "content": {
                    "བྱང་གཏེར་དགོངས་པ་ཟང་ཐལ་གྱི་རྒྱུད་ཆེན་ལས་བྱུང་བའི་ཀུན་བཟང་སྨོན་ལམ་གྱི་རྣམ་བཤད། ཀུན་བཟང་ཉེ་ལམ་འོད་སྣང་གསལ་བའི་སྒྲོན་མ།": {
                        "data": [
                            "<1><1>intro data to parent node/level",
                            "some text"
                        ],
                        "ཐོག་མར་གཞི་ལམ་འབྲས་བུའི་རྣམ་བཞག་མདོར་བསྡུས་ཏེ་བསྟན་པ།": {
                            "data": [
                                "<1><2>text content1",
                                "<1><2>text content2",
                                "<1><2>text content3",
                                "<1><2>text content4",
                                "<1><2>text content5"
                            ]
                        },
                        "སྨོན་ལམ་ཀློག་པ་དང་ཐོས་པའི་ཕན་ཡོན་བསྟན་པ།": {
                            "data": [
                                "intro to parent level/node"
                            ],
                            "རྫོགས་ཆེན་གྱི་ལམ་ལ་བརྟན་པ་ཐོབ་པའི་རྣལ་འབྱོར་པས་བསམ་པས་ཇི་ལྟར་སྨོན་པ་དང་སྦྱོར་བ་ཚིག་ཉན་ཀློག་བྱས་པའི་ཕན་ཡོན་དངོས།": {
                                "data": [
                                    "<1><74>text content1",
                                    "<1><75>text content2"
                                ]
                            }
                        }
                    }
                }
            }
        ]
    ```
- Simple text: text having one level/node:
    ```
    "books": [
            {
                "title": "ཀུན་བཟང་སྨོན་ལམ།",
                "language": "bo",
                "versionSource": " ",
                "content": [
                    [
                        "༄༅། །དཔལ་ཀུན་ཏུ་བཟང་པོའི་སྨོན་ལམ་བཞུགས་སོ། ། <br>",
                        "ཧོ༔ སྣང་སྲིད་འཁོར་འདས་ཐམས་ཅད་ཀུན༔  <br>  གཞི་གཅིག་ལམ་གཉིས་འབྲས་བུ་གཉིས༔ <br>",
                        "རིག་དང་མ་རིག་ཆོ་འཕྲུལ་ཏེ༔ <br>",
                        "ཀུན་ཏུ་བཟང་པོའི་སྨོན་ལམ་གྱིས༔  <br>  ཐམས་ཅད་ཆོས་དབྱིངས་ཕོ་བྲང་དུ༔  <br>  མངོན་པར་རྫོགས་ཏེ་འཚང་རྒྱ་ཤོག༔ <br>",
                        "ཀུན་གྱི་གཞི་ནི་འདུས་མ་བྱས༔ <br>",
                        "རང་བྱུང་ཀློང་ཡངས་བརྗོད་དུ་མེད༔ <br>",
                        "འཁོར་འདས་གཉིས་ཀའི་མིང་མེད་དོ༔ <br>",
                        "དེ་ཉིད་རིག་ན་སངས་རྒྱས་ཏེ༔ <br>",
                        "མ་རིག་སེམས་ཅན་འཁོར་བར་འཁྱམས༔ <br>",
                        "ཁམས་གསུམ་སེམས་ཅན་ཐམས་ཅད་ཀྱིས༔  <br>  བརྗོད་མེད་གཞི་དོན་རིག་པར་ཤོག༔ <br>",
                        "ཀུན་ཏུ་བཟང་པོ་ང་ཡིས་ཀྱང་༔  <br>  རྒྱུ་རྐྱེན་མེད་པ་གཞི་ཡི་དོན༔  <br>  དེ་ཉིད་གཞི་ལ་རང་བྱུང་རིག༔ <br>"
                    ]
                ],
                "direction": "ltr"
            }
    ]
    ```

    

    



    


3. **Source and Target**: 

    - __Source__: Where all English version of book and its metadata are store
    - __Target__: Where all Tibetan version of book and its metadata are store
    


 