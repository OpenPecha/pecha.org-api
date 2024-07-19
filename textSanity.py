import os
import json

def read_file_lines(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.readlines()

def find_commentary_files(commentary_folder):
    commentary_files = []
    for filename in os.listdir(commentary_folder):
        if filename.endswith('.json'):
            commentary_files.append(os.path.join(commentary_folder, filename))
    return commentary_files

def compare_files(root_folder, commentary_folder):
    commentary_files = find_commentary_files(commentary_folder)
    
    for commentary_file in commentary_files:
        with open(commentary_file, 'r', encoding='utf-8') as file:
            commentary_data = json.load(file)
        
        root_name = commentary_data.get('root_name')
        if not root_name:
            print(f"No root_name found in {commentary_file}")
            continue
        
        root_filepath = os.path.join(root_folder, root_name)
        if not os.path.exists(root_filepath):
            print(f"Root file {root_filepath} does not exist for commentary file {commentary_file}")
            continue

        root_lines = read_file_lines(root_filepath)
        commentary_lines = commentary_data.get('content', '').splitlines()

        for i, (root_line, commentary_line) in enumerate(zip(root_lines, commentary_lines)):
            if root_line.strip() != commentary_line.strip():
                print(f"Root and commentary line not match at line {i+1}")
                print(f"Root line: {root_line.strip()}")
                print(f"Commentary line: {commentary_line.strip()}")
                return root_line.strip()

        # Check if root file has more lines than commentary file
        if len(root_lines) > len(commentary_lines):
            for i in range(len(commentary_lines), len(root_lines)):
                print(f"Root and commentary line not match at line {i+1}")
                print(f"Root line: {root_lines[i].strip()}")
                print(f"Commentary line: (no line)")
                return root_lines[i].strip()
        
        # Check if commentary file has more lines than root file
        if len(commentary_lines) > len(root_lines):
            for i in range(len(root_lines), len(commentary_lines)):
                print(f"Root and commentary line not match at line {i+1}")
                print(f"Root line: (no line)")
                print(f"Commentary line: {commentary_lines[i].strip()}")
                return commentary_lines[i].strip()

    print("All files matched successfully.")
    return None

# Define the root and commentary folders
root_folder = 'root_text'
commentary_folder = 'commentary'

# Run the comparison
compare_files(root_folder, commentary_folder)
