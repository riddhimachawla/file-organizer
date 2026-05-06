# this program looks inside a folder
# checks the files it contains 
# sorts them into subfolders according to their extensions

import os
import shutil

#taking input
folder_path = os.getcwd()

#creating destination folders
images_folder = os.path.join(folder_path,"images")
docs_folder = os.path.join(folder_path,"docs")
code_folder = os.path.join(folder_path,"code")

os.makedirs(images_folder, exist_ok=True)
os.makedirs(docs_folder, exist_ok=True)
os.makedirs(code_folder, exist_ok=True)

#loop for full path
for file in os.listdir(folder_path):
    full_path = os.path.join(folder_path, file) #joining the path and the file name

#checking if full path exists or not
    if os.path.isfile(full_path):
        root, ext = os.path.splitext(file) #splitting the file name into root and extension
        if file == "main.py":
            continue

#loop for sorting
        if ext == ".jpg":
            shutil.move(full_path,images_folder)
        elif ext == ".pdf":
            shutil.move(full_path, docs_folder)
        elif ext == ".py":
            shutil.move(full_path, code_folder)