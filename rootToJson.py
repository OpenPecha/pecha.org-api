import os
import json
import yaml
import re

BASEPATH = os.path.dirname(os.path.abspath(__file__))  

def createJson(jsonPayload):
    filename = jsonPayload["source"]["categories"][len(jsonPayload["source"]["categories"]) - 1 ]['name']
    filename = filename.replace(" ", "_")

    with open(f'{BASEPATH}/jsondata/texts/baseText/{filename}.json', 'w') as file:
        json.dump(jsonPayload,file, indent=4, ensure_ascii=False) 


def parseBook(url, file): 

    book = {
        'title': '',
        'language': '',
        'versionSource': '',
        'content': []
    }
    content = []
    chapter = []
    line_breaker = ["། །","ག །","ག།","།།","ཤ །","ཤ།","ཀ།","ཀ །", "།། །།", "། །།", "།།།"]
    try:
        with open(f'{url}/{file}', mode='r', encoding='utf-8') as f:
            text = f.read()
            # Split the text into paragraphs
            paragraphs = text.split('\n\n')

            book['versionSource'] = paragraphs[0].replace('source:', '').strip()
            book['direction'] = paragraphs[1].replace('direction: ', '').strip()
            book['title'] = paragraphs[2].replace('# ', '').strip() if file.startswith('bo') or file.startswith('en') else paragraphs[2].replace('# ', '')+f'[{file.replace(".md", "")}]'
            book['language'] = file.replace('.md', '').strip()

            for paragraph in paragraphs[3:]:
                found_breaker = [breaker for breaker in line_breaker if breaker in paragraph]

                # Split the stanza into lines, remove spaces and tabs from each line, then join back with a space
                if "|" in paragraph:
                    paragraph = paragraph.replace('|',' <br> ')
                if len(found_breaker) > 0:
                   for breaker in found_breaker:
                      paragraph = paragraph.replace(breaker, breaker+' <br> ')
                processed_lines = [line.strip().replace('\t', '') + ' <br>' for line in paragraph.replace('\t', '').split('\n') if line.strip()]
                processed_stanza = ' '.join(processed_lines)
                #chapter
                if paragraph.startswith("ch"):
                    processed_stanza = re.sub("ch-\d+ ", "", processed_stanza)
                    processed_stanza = re.sub("<\d+> ", "", processed_stanza)
                    content = []
                    content.append(processed_stanza)
                    chapter.append(content)
                    book['content'] = chapter
                else: 
                    processed_stanza = re.sub("<\d+> ", "", processed_stanza)
                    content.append(processed_stanza)

                


                

                
                
                
            return book
    except FileNotFoundError:
        print("File not found")
    


def txtToJson():
    #where all the text files are located
    sourcePATH = BASEPATH + "/sources/root_texts"
    # structure of the JSON file requiered by the API
    jsonPayload = {
        "source": {
            "categories": [],
            "books": []
        },
        "target": {
            "categories": [],
            "books": []
        }
    }
    # Walk through the source directory
    for root, dirs, files in os.walk(sourcePATH):
        print(root)
        if(os.path.basename(root) != "root_texts"): # skip the sources directory

            #BOOKS: 
            for file in files:
                if(file.endswith('.md')):
                    if(file == "bo.md"):
                        jsonPayload["target"]["books"].append(parseBook(root, file))
                    else:
                        jsonPayload["source"]["books"].append(parseBook(root, file))
             
                        
            #CATEGORIES: 
            # Open the YAML file and load its content
            with open(f'{root}/meta.yaml', 'r') as file:
                yamlCategories = (yaml.safe_load(file))
                # filter yaml to seperate source and target language's categories
            for cat in yamlCategories['categories']:
                jsonPayload["source"]["categories"].append({key if key != 'enName' else 'name': value for key, value in cat.items() if key.startswith('en')}) 
                jsonPayload["target"]["categories"].append({key.replace('bo', 'he') if key != 'boName' else 'name': value for key, value in cat.items() if key.startswith('bo')})  
                
            # Create the JSON file for each text
            createJson(jsonPayload)
            # reset the jsonPayload after creating the json file for each text
            jsonPayload["target"]["categories"], jsonPayload["source"]["categories"] = [], []
            jsonPayload["target"]["books"], jsonPayload["source"]["books"] = [], []
                
                
def main():
    print("------ TXT TO JSON -----")
    txtToJson()
    
main()