import os

path = "./"
file_folder = os.listdir(directory) #oslistdir usado para entrar em pastas
print(file_folder)

# for files in file_folder:
#     complete_path = (os.path.join(directory, files))
#     #if os.path.isfile(complete_path): isfile used to open and navigate for files
#     if os.path.isdir(complete_path):
#         print(f"Checking Folder {files}")
#         print(os.listdir(files))
    
for folders in file_folder:
    complete_path = (os.path.join(directory, folders))
    if os.path.isfile(complete_path):
        print(f"Checking the correct path that contains files in {file_folder}")
        print(files)
    
#result
#only shows the archives or files
#modulo_os.py
