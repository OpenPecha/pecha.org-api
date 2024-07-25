import os
import yaml
import json
import re

BASEPATH = os.path.dirname(os.path.abspath(__file__))

def createMessageFile(is_success, message, com_title, root_title):

    if is_success:
        with open(f'{BASEPATH}/sanityMessage/success--{com_title}.json', 'w') as file:
            json.dump([f'{root_title} matched with {com_title}'],file, indent=4, ensure_ascii=False) 
    else:
        with open(f'{BASEPATH}/sanityMessage/failed--{com_title}.json', 'w') as file:
            json.dump(message,file, indent=4, ensure_ascii=False) 
        print("hello")
    

def find_commentary_files(commentary_folder):
    commentaries_index_data= []
    commentary_file = {}
    root_title = ""
    root_titles = []
    commentary_title = ""
    for root, dirs, files in os.walk(commentary_folder):
        for dir in dirs:
            for subroot, subdirs, subfiles in os.walk(f'{root}/{dir}'):
                for file in subfiles:
                    commentary = []
                    if(file.endswith('.yaml')):
                        with open(f'{subroot}/meta.yaml', 'r') as file:
                            yamlCategories = (yaml.safe_load(file))
                            bookCat = yamlCategories['categories'][-1]
                            commentary_title = yamlCategories['categories'][-1]['enName']
                        if(bookCat['base_text_titles']):
                            root_title = bookCat['base_text_titles'][0]
                            if root_title not in root_titles:
                                root_titles.append(root_title)
                    elif(file.endswith('.md')):
                        with open(f'{subroot}/{file}', mode='r', encoding='utf-8') as f:
                            text = f.read()
                            paragraphs = text.split('\n')
                            for i, para in enumerate(paragraphs):
                                para = para.strip()
                               
                                # if((i + 1)%2 != 0):
                                commentary.append([i+1, para])
                                
                            commentary_file[f'{root_title}-{commentary_title}'] = commentary  
    commentaries_index_data.append(commentary_file)
                               
    return commentaries_index_data 



def find_root_files(filepath, root_title):
    root_content = []
    for root, dirs, files in os.walk(filepath):
        for dir in dirs:
            for subroot, subdirs, subfiles in os.walk(f'{root}/{dir}'):
                for file in subfiles:
                    if(file.endswith('.yaml')):
                        with open(f'{subroot}/meta.yaml', 'r') as file:
                            yamlCategories = (yaml.safe_load(file))
                        bookCat = yamlCategories['categories'][-1]
                    elif (file.endswith('.md')):
                        with open(f'{subroot}/{file}', mode='r', encoding='utf-8') as f:
                            text = f.read()
                            paragraphs = text.split('\n')
                            for i, para in enumerate(paragraphs):
                                para = para.strip()
                                # if((i + 1)%2 != 0):
                                root_content.append([i+1, para])
    return root_content

def match(root_data, commentary_data, root_title, commentary_title):
    messageList = []
    message = {}
    rootline = []
    success = True
    print(commentary_data)
    for i, line in enumerate(commentary_data):
        #find mismatch line
        if(line[0]%2 == 0 and line[1]):
            success = False
            message[f'{commentary_title}  {line[0]}'] = f'line no: {line[0]} of Commentary<`{commentary_title}`> does not match with Root: <`{root_title}`>'
            messageList.append(message)
    return success, messageList      

def compare_files(root_folder, commentary_folder):
    root_title = ""
    root_titles = []
    commentary_title = ""
    commentary_files = find_commentary_files(BASEPATH+commentary_folder)
    # j = json.dumps(commentary_files, indent=4, ensure_ascii=False) 
    # print(j)
    root_data = []
    commentary_data = []
    is_matched_commentaries = []
    for commentary_file in commentary_files:
        for (key, values) in commentary_file.items():
            commentary_data = values
            result = re.search(r'^(.*?)-(.*)', key)
            # Check if there's a match and retrieve the desired substrings
            root_title = result.group(1).strip()
            commentary_title = result.group(2).strip()
            
            if root_title not in root_titles: #avoid fetching same root text content
                root_data = find_root_files(BASEPATH+root_folder, root_title)
            success, messageList = match(root_data, commentary_data, root_title, commentary_title )
            #crete failed and success file 
            if commentary_title not in is_matched_commentaries:
                createMessageFile(success, messageList, commentary_title, root_title)
                is_matched_commentaries.append(commentary_title)
            root_titles.append(root_title)

   

def main():

    # Define the root and commentary folders
    root_folder = '/sources/root_texts'
    commentary_folder = '/sources/commentaries'

    # Run the comparison
    compare_files(root_folder, commentary_folder)


main()