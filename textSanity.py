import os
import yaml
import json
import re

BASEPATH = os.path.dirname(os.path.abspath(__file__))

def read_file_lines(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.readlines()
    

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
                                if (para):
                                    if((i + 1)%2 != 0):
                                        commentary.append([i+1, para])
                                
                            commentary_file[f'{root_title}-{commentary_title}'] = commentary  
    commentaries_index_data.append(commentary_file)
                               
    return commentaries_index_data 



def find_root_files(filepath, root_title):
    root_content = []
    isRootMatch = False
    for root, dirs, files in os.walk(filepath):
        for dir in dirs:
            for subroot, subdirs, subfiles in os.walk(f'{root}/{dir}'):
                for file in subfiles:
                    if(file.endswith('.yaml')):
                        with open(f'{subroot}/meta.yaml', 'r') as file:
                            yamlCategories = (yaml.safe_load(file))
                        bookCat = yamlCategories['categories'][-1]
                        if bookCat['enName'] == root_title:
                            isRootMatch = True
                    elif (file.endswith('.md')):
                        with open(f'{subroot}/{file}', mode='r', encoding='utf-8') as f:
                            text = f.read()
                            paragraphs = text.split('\n')
                            for i, para in enumerate(paragraphs):
                                para = para.strip()
                                if (para):
                                    if((i + 1)%2 != 0):
                                        root_content.append([i+1, para])
    return root_content

def match(root_data, commentary_data, root_title, commentary_title):
    result = {}
    errorMessageList = []
    for i , rootline in enumerate(root_data):
        pass
    for i, line in enumerate(commentary_data):
        print(line)
        if(line[0] == root_data[i][0]):
            print(line[0] ,">>>>>>>>>>>>>>>>>>",  root_data[i][0])    
        else: 
            print(line[0] ,"-----------------",  root_data[i][0])               

def compare_files(root_folder, commentary_folder):
    root_title = ""
    root_titles = []
    commentary_title = ""
    commentary_files = find_commentary_files(BASEPATH+commentary_folder)
    # j = json.dumps(commentary_files, indent=4, ensure_ascii=False) 
    # print(j)
    root_data = []
    commentary_data = []
    for commentary_file in commentary_files:
        for (key, values) in commentary_file.items():
            commentary_data = values
            result = re.search(r'^(.*?)-(.*)', key)
            # Check if there's a match and retrieve the desired substrings
            root_title = result.group(1).strip()
            commentary_title = result.group(2).strip()
            if root_title not in root_titles:
                root_data = find_root_files(BASEPATH+root_folder, root_title)
            data = match(root_data, commentary_data, root_title, commentary_title )
            root_titles.append(root_title)

    #     root_filepath = os.path.join(root_folder, root_name)
    #     if not os.path.exists(root_filepath):
    #         print(f"Root file {root_filepath} does not exist for commentary file {commentary_file}")
    #         continue

    #     root_lines = read_file_lines(root_filepath)
    #     commentary_lines = commentary_content.splitlines()

    #     for i, (root_line, commentary_line) in enumerate(zip(root_lines, commentary_lines)):
    #         if root_line.strip() != commentary_line.strip():
    #             print(f"Root and commentary line not match at line {i+1}")
    #             print(f"Root line: {root_line.strip()}")
    #             print(f"Commentary line: {commentary_line.strip()}")
    #             return root_line.strip()

    #     # Check if root file has more lines than commentary file
    #     if len(root_lines) > len(commentary_lines):
    #         for i in range(len(commentary_lines), len(root_lines)):
    #             print(f"Root and commentary line not match at line {i+1}")
    #             print(f"Root line: {root_lines[i].strip()}")
    #             print(f"Commentary line: (no line)")
    #             return root_lines[i].strip()
        
    #     # Check if commentary file has more lines than root file
    #     if len(commentary_lines) > len(root_lines):
    #         for i in range(len(root_lines), len(commentary_lines)):
    #             print(f"Root and commentary line not match at line {i+1}")
    #             print(f"Root line: (no line)")
    #             print(f"Commentary line: {commentary_lines[i].strip()}")
    #             return commentary_lines[i].strip()

    # print("All files matched successfully.")
    # return None




def main():

    # Define the root and commentary folders
    root_folder = '/sources/root_texts'
    commentary_folder = '/sources/commentaries'

    # Run the comparison
    compare_files(root_folder, commentary_folder)


main()