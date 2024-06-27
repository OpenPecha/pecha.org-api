
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
1. **Prepare JSON Files**: Ensure that the data files follow the specific formats required by the PechaAPI (look below json sample text format).
2. **Organize Files**:
    - **_Books/text json_**: Book/texts json file are need to be stored in folder `/jsondata/texts`
    - **_Links between books_**: links/refs json file is created by using/running `commentaryToJson.py` and stored in `/jsondata/refs`
3. **Execute Scripts**: Run the `commentaryToJson.py` script to create links, followed by executing `pechaAPI.py` to upload the data to Pecha.org.

## Useful links
- 


## File Types 

### 1) Texts/Article

Put your JSON files (file name is arbitrary) into `/jsondata/texts` and execute pechaAPI.py
#### NOTE
For commentary text add bellow key-value in categories 
```
"base_text_titles": [
    "Title of root text (English)"
],
"base_text_mapping": "many_to_one | one_to_one",
"link": "Commentary"

```
[More detail on commentary](https://developers.sefaria.org/docs/commentaries)

**The sample/example file description for complext Commentary text**:

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
                "name": "Commentaries",
                "enDesc": "",
                "enShortDesc": ""
            },
            {
                "name": "The short path of Samantabhadra the lamp that illuminates with light",
                "enDesc": "",
                "enShortDesc": "",
                "base_text_titles": [
                    "Prayer of Kuntuzangpo"
                ],
                "base_text_mapping": "many_to_one",
                "link": "Commentary"
            }
        ],
        "books": [
            {
                "title": "The short path of Samantabhadra the lamp that illuminates with light",
                "language": "en",
                "versionSource": "",
                "text_completeness_status": "in_progress",
                "content": {
                    "The short path of Samantabhadra the lamp that illuminates with light": {
                        "data": [],
                        "A brief presentation of the ground path and result": {
                            "data": []
                        },
                        "The Benefits Of Reading And Hearing The Prayer Of Aspiration": {
                            "data": [],
                            "l actual benefits of listening to and reading the words of the Great Perfection as they are intended applied and recited by a yogin who has attained stability on the path of the Great Perfection": {
                                "data": []
                            },
                            "The Key Points of Time": {
                                "data": []
                            }
                        }
                    }
                }
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
                "name": "འགྲེལ་པ།",
                "heDesc": "",
                "heShortDesc": ""
            },
            {
                "name": "བྱང་གཏེར་དགོངས་པ་ཟང་ཐལ་གྱི་རྒྱུད་ཆེན་ལས་བྱུང་བའི་ཀུན་བཟང་སྨོན་ལམ་གྱི་རྣམ་བཤད། ཀུན་བཟང་ཉེ་ལམ་འོད་སྣང་གསལ་བའི་སྒྲོན་མ།",
                "heDesc": "",
                "heShortDesc": "ཊྰི་ཀའི་ཐུར་མས་བསལ་བ།",
                "base_text_titles": [
                    "Prayer of Kuntuzangpo"
                ],
                "base_text_mapping": "many_to_one",
                "link": "Commentary"
            }
        ],
        "books": [
            {
                "title": "བྱང་གཏེར་དགོངས་པ་ཟང་ཐལ་གྱི་རྒྱུད་ཆེན་ལས་བྱུང་བའི་ཀུན་བཟང་སྨོན་ལམ་གྱི་རྣམ་བཤད། ཀུན་བཟང་ཉེ་ལམ་འོད་སྣང་གསལ་བའི་སྒྲོན་མ།",
                "language": "bo",
                "versionSource": "",
                "text_completeness_status": "in_progress",
                "content": {
                    "བྱང་གཏེར་དགོངས་པ་ཟང་ཐལ་གྱི་རྒྱུད་ཆེན་ལས་བྱུང་བའི་ཀུན་བཟང་སྨོན་ལམ་གྱི་རྣམ་བཤད། ཀུན་བཟང་ཉེ་ལམ་འོད་སྣང་གསལ་བའི་སྒྲོན་མ།": {
                        "data": [
                            "<1><1>དེ་ལ་འདིར་ཀུན་ཏུ་བཟང་པོའི་དེ་ཉིད་ལ་དབང་འབྱོར་མཐར་ཕྱིན་རྙེད་པའི་སངས་རྒྱས་རྣམས། སེམས་ཅན་གྱི་དྲི་མ་བྲལ་བའི་མཛད་པ་ལས་གཞན་མ་མཆིས་པས། དྲི་བྲལ་ལམ་གྱི་མཛད་ཕྲིན་ཐམས་ཅད་ཀྱི་སྐྱེལ་སོ། མཐར་ཐུག་ཀུན་ཏུ་བཟང་པོའི་སྨོན་ལམ་མམ་རྫོགས་ཆེན་མན་ངག་སྡེའི་གཞི་ལམ་འབྲས་བུའི་ལམ་མཆོག་ནས་དྲི་བྲལ་གདོད་མའི་དབྱིངས་སུ་བཙན་ཐབས་སུ་སྦྱོར་བའི་",
                            "(ཉེ་ལམ་འདི་ཉིད་ཅུང་ཟད་འཆད་པ་ལ་གསུམ་སྟེ། ཐོག་མར་གཞི་ལམ་འབྲས་བུའི་རྣམ་བཞག་མདོར་བསྡུས་ཏེ་བསྟན་པ་དང་། དེ་ཉིད་སོ་སོར་ཕྱེ་སྟེ་རྒྱས་པར་འཆད་པ་དང་། སྨོན་ལམ་ཀློག་པ་དང་ཐོས་པའི་ཕན་ཡོན་བསྟན་པ་དང་གསུམ་མོ། །)"
                        ],
                        "ཐོག་མར་གཞི་ལམ་འབྲས་བུའི་རྣམ་བཞག་མདོར་བསྡུས་ཏེ་བསྟན་པ།": {
                            "data": [
                                "<1><2>(དང་པོ་ནི་){ཧོ་སྣང་སྲིད་}སོགས་ཚིག་རྐང་དྲུག་གིས་བསྟན། {ཧོ༵་}ཞེས་པ་འཁྲུལ་བས་དབང་མེད་དུ་བྱས་ཏེ་མི་འདོད་པའི་ཉེས་རྒུད་དྲག་པོས་རབ་ཏུ་གཟིར་བའི་འཁོར་བའི་སེམས་ཅན་རྣམས་ལ་དམིགས་མེད་བརྩེ་བའི་རྣམ་པར་ཤར་ཏེ་འཁྲུལ་སྣང་རང་སར་དག་པའི་ཉེ་ལམ་ཟབ་མོ་འདིར་བསྐུལ་བའི་ཚིག་ཏུ་བྱས་པ་སྟེ། ",
                                "<1><2>འདི་ལྟར་བློའི་ཡུལ་དུ་བྱ་རུང་བའི་ཆོས་རང་ངོས་ནས་བདེན་པར་མ་གྲུབ་པས་{སྣང༵་}བ་ཙམ་དུ་ཟད་ཅིང་། གང་སྣང་ཐ་སྙད་ཙམ་དུ་བསླུ་བ་མེད་པར་གནས་པས་སྣང་ཙམ་དུ་{སྲི༵ད་}ཅིང་ཡོད་པའི་མ་དག་ཀུན་ཉོན་འཁྲུལ་བའི་{འཁོ༵ར་}བའི་སྣོད་བཅུད་རྒྱུ་འབྲས་ཀྱི་སྒྱུ་འཕྲུལ་སྣ་ཚོགས་ཀྱི་བཀོད་པ་འདི་དང་། དག་པ་རྣམ་བྱང་མྱང་{འད༵ས་}ཀྱི་གྲོལ་བ་ཐར་པའི་ཡེ་ཤེས་ཡོན་ཏན་ཕྲིན་ལས་ཀྱི་རོལ་གར་བསམ་ལས་འདས་པའི་འཁྲུལ་གྲོལ་གྱི་ཆོས་འདི་{ཐམ༵ས་}{ཅ༵ད་}{ཀུན༵}། ",
                                "<1><2>ལམ་དེ་གཉིས་ཀྱི་བྱེད་པ་ལས་ཐོབ་ཅིང་གྲུབ་པའི་{འབྲས༵་}{བུ༵་}མཐར་ཐུག་ལ། ཟག་བཅས་མ་དག་འཁྲུལ་སྣང་སྡུག་བདེན་འཁོར་བའི་ཆོས་དང་། ཟག་མེད་དག་པ་ཡེ་ཤེས་ཀྱི་རང་བཞིན་ཐར་པ་དྲི་མེད་ཀྱི་ཆོས་གཉིས་སོ། །",
                                "<1><3>དེ་ལྟ་བུའི་དག་མ་དག་གི་འཁོར་འདས་ཀྱི་ལམ་འབྲས་དེ་དག་ཉིད་ཀྱང་། ཐོག་མའི་གཞིའི་གནས་ལུགས་རང་ངོ་རང་གིས་ཤེས་ཤིང་{རི༵ག་}པར་དབང་ཐོབ་པ་{དང༵་}། རང་སྣང་གཞན་དུ་འཁྲུལ་ཏེ་རང་ངོ་{མ༵་}{རི༵ག་}པར་འཁྲུལ་བའི་ལུས་སྟོབས་རྒྱས་པའི་{ཆོ༵་}{འཕྲུལ༵་}ཙམ་{ཏེ༵}། དེ་ལས་གཞན་པའི་རྟག་བརྟན་ཐེར་ཟུག་གི་དངོས་མཚན་དུ་གྲུབ་པའི་ཆོས་དང་འགལ་བར་གྱུར་པ་ཁོ་ནའོ། །",
                                "<1><4>དེ་ལྟར་ན་གྲོལ་འཁྲུལ་གཞིའི་གནས་ལུགས་གཟིགས་པ་མཐར་ཕྱིན་འབྲས་བུའི་ཡོན་ཏན་ཟད་མི་ཤེས་པ་{ཀུན༵་}ཏུ་{ག༵ནས་}པའི་གཏེར་མཛོད་{བཟང༵་}{པོའི༵་}ཆོས་གྱི་གཏེར་རྟག་ཁྱབ་ལྷུན་གྲུབ་ཏུ་རྡོལ་བ་དྲི་མེད་ཡེ་ཤེས་ཀྱི་དགོངས་{སྨོན༵་}ཟབ་མོའི་{ལམ༵་}ནས་རང་ཉིད་གཤེགས་ཤིང་གཞན་དག་དེ་ནས་དྲངས་པར་མཛད་པའི་སངས་རྒྱས་ཉིད་{ཀྱིས༵་}ཐེག་དགུའི་རྩེ་རྒྱལ་ཡང་གསང་བླ་མེད་ཀྱི་གསང་ལམ་འདི་བསྟན་པས་ན།",
                                "<1><4>དེ་ལྟ་བུའི་ལམ་མཆོག་འདི་ནས་བསྟན་པའི་གཞི་དོན་མངོན་དུ་གྱུར་ཏེ་འཁྲུལ་བའི་གང་ཟག་གི་འཁྲུལ་བའི་དྲི་མའི་ཉེས་སྐྱོན་{ཐམ༵ས་}{ཅ༵ད་}གདོད་མའི་གྲོལ་ས་ཆེན་པོ་{ཆོས༵་}ཀྱི་{དབྱིང༵ས་}ཀྱི་{ཕོ༵་}{བྲང༵་}དེར་དེངས་ཏེ་དྲི་བྲལ་དོན་གྱི་འོག་མིན་དུ་། བྲལ་སྨིན་གྱི་ཡོན་ཏན་གྱི་ཆོས་{མངོ༵ན་}{པར༵་}{རྫོགས༵་}{ཏེ༵་}{སངས༵་}{རྒྱས༵་}ཀྱི་གོ་འཕང་མྱུར་དུ་ཐོབ་པར་{ཤོག༵་}ཅེས་པའོ། །"
                            ]
                        },
                        "སྨོན་ལམ་ཀློག་པ་དང་ཐོས་པའི་ཕན་ཡོན་བསྟན་པ།": {
                            "data": [
                                "(རྩ་བའི་ས་བཅད་གསུམ་པ། སྨོན་ལམ་གྱི་གཞུང་ཐོས་པ་དང་བཀླག་པའི་ཕན་ཡོན་ལ། རྫོགས་ཆེན་གྱི་ལམ་ལ་བརྟན་པ་ཐོབ་པའི་རྣལ་འབྱོར་པས་བསམ་པས་ཇི་ལྟར་སྨོན་པ་དང་སྦྱོར་བ་ཚིག་ཉན་ཀློག་བྱས་པའི་ཕན་ཡོན་དངོས་དང་། དུས་གནད་བསྟན་པ་གཉིས་ལས།)"
                            ],
                            "རྫོགས་ཆེན་གྱི་ལམ་ལ་བརྟན་པ་ཐོབ་པའི་རྣལ་འབྱོར་པས་བསམ་པས་ཇི་ལྟར་སྨོན་པ་དང་སྦྱོར་བ་ཚིག་ཉན་ཀློག་བྱས་པའི་ཕན་ཡོན་དངོས།": {
                                "data": [
                                    "<1><74>(དང་པོ་ནི།) {ཨེ་མ་ཧོ༔ ཕྱིན་ཆད་རྣལ་འབྱོར་སྟོབས་ཆེན་གྱིས༔} སོགས་ཚིག་རྐང་ལྔས་བསྟན་ཏེ་{ཨེ༵་}{མ༵་}{ཧོ༵་}ཞེས་པ་འཆད་འགྱུར་གྱི་ཕན་ཡོན་ལ་ངོ་མཚར་བའི་ཚིག་ཏུ་བྱས་པའོ། །",
                                    "<1><75>དུས་སྙིགས་ཕྱི་མའི་དུས་སུ་འབྱུང་བའི་{ཕྱིན༵་}{ཆད༵་}སྐལ་དམན་གྱི་དོན་དུ་ལམ་འདིའི་{རྣལ༵་}{འབྱོར༵་}གྱི་ཉམས་ལེན་ལ་བརྟན་པའི་{སྟོབས༵་}ཕུལ་བྱུང་ཐོབ་པའི་རྟོགས་པ་{ཆེན༵་}པོའི་རྣལ་འབྱོར་པས་སེམས་ཅན་ལ་སྨན་པའི་ཐུགས་འདུན་{གྱིས༵}། འཁྲུལ་མེད་རང་བྱུང་གི་རིག་པའི་རང་གསལ་གྱི་ཧུར་ཆ་བཏོན་ནས། ",
                                    "<1><76>དུས་གསུམ་རྒྱལ་དང་སྲས་ཀྱིས་ཕན་ཡོན་བསྐལ་པར་བརྗོད་ཀྱང་གཏུགས་པ་མ་མཆིས་པའི་གཞི་ལམ་འབྲས་གསུམ་གྱི་{སྨོན༵་}{ལམ༵་}གྱི་གཞུང་ཡོན་ཏན་{སྟོབ༵ས་}{ཆེ༵ན་}གྱི་རང་བཞིན་ཅན་{འདི༵་}བརྗོད་དེ་སྨོན་ལམ་འདི་བཞིན་{བཏབ༵་}པར་བྱས་{པ༵་}{ཡི༵ས}། སྨོན་ལམ་སྒྲོག་པའི་ཚིག་{འདི༵་}རྣ་བས་{ཐོས༵་}པ་ཙམ་གྱིས་ཀྱང་། ",
                                    "<1><76>དེ་ཐོས་པའི་{སེམས༵་}{ཅན༵་}{ཐམ༵ས་}{ཅད༵་}{ཀུན༵}། སྐྱེ་བའི་ཕྲེང་བ་རིང་པོར་བརྒྱུད་པ་ལ་མི་ལྟོས་པར། {སྐྱེ༵་}{བའི༵་}ཕྲེང་བའི་རིམ་པ་{གསུམ༵་}ཙམ་བརྒྱུད་{ནས༵་}{མངོ༵ན་}པར་{སང༵ས་}{རྒྱས༵་}པར་གསུངས་ན།དེ་ལས་གཞན་འདི་བཞིན་ཉམས་སུ་བླངས་ཏེ་སྒོམ་སྒྲུབ་བྱས་པ་ལ་ཕན་ཡོན་རྒྱ་ཆེར་འབྱུང་བ་སྨོས་མ་དགོས་པའོ། །"
                                ]
                            },
                            "དུས་གནད་བསྟན་པ།": {
                                "data": [
                                    "<1><77>(གཉིས་པ་ནི།) གནས་སྐབས་འཇིག་རྟེན་དུ་དུས་གནད་ལེགས་ཉེས་ཀྱི་ལྟས་སུ་ཤར་བའི་{ཉི༵་}{ཟླ༵་}{གཟའ༵་}{ཡིས༵་}{ཟིན༵་}{པའི༵་}དུས་འབྱུང་{བའམ༵}། རི་དང་བར་སྣང་ལས་སྒྲ་ཆེན་ལྡིར་བའི་ཚེ་{དང༵་}། {ས༵་}{གཡོ༵ས་}{འབྱུང༵་}{བའི༵་}དུས་{སམ༵}། ལྷོ་བྱང་དུ་{ཉི༵་}{མ༵་}{ལྡོག༵་}པར་{འགྱུར༵་}བ་དང་། སྔ་ཕྱི་{ལོ༵་}{འཕོ༵་}བའི་{དུས༵་}རྣམས་སུ། སྨོན་ལམ་འདེབས་པ་པོ་{རང༵་}{ཉིད༵་}{ཀུན༵་}ཏུ་{བཟང༵་}{པོར༵་}{བསྐྱེད༵་}ཅིང་གསལ་བཞིན། ",
                                    "<1><78>ཡུལ་སྐྱེ་བོའི་ཚོགས་དུ་མ་འདུས་པའི་ཕྱོགས་ཀྱི་སྐྱེ་བོ་{ཀུན༵་}{གྱིས༵་}{ཐོས༵་}བཞིན་{པར༵}། སྨོན་ལམ་{འདི༵་}{བརྗོད༵་}{ན༵}། དུས་དང་བསམ་སྦྱོར་རྣམ་དག་ནང་འདོམས་པ་ལས། {ཁམས༵་}{གསུམ༵་}གྱི་འགྲོ་བའི་སྐྱེ་བོ་{སེམ༵ས་}{ཅན༵་}{ཐམས༵་}{ཅད༵་}{ལ༵་}དངོས་བརྒྱུད་ཅི་རིག་པར། {རྣལ༵་}{འབྱོར༵་}{དེ༵་}{ཡི༵་}ཐུགས་བསྐྱེད་རྣམ་པར་དག་པ་དང་། {སྨོན༵་}{ལམ༵་}མཐུ་བཙན་པའི་སྟོབས་{ཀྱིས༵}། གནས་སྐབས་འཁོར་བ་རགས་པའི་{སྡུ༵ག་}{བསྔལ༵་}རྒྱུ་བཅས་ཀྱི་གཉེན་པོ་རང་སྐལ་གྱི་དབང་བོ་དང་འཚམས་པའི་ལམ་རིམ་བཞིན་སྐྱེས་ཏེ། སྡུག་བསྔལ་{རིམ༵་}{གྱིས༵་}{བྲལ༵་}{ནས༵་}{ཀྱང༵་}། ",
                                    "<1><79>{མཐར༵་}{ཐུག༵་}ལམ་ཐམས་ཅད་ཀྱི་མཐར་ཐུག་གི་ཐེག་པ་འདི་ནས་ཀུན་གཞི་ཆ་བཅས་ལས་གྲོལ་བའི་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་{སངས༵་}{རྒྱས༵་}ཀྱི་གོ་འཕང་རིན་པོ་ཆེ་{ཐོབ༵་}{པར༵་}འགྱུར་བར་བསྟན་པའོ། །དེ་ལྟ་བུའི་ཕན་ཡོན་ཇི་སྐད་བཤད་པ་དེ་རྣམས་ཀྱང་། ཚུལ་བཞིན་གེགས་མེད་དུ་སེམས་ཅན་ལ་འབྱོར་ནུས་པར་ཡང་{ཤོག༵་}ཅེས་པའོ།།"
                                ]
                            }
                        }
                    }
                }
            }
        ]
    }
}

```
**The sample/example file description for simple Root/base text**:

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
                "content": [],
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
                        "ཀུན་ཏུ་བཟང་པོ་ང་ཡིས་ཀྱང་༔  <br>  རྒྱུ་རྐྱེན་མེད་པ་གཞི་ཡི་དོན༔  <br>  དེ་ཉིད་གཞི་ལ་རང་བྱུང་རིག༔ <br>",
                        "ཕྱི་ནང་སྒྲོ་སྐུར་སྐྱོན་མ་བཏགས༔ <br>",
                        "དྲན་མེད་མུན་པའི་སྒྲིབ་མ་གོས༔ <br>",
                        "དེ་ཕྱིར་རང་སྣང་སྐྱོན་མ་གོས༔ <br>",
                        "རང་རིག་སོ་ལ་གནས་པ་ལ༔  <br>  སྲིད་གསུམ་འཇིག་ཀྱང་དངངས་སྐྲག་མེད༔ <br>",
                        "འདོད་ཡོན་ལྔ་ལ་ཆགས་པ་མེད༔ <br>",
                        "རྟོག་མེད་ཤེས་པ་རང་བྱུང་ལ༔  <br>  རྡོས་པའི་གཟུགས་དང་དུག་ལྔ་མེད༔ <br>",
                        "རིག་པའི་གསལ་ཆ་མ་འགགས་པ༔ <br>",
                        "ངོ་བོ་གཅིག་ལ་ཡེ་ཤེས་ལྔ༔ <br>",
                        "ཡེ་ཤེས་ལྔ་པོ་སྨིན་པ་ལས༔  <br>  ཐོག་མའི་སངས་རྒྱས་རིགས་ལྔ་བྱུང༔ <br>",
                        "དེ་ལས་ཡེ་ཤེས་མཐའ་རྒྱས་པས༔  <br>  སངས་རྒྱས་བཞི་བཅུ་རྩ་གཉིས་བྱུང་༔ <br>",
                        "ཡེ་ཤེས་ལྔ་ཡི་རྩལ་ཤར་བས༔  <br>  ཁྲག་འཐུང་དྲུག་ཅུ་ཐམ་པ་བྱུང་༔ <br>",
                        "དེ་ཕྱིར་གཞི་རིག་འཁྲུལ་མ་མྱོང་༔ <br>",
                        "ཐོག་མའི་སངས་རྒྱས་ང་ཡིན་པས༔  <br>  ང་ཡི་སྨོན་ལམ་བཏབ་པ་ཡིས༔  <br>  ཁམས་གསུམ་འཁོར་བའི་སེམས་ཅན་གྱིས༔  <br>  རང་བྱུང་རིག་པ་ངོ་ཤེས་ནས༔  <br>  ཡེ་ཤེས་ཆེན་པོ་མཐའ་རྒྱས་ཤོག༔ <br>",
                        "ང་ཡི་སྤྲུལ་པ་རྒྱུན་མི་ཆད༔ <br>",
                        "བྱེ་བ་ཕྲག་བརྒྱ་བསམ་ཡས་འགྱེད༔ <br>",
                        "གང་ལ་གང་འདུལ་སྣ་ཚོགས་སྟོན༔ <br>",
                        "ང་ཡི་ཐུགས་རྗེའི་སྨོན་ལམ་གྱིས༔  <br>  ཁམས་གསུམ་འཁོར་བའི་སེམས་ཅན་ཀུན༔  <br>  རིགས་དྲུག་གནས་ནས་འཐོན་པར་ཤོག༔ <br>",
                        "དང་པོ་སེམས་ཅན་འཁྲུལ་པ་རྣམས༔  <br>  གཞི་ལ་རིག་པ་མ་ཤར་བས༔  <br>  ཅི་ཡང་དྲན་མེད་ཐོམ་མེ་བ༔  <br>  དེ་ཀ་མ་རིག་འཁྲུལ་པའི་རྒྱུ༔ <br>",
                        "དེ་ལ་ཧད་ཀྱིས་བརྒྱལ་བ་ལས༔  <br>  དངངས་སྐྲག་ཤེས་པ་ཟ་ཟི་འགྱུས༔ <br>",
                        "དེ་ལས་བདག་གཞན་དགྲར་འཛིན་སྐྱེས༔ <br>",
                        "བག་ཆགས་རིམ་བཞིན་བརྟས་པ་ལས༔  <br>  འཁོར་བ་ལུགས་སུ་འཇུག་པ་བྱུང་༔ <br>",
                        "དེ་ལས་ཉོན་མོངས་དུག་ལྔ་རྒྱས༔ <br>",
                        "དུག་ལྔའི་ལས་ལ་རྒྱུན་ཆད་མེད༔ <br>",
                        "དེ་ཕྱིར་སེམས་ཅན་འཁྲུལ་པའི་གཞི༔ <br>",
                        "དྲན་མེད་མ་རིག་ཡིན་པའི་ཕྱིར༔  <br>  སངས་རྒྱས་ང་ཡི་སྨོན་ལམ་གྱིས༔  <br>  ཀུན་གྱི་རིག་པ་རང་ཤེས་ཤོག༔ <br>",
                        "ལྷན་ཅིག་སྐྱེས་པའི་མ་རིག་པ༔  <br>  ཤེས་པ་དྲན་མེད་ཡེངས་པ་ཡིན༔ <br>",
                        "ཀུན་ཏུ་བཏགས་པའི་མ་རིག་པ༔  <br>  བདག་གཞན་གཉིས་སུ་འཛིན་པ་ཡིན༔ <br>",
                        "ལྷན་ཅིག་ཀུན་བཏགས་མ་རིག་གཉིས༔  <br>  སེམས་ཅན་ཀུན་གྱི་འཁྲུལ་གཞི་ཡིན༔ <br>",
                        "སངས་རྒྱས་ང་ཡི་སྨོན་ལམ་གྱིས༔  <br>  འཁོར་བའི་སེམས་ཅན་ཐམས་ཅད་ཀྱི༔  <br>  དྲན་མེད་འཐིབ་པའི་མུན་པ་སངས༔ <br>",
                        "གཉིས་སུ་འཛིན་པའི་ཤེས་པ་དྭངས༔ <br>",
                        "རིག་པའི་རང་ངོ་ཤེས་པར་ཤོག༔ <br>",
                        "གཉིས་འཛིན་བློ་ནི་ཐེ་ཚོམ་སྟེ༔ <br>",
                        "ཞེན་པ་ཕྲ་མོ་སྐྱེས་པ་ལས༔  <br>  བག་ཆགས་འཐུག་པོ་རིམ་གྱིས་བརྟས༔ <br>",
                        "ཟས་ནོར་གོས་དང་གནས་དང་གྲོགས༔  <br>  འདོད་ཡོན་ལྔ་དང་བྱམས་པའི་གཉེན༔  <br>  ཡིད་འོང་ཆགས་པའི་འདོད་པས་གདུངས༔ <br>",
                        "དེ་དག་འཇིག་རྟེན་འཁྲུལ་པ་སྟེ༔ <br>",
                        "གཟུང་འཛིན་ལས་ལ་ཟད་མཐའ་མེད༔ <br>",
                        "ཞེན་པའི་འབྲས་བུ་སྨིན་པའི་ཚེ༔  <br>  རྐམ་ཆགས་གདུང་བའི་ཡི་དྭགས་སུ༔  <br>  སྐྱེས་ནས་བཀྲེས་སྐོམ་ཡ་རེ་ང་༔ <br>",
                        "སངས་རྒྱས་ང་ཡི་སྨོན་ལམ་གྱིས༔  <br>  འདོད་ཆགས་ཞེན་པའི་སེམས་ཅན་རྣམས༔  <br>  འདོད་པའི་གདུང་བ་ཕྱིར་མ་སྤངས༔ <br>",
                        "འདོད་ཆགས་ཞེན་པ་ཚུར་མ་བླང་༔ <br>",
                        "ཤེས་པ་རང་སོར་ཀློད་པ་ཡིས༔  <br>  རིག་པ་རང་སོ་ཟིན་གྱུར་ནས༔  <br>  ཀུན་རྟོག་ཡེ་ཤེས་ཐོབ་པར་ཤོག༔ <br>",
                        "ཕྱི་རོལ་ཡུལ་གྱི་སྣང་བ་ལ༔  <br>  འཇིགས་སྐྲག་ཤེས་པ་ཕྲ་མོ་འགྱུས༔ <br>",
                        "སྡང་བའི་བག་ཆགས་བརྟས་པ་ལས༔  <br>  དགྲར་འཛིན་བརྡེག་གསོད་ཧྲག་པ་སྐྱེས༔ <br>",
                        "ཞེ་སྡང་འབྲས་བུ་སྨིན་པའི་ཚེ༔  <br>  དམྱལ་བའི་བཙོ་བསྲེག་སྡུག་རེ་བསྔལ༔ <br>",
                        "སངས་རྒྱས་ང་ཡིས་སྨོན་ལམ་གྱིས༔  <br>  འགྲོ་དྲུག་སེམས་ཅན་ཐམས་ཅད་ཀྱི༔  <br>  ཞེ་སྡང་དྲག་པོ་སྐྱེས་པའི་ཚེ༔  <br>  སྤང་བླང་མི་བྱ་རང་སོར་ཀློད༔ <br>",
                        "རིག་པ་རང་སོ་ཟིན་གྱུར་ནས༔  <br>  གསལ་བའི་ཡེ་ཤེས་ཐོབ་པར་ཤོག༔ <br>",
                        "རང་སེམས་ཁེངས་པར་གྱུར་པ་ལ༔  <br>  གཞན་ལ་འགྲན་སེམས་སྨད་པའི་བློ༔ <br>",
                        "ང་རྒྱལ་དྲག་པོའི་སེམས་སྐྱེས་པས༔  <br>  བདག་གཞན་འཐབ་རྩོད་སྡུག་བསྔལ་མྱོང༔ <br>",
                        "ལས་དེའི་འབྲས་བུ་སྨིན་པའི་ཚེ༔  <br>  འཕོ་ལྟུང་མྱོང་བའི་ལྷ་རུ་སྐྱེ༔ <br>",
                        "སངས་རྒྱས་ང་ཡི་སྨོན་ལམ་གྱིས༔  <br>  ཁེངས་སེམས་སྐྱེས་པའི་སེམས་ཅན་རྣམས༔  <br>  དེ་ཚེ་ཤེས་པ་རང་སོར་ཀློད༔ <br>",
                        "རིག་པ་རང་སོ་ཟིན་གྱུར་ནས༔  <br>  མཉམ་པ་ཉིད་ཀྱི་དོན་རྟོགས་ཤོག༔ <br>",
                        "གཉིས་འཛིན་བརྟས་པའི་བག་ཆགས་ཀྱིས༔  <br>  བདག་བསྟོད་གཞན་སྨོད་ཟུག་རྔུ་ལས༔  <br>  འཐབ་རྩོད་འགྲན་སེམས་བརྟས་པ་ལས༔  <br>  གསོད་གཅོད་ལྷ་མིན་གནས་སུ་སྐྱེ༔ <br>",
                        "འབྲས་བུ་དམྱལ་བའི་གནས་སུ་ལྟུང་༔ <br>",
                        "སངས་རྒྱས་ང་ཡི་སྨོན་ལམ་གྱིས༔  <br>  འགྲན་སེམས་འཐབ་རྩོད་སྐྱེས་པ་རྣམས༔  <br>  དགྲར་འཛིན་མི་བྱ་རང་སོར་ཀློད༔ <br>",
                        "ཤེས་པ་རང་སོ་ཟིན་གྱུར་ནས༔  <br>  ཕྲིན་ལས་ཐོགས་མེད་ཡེ་ཤེས་ཤོག༔ <br>",
                        "དྲན་མེད་བཏང་སྙོམས་ཡེངས་པ་ཡིས༔  <br>  འཐིབས་དང་རྨུགས་དང་བརྗེད་པ་དང་༔  <br>  བརྒྱལ་དང་ལེ་ལོ་གཏི་མུག་པས༔  <br>  འབྲས་བུ་སྐྱབས་མེད་བྱོལ་སོང་འཁྱམས༔ <br>",
                        "སངས་རྒྱས་ང་ཡི་སྨོན་ལམ་གྱིས༔  <br>  གཏི་མུག་བྱིང་པའི་མུན་པ་ལ༔  <br>  དྲན་པ་གསལ་བའི་མདངས་ཤར་བས༔  <br>  རྟོག་མེད་ཡེ་ཤེས་ཐོབ་པར་ཤོག༔ <br>",
                        "ཁམས་གསུམ་སེམས་ཅན་ཐམས་ཅད་ཀུན༔  <br>  ཀུན་གཞི་སངས་རྒྱས་ང་དང་མཉམ༔ <br>",
                        "དྲན་མེད་འཁྲུལ་པའི་གཞི་རུ་སོང་༔ <br>",
                        "ད་ལྟ་དོན་མེད་ལས་ལ་སྤྱོད༔ <br>",
                        "ལས་དྲུག་རྨི་ལམ་འཁྲུལ་པ་འདྲ༔ <br>",
                        "ང་ནི་སངས་རྒྱས་ཐོག་མ་ཡིན༔ <br>",
                        "འགྲོ་དྲུག་སྤྲུལ་པས་འདུལ་བའི་ཕྱིར༔  <br>  ཀུན་ཏུ་བཟང་པོའི་སྨོན་ལམ་གྱིས༔  <br>  སེམས་ཅན་ཐམས་ཅད་མ་ལུས་པ༔  <br>  ཆོས་ཀྱི་དབྱིངས་སུ་འཚང་རྒྱ་ཤོག༔ <br>",
                        "ཨ་ཧོ༔ <br>",
                        "ཕྱིན་ཆད་རྣལ་འབྱོར་སྟོབས་ཅན་གྱིས༔  <br>  འཁྲུལ་མེད་རིག་པ་རང་གསལ་ནས༔ <br>",
                        "སྨོན་ལམ་སྟོབས་ཅན་འདི་བཏབ་པས༔  <br>  འདི་ཐོས་སེམས་ཅན་ཐམས་ཅད་ཀུན༔  <br>  སྐྱེ་བ་གསུམ་ནས་མངོན་འཚང་རྒྱ༔ <br>",
                        "ཉི་ཟླ་གཟའ་ཡིས་ཟིན་པའམ༔  <br>  སྒྲ་དང་ས་གཡོས་བྱུང་བའམ༔  <br>  ཉི་མ་ལྡོག་འགྱུར་ལོ་འཕོ་དུས༔  <br>  རང་ཉིད་ཀུན་ཏུ་བཟང་པོར་བསྐྱེད༔ <br>",
                        "ཀུན་གྱིས་ཐོས་སར་འདི་བརྗོད་ན༔  <br>  ཁམས་གསུམ་སེམས་ཅན་ཐམས་ཅད་ལ༔  <br>  རྣལ་འབྱོར་དེ་ཡི་སྨོན་ལམ་གྱིས༔  <br>  སྡུག་བསྔལ་རིམ་བཞིན་གྲོལ་ནས་ཀྱང་༔ <br>",
                        "མཐའ་རུ་སངས་རྒྱས་ཐོབ་པར་འགྱུར༔ <br>"
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
