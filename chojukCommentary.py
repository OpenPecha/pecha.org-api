import os
import json
import yaml
import re

BASEPATH = os.path.dirname(os.path.abspath(__file__))  

def createJson(jsonPayload):
    filename = jsonPayload["source"]["categories"][len(jsonPayload["source"]["categories"]) - 1 ]['name']
    filename = filename.replace(" ", "_")

    with open(f'{BASEPATH}/jsondata/texts/commentaryText/{filename}.json', 'w') as file:
        json.dump(jsonPayload,file, indent=4, ensure_ascii=False) 


def parseBook(url, file): 

    book = {
        'title': '',
        'language': '',
        'versionSource': '',
        "completestatus": "in_progress",
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
            

            book['versionSource'] = paragraphs[0].replace('source: ', '').strip()
            book['direction'] = paragraphs[1].replace('direction: ', '').strip()
            book['title'] = paragraphs[2].replace('# ', '').strip() if file.startswith('bo') or file.startswith('en') else paragraphs[2].replace('# ', '')+f'[{file.replace(".md", "")}]'
            book['language'] = file.replace('.md', '').strip()

            for paragraph in paragraphs[3:]:
                paragraph = paragraph.strip()
                found_breaker = [breaker for breaker in line_breaker if breaker in paragraph]

                processed_lines = [line.strip().replace('\t', '') for line in paragraph.replace('\t', '').split('\n') if line ]
                processed_stanza = ' '.join(processed_lines)

                # if len(found_breaker) > 0:
                #    for breaker in found_breaker:
                #       paragraph = paragraph.replace(breaker, breaker+' <br> ')
                # processed_lines = [line.strip().replace('\t', '') for line in paragraph.replace('\t', '').split('\n') if line ]
                # processed_stanza = ' '.join(processed_lines)

                #chapter
                if paragraph.startswith("ch"):
                    content = []
                    processed_stanza = re.sub(r'ch-\d+', "", processed_stanza)
                    processed_stanza = re.sub(r'<\d+>', "", processed_stanza)
                    if(processed_stanza == ""):
                        content.append([])  
                    else: 
                        content.append([processed_stanza])
                    chapter.append(content)
                    book['content'] = chapter
                else: 
                    processed_stanza = re.sub("<\d+> ", "", processed_stanza)
                    if(processed_stanza == ""):
                        content.append([])  
                    else: 
                        content.append([processed_stanza])
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
            print(dirs)
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
            create_links(jsonPayload)

            # reset the jsonPayload after creating the json file for each text
            jsonPayload["target"]["categories"], jsonPayload["source"]["categories"] = [], []
            jsonPayload["target"]["books"], jsonPayload["source"]["books"] = [], []
        # j = json.dumps(jsonPayload, indent=4, ensure_ascii=False)
        # print(j)
                

def create_links(text):
    
    commentary_content = text['target']['books'][0]['content']
    #title of root text
    root_text_title = text['source']['categories'][-1]['base_text_titles'][0]
    commentary_title = text['source']['categories'][-1]['name']
    link_type = text['source']['categories'][-1]['link']
    total_link = []
    
    print(root_text_title)
    for i in range(len(commentary_content)):
        ref = {}
        for j in range(len(commentary_content[i])):
            map_list = []
            total_map = len(commentary_content[i][j])
            map_list.append(f'{root_text_title} {i+1}:{j+1}')
            if (total_map == 0): # no mapping
                continue
            elif(total_map > 1): # one mapping
                map_list.append(f'{commentary_title} {i+1}:{j+1}:1-{total_map}')
            else:  #many mapping
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