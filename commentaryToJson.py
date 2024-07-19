import os
import json
import yaml
import re
from collections import defaultdict

BASEPATH = os.path.dirname(os.path.abspath(__file__))  

# ?def createJson(jsonPayload):
#     filename = jsonPayload["source"]["categories"][len(jsonPayload["source"]["categories"]) - 1 ]['name']
#     filename = filename.strip()

#     with open(f'{BASEPATH}/jsondata/texts/{filename.replace(" ", "_")}.json', 'w') as file:
#         json.dump(jsonPayload,file, indent=4, ensure_ascii=False) 

# def parseBook(url, file): 

#     book = {
#         'title': '',
#         'language': '',
#         'versionSource': '',
#         'mapping': {
#             'linker_pair': []
#         },
#         'content': []
#     }
#     chapter = []
#     content = []
#     current_group = 0 
#     groups = {}
#     is_multi_chapter = False


#     line_indices = []  # To store the indexed lines
#     index_map = {}  # Map numbers to their corresponding index
#     current_index = 0
    

#     try:
#         with open(f'{url}/{file}', mode='r', encoding='utf-8') as f:
#             text = f.read()
#             # Split the text into paragraphs
#             paragraphs = text.split('\n\n')

#             book['versionSource'] = paragraphs[0].replace('source: ', '')
#             book['direction'] = paragraphs[1].replace('direction: ', '')
#             book['title'] = paragraphs[2].replace('# ', '') if file.startswith('bo') or file.startswith('en') else paragraphs[2].replace('# ', '')+f'[{file.replace(".md", "")}]'
#             book['language'] = file.replace('.md', '')
#             book['mapping']['commentary'] = book['title']

#             for commentary_num, paragraph in enumerate(paragraphs[3:]):
#                 # Line break
#                 if "|" in paragraph:
#                     paragraph = paragraph.replace('|',' <br> ')
#                 # Quotation
#                 if "[" in paragraph:
#                     paragraph = paragraph.replace('[',' <i> ')
#                     paragraph = paragraph.replace(']',' </i> ')
#                 # Citation
#                 if "{" in paragraph:  
#                     paragraph = paragraph.replace('{',' <b> ')
#                     paragraph = paragraph.replace('}',' </b> ')
#                 # Sapche
#                 if "(" in paragraph:  
#                     paragraph = paragraph.replace("(",' <u> ')
#                     paragraph = paragraph.replace(")",' </u> ')

#                 # list root and commentary link number.
#                 match = re.match(r'<(\d+)>', paragraph)
#                 if match:
#                     number = int(match.group(1))
#                     if number not in index_map.keys():
#                         index_map[number] = current_index
#                     current_index += 1
#                     line_indices.append([number, current_index ])
                        
#                 else:
#                     current_index += 1
                        
#                 #Chapter segmentation
#                 if paragraph.startswith("CH"):
#                     is_multi_chapter = True
                    
#                     processed_stanza = re.sub("CH-\d+", "", paragraph)
#                     content = []
#                     content.append([processed_stanza.strip()])
#                     chapter.append(content)
#                     book['content'] = chapter
                
#                 #if have only one chapter
#                 elif(is_multi_chapter == False):
                    
#                     match = re.match(r'^<(\d+)>', paragraph)
#                     if match:
#                         # Found a new group number, update the current group
#                         current_group = int(match.group(1))
#                         # Ensure the key exists in the dictionary
#                         if current_group not in groups:
#                             groups[current_group] = []
#                         # Extract the rest of the line after the group number, if any
#                         text = paragraph[match.end():].strip()
#                         if text:  # Add the text if it's not just the number
#                             groups[current_group].append(text)
#                     else:
#                         # No new group number, append line to the current group
#                         current_group = f'no_link-{commentary_num}'
#                         groups[current_group] = [paragraph.replace('\n', '').strip()]
                    
#                 else:
#                     processed_stanza = re.sub("<\d+>", "", paragraph.strip())
#                     content.append([processed_stanza])

#             if groups:
#                 final_group = [groups[key] for key in groups]
#                 content.append(final_group)
#                 book['content'] = content
#             book['mapping']['linker_pair'] = [line_indices]
              
#             return book
#     except FileNotFoundError:
#         print("File not found")


# def txtToJson():
#     #where all the text files are located
#     sourcePATH = BASEPATH + "/sources/commentaries"
#     # structure of the JSON file requiered by the API
#     jsonPayload = {
#         "source": {
#             "categories": [],
#             "books": []
#         },
#         "target": {
#             "categories": [],
#             "books": []
#         }
#     }
#     # Walk through the source directory
#     for root, dirs, files in os.walk(sourcePATH):
#         if(os.path.basename(root) != "commentaries"):
            
                
#             #CATEGORIES: 
#             # Open the YAML file and load its content
#             with open(f'{root}/meta.yaml', 'r') as file:
#                 yamlCategories = (yaml.safe_load(file))
#                 # filter yaml to seperate source and target language's categories
#             for cat in yamlCategories['categories']:
#                 jsonPayload["source"]["categories"].append({key if key != 'enName' else 'name' : value.strip() if key == "enName" else value 
#                     for key, value in cat.items() 
#                     if key.startswith('bo') != True
#                 }) 
#                 jsonPayload["target"]["categories"].append({
#                     key.replace('bo', 'he') if key != 'boName' else 'name': value.strip() if key == "boName" else value
#                     for key, value in cat.items()
#                     if not key.startswith('en')
#                 })

            
#             #BOOKS: 
#             for file in files:
#                 if(file.endswith('.md')):
#                     # if(file == "bo.md"):
#                     jsonPayload["target"]["books"].append(parseBook(root, file))

#                     d = {
#                             'title': jsonPayload["source"]["categories"][-1]['name'],
#                             'language': 'en',
#                             'versionSource': '',
#                             'content': [],
#                         }
                    
#                     jsonPayload["source"]["books"].append(d)
                
#             # Create the JSON file for each text
#             createJson(jsonPayload)
#             if(len(jsonPayload['target']['books'][0]['mapping']['linker_pair'][0]) > 0):
#                 create_links(jsonPayload)

#             # reset the jsonPayload after creating the json file for each text
#             jsonPayload["target"]["categories"], jsonPayload["source"]["categories"] = [], []
#             jsonPayload["target"]["books"], jsonPayload["source"]["books"] = [], []
#         # j = json.dumps(jsonPayload, indent=4, ensure_ascii=False)
#         # print(j)
                

# def create_links(text):
#     mapping_list =  text['target']['books'][0]['mapping']['linker_pair']
#     commentary_content =  text['target']['books'][0]['content']
#     #title of root text
#     commentary_title = text['source']['categories'][-1]['name']
#     link_type = text['source']['categories'][-1]['link']
#     root_text_title = text['source']['categories'][-1]['base_text_titles'][0]
#     total_link = []
    
#     link_ranges = defaultdict(list)

    

#     #root 1:1 --- commentary 1(book):1(chapter):3-4
#     for i, linkers in enumerate(mapping_list):
#         ref = {}
#         map_list = [] 
#         l = []
        
#         # Collect all values for the same key
#         for k, value in linkers:
#             link_ranges[k].append(value)
#         l = list(link_ranges.values())
#         print(link_ranges.keys())
#         commentary_section = [l[0][0], len(list(link_ranges.values())) + l[0][0]]
#         start_index = start_index = commentary_section[0]

#         for key, values in link_ranges.items():
#             length = 0
#             map_list.append(f'{root_text_title} {i + 1}:{key}')
#             if len(set(values)) > 1:  
#                 length =( max(values) - min(values)) + 1
#                 range_string = [values[0], length]
#                 map_list.append(f'{commentary_title} {i + 1}:{start_index}:1-{range_string[1]}')

#             else:
#                 length = 1
#                 range_string = [values[0], length]  
#                 map_list.append(f'{commentary_title} {i + 1}:{start_index}:{range_string[1]}')
                
#             print(start_index, range_string[1] )

#             start_index +=1
#             ref['refs'] = map_list
#             ref['type'] = link_type.lower()
#             total_link.append(ref)
#             ref = {}
#             map_list = []
        
            
            

#     # for i in range(len(commentary_content)):
#     #     ref = {}
#     #     for j in range(len(commentary_content[i])):
#     #         map_list = []
#     #         total_map = len(commentary_content[i][j])
#     #         map_list.append(f'{root_text_title} {i+1}:{j+1}')
#     #         if(total_map > 1):
#     #             map_list.append(f'{commentary_title} {i+1}:{j+1}:1-{total_map}')
#     #         else: 
#     #             map_list.append(f'{commentary_title} {i+1}:{j+1}:1')
#     #         ref['refs'] = map_list
#     #         ref['type'] = link_type.lower()
#     #         total_link.append(ref)
#     #         ref = {}

#     # create json
#     commentary_title = commentary_title.strip()
#     with open(f'{BASEPATH}/jsondata/refs/{commentary_title.replace(" ", "_")}.json', 'w') as file:
#        json.dump(total_link,file, indent=4, ensure_ascii=False) 




#-----------------------------------commentary link from jsonfile----------------------------------------
     
def commentaryToRoot(textType):
    print(BASEPATH)
    for root, dirs, files in os.walk(f"{BASEPATH}/jsondata/texts/{textType}"):
         for file in files:
            if file.endswith('.json'):
                try:
                    if file.endswith('.json'):
                        with open("{}/jsondata/texts/{}/{}".format(BASEPATH, textType, file), mode='r', encoding='utf-8') as f:
                            data = json.load(f)
                            createLinks(data)
                except Exception as e:
                    print('[Error] opening file: ', e)
                    return
                
#                 
def linkMapper(title, contents, root_detail):
    links = []
    refs = {}
    root_title = root_detail['base_text_titles'][0]
    if get_list_depth(contents) == 1:
        #for dept 1
        range = get_range(contents)
        for value in range.values():
            ref = []
            ref.append(f'{root_title} {value[1][0]}:{value[1][1]}')
            ref.append(f'{title} {value[0]}')
            refs['refs'] = ref
            refs['type'] = 'commentary'
            links.append(refs)
            refs = {}
    else:
        for i, content in enumerate(contents):
            if isinstance(content, list):
                if get_list_depth(content) == 1:
                    # for dept 2
                    range = get_range(content)
                    for value in range.values():
                        ref = []
                        ref.append(f'{root_title} {value[1][0]}:{value[1][1]}')
                        ref.append(f'{title} {i+1}:{value[0]}')
                        refs['refs'] = ref
                        refs['type'] = 'commentary'
                        links.append(refs)
                        refs = {}
                else:
                    for j, data in enumerate(content):
                        if isinstance(data, list):
                            #for dept 3
                            range = get_range(data)
                            for value in range.values():
                                ref = []
                                ref.append(f'{root_title} {value[1][0]}:{value[1][1]}')
                                ref.append(f'{title} {i+1}:{j+1}:{value[0]}')
                                refs['refs'] = ref
                                refs['type'] = 'commentary'
                                links.append(refs)
                                refs = {}   
    if links:
        j = json.dumps(links, indent=4, ensure_ascii=False)
        print(j)
        # create json
        commentary_title = title.strip()
        with open(f'{BASEPATH}/jsondata/refs/{commentary_title[-30:]}.json', 'w') as file:
           json.dump(links,file, indent=4, ensure_ascii=False) 

    
    


        
    
def get_range(data):
    indices = defaultdict(list)
    
    for i, elem in enumerate(data):
         matches = re.search(r"<\d+><\d+>", elem)
         if matches:
            unique_elem = matches.group()
            indices[unique_elem].append(i)

    output = {}
    for key, value in indices.items():
        output[key] = []
        initial_index = value[0]
        final_index = value[-1]
        if initial_index == final_index:
            output[key].append(str(initial_index + 1))
            match = re.findall(r'\d+', key)
            output[key].append( list(map(int, match)))
        else:
            output[key].append(f"{initial_index + 1}-{final_index + 1}")
            match = re.findall(r'\d+', key)
            output[key].append( list(map(int, match)))
        
    return output

def createLinks(data):
    jsonData = data
    book_last_category = jsonData['source']['categories'][-1]

    #check if jsonData is commentary text or not
    if 'link' in book_last_category:

        # English version
        for enbook in jsonData['source']['books']:
            chapters = generate_chapters({}, enbook, enbook['language'])

            for key, value in chapters.items():
                linkMapper(key, value, book_last_category)

        # Tibetan version
        for bobook in jsonData['target']['books']:
            chapters = generate_chapters(bobook, jsonData['source']['books'][0], bobook['language'])
            # j = json.dumps(chapters, indent=4, ensure_ascii=False)
            # print(j)

            for key, value in chapters.items():
                linkMapper(key, value, book_last_category)
        


def generate_chapters(botext, entext, language, current_key="", parent_keys=[]):
    result = {}
    if 'content' in entext:
        if botext:
            bobook = botext['content']
        enbook = entext['content']
    else:
        if botext:
            bobook = botext
        enbook = entext
    
    if isinstance(enbook, dict):
        if not botext:
            for key, value in enbook.items():
                full_key = key if current_key else key
                new_parent_keys = parent_keys + [key.strip()]

                if isinstance(value, dict):
                    # Check if the dictionary has any children other than data
                    has_children = any(sub_key != 'data' for sub_key in value.keys())    
                    child_data = generate_chapters(value, language, full_key, new_parent_keys)
                    result.update(child_data)  # Merge results from children

                        # If there are other children, include data in the key, else exclude it
                    if has_children:
                        if language == 'bo':
                            data_key = ', '.join(new_parent_keys) + ', གོང་གི་ས་བཅད་ཀྱི་ནང་དོན།'
                        else: 
                             data_key = ', '.join(new_parent_keys) + ', data'
                    else:
                        data_key = ', '.join(new_parent_keys)  # Exclude data from the key if no other children
                    result[data_key] = value['data']
        else:
            for (enkey, envalue), (bokey, bovalue) in zip(enbook.items(), bobook.items()):
                full_key = enkey if current_key else enkey
                new_parent_keys = parent_keys + [enkey.strip()]
                if isinstance(envalue, dict):
                    # Check if the dictionary has any children other than data
                    has_children = any(sub_key != 'data' for sub_key in envalue.keys())    
                    child_data = generate_chapters(bovalue, envalue, language, full_key, new_parent_keys)
                    result.update(child_data)  # Merge results from children
                    if has_children:
                        data_key = ', '.join(new_parent_keys) + ', data'
                    else:
                        data_key = ', '.join(new_parent_keys)
                    if language == 'bo':
                        result[data_key] = bovalue['data']
                    else:
                        result[data_key] = envalue['data']

            
    if isinstance(enbook, list):
        result[enbook['title']] = enbook['content']
    
    return result

def get_list_depth(lst):
    """
    Function to calculate the depth of a nested list.
    """
    if not isinstance(lst, list):  # Base case: not a list, no depth
        return 0
    else:
        max_depth = 0
        for item in lst:
            max_depth = max(max_depth, get_list_depth(item))  # Recurse and update max depth
        return max_depth + 1  # Add one to include the current depth level



def main():
    print("------ TXT TO JSON -----")
    #txtToJson()
    commentaryToRoot('baseText')
    commentaryToRoot('commentaryText')
    
main()