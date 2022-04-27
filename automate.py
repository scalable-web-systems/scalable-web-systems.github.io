import json 
import subprocess
import re
import os

BASE_URL = "https://github.com/scalable-web-systems/"
f = open('config.json')
 
data = json.load(f)

exceptions = ['README.md']

# Helper Function to get file names in a directory
def get_file_names(dir):
    
    files = os.listdir(dir)
    file_names = []

    for file in files:
        if '.md' in file and file not in exceptions:
            file_names.append(file)
    return file_names

def get_matching_dir(num):
    folders = os.listdir("docs")
    for folder in folders:
        if str(num) in folder:
            return folder

for repo_name in data['repos']:
    print(repo_name)
    subprocess.run(["git", "clone", BASE_URL+repo_name])

    file_names = get_file_names(repo_name)
    for file_name in file_names:
        print(file_name)
        file_dir = repo_name + "/" + file_name
        with open(file_dir, 'r') as f:
            text = f.read()
            first_line = text.split('\n')[0]
            to_folder_name = get_matching_dir(int(re.search(r'\d+', first_line).group()))
            move_to = "docs" + "/" + to_folder_name
            subprocess.run(['mv', file_dir, move_to])
    
    subprocess.run(["rm", "-rf", repo_name])


    
