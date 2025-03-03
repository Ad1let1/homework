import os


path = "files"

def list_directories(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

def list_files(path):
    print("Files:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

def list_all(path):
    print("All:")
    for item in os.listdir(path):
        print(item)

path = input("Enter the path: ")
if os.path.exists(path):
    list_directories(path)
    list_files(path)
    list_all(path)
else:
    print("Path does not exist.")

