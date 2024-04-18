import os
import json
import yaml
import re

BASEPATH = os.path.dirname(os.path.abspath(__file__))  

def createJson(jsonPayload):
    filename = jsonPayload["source"]["categories"][len(jsonPayload["source"]["categories"]) - 1 ]['name']
    filename = filename.replace(" ", "_")

    with open(f'{BASEPATH}/jsondata/texts/{filename}.json', 'w') as file:
        json.dump(jsonPayload,file, indent=4, ensure_ascii=False) 

def parseBook(url, file): 

    book = {
        'title': '',
        'language': '',
        'versionSource': '',
        'content': []
    }
    chapter = []
    content = []
    emptyLine = []
    try:
        with open(f'{url}/{file}', mode='r', encoding='utf-8') as f:
            text = f.read()
            # Split the text into paragraphs
            paragraphs = text.split('\n\n')

            book['versionSource'] = paragraphs[0].replace('source: ', '')
            book['direction'] = paragraphs[1].replace('direction: ', '')
            book['title'] = paragraphs[2].replace('# ', '') if file.startswith('bo') or file.startswith('en') else paragraphs[2].replace('# ', '')+f'[{file.replace(".md", "")}]'
            book['language'] = file.replace('.md', '')


            for paragraph in paragraphs[3:]:
                
                if paragraph.startswith("CH"):
                    
                    if "/" in paragraph:
                        split_text = paragraph.split('/')
                        # Remove any empty strings resulting from consecutive slashes
                        split_text = [substring.strip() for substring in split_text if substring.strip()]
                        content.append(split_text)
                    

                    processed_stanza = re.sub("CH-\d+", "", paragraph)
                    content = []
                    content.append([processed_stanza.strip()])
                    chapter.append(content)
                    book['content'] = chapter
                else: 
                    content.append([paragraph])

            return book
    except FileNotFoundError:
        print("File not found")
    


def txtToJson():
    #where all the text files are located
    sourcePATH = BASEPATH + "/sources/commentaries"
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
        if(os.path.basename(root) != "commentaries"):
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
                jsonPayload["source"]["categories"].append({key if key != 'enName' else 'name' : value for key, value in cat.items() if key.startswith('bo') != True}) 
                jsonPayload["target"]["categories"].append({key.replace('bo', 'he') if key != 'boName' else 'name': value for key, value in cat.items() if key.startswith('en') != True})  
                
            # Create the JSON file for each text
            createJson(jsonPayload)
            #create_links(jsonPayload)

            # reset the jsonPayload after creating the json file for each text
            jsonPayload["target"]["categories"], jsonPayload["source"]["categories"] = [], []
            jsonPayload["target"]["books"], jsonPayload["source"]["books"] = [], []
        # j = json.dumps(jsonPayload, indent=4, ensure_ascii=False)
        # print(j)
                

def create_links(text):
    commentary_content = text['target']['books'][0]['content']
    #title of root text
    commentary_title = text['source']['categories'][-1]['name']
    link_type = text['source']['categories'][-1]['link']
    root_text_title = text['source']['categories'][-1]['base_text_titles'][0]
    total_link = []

    for i in range(len(commentary_content)):
        ref = {}
        for j in range(len(commentary_content[i])):
            map_list = []
            total_map = len(commentary_content[i][j])
            map_list.append(f'{root_text_title} {i+1}:{j+1}')
            if(total_map > 1):
                map_list.append(f'{commentary_title} {i+1}:{j+1}:1-{total_map}')
            else: 
                map_list.append(f'{commentary_title} {i+1}:{j+1}:1')
            ref['refs'] = map_list
            ref['type'] = link_type.lower()
            total_link.append(ref)
            ref = {}
    # create json
    with open(f'{BASEPATH}/jsondata/refs/{commentary_title}.json', 'w') as file:
        json.dump(total_link,file, indent=4, ensure_ascii=False) 
     

def main():
    print("------ TXT TO JSON -----")
    txtToJson()
    
main()