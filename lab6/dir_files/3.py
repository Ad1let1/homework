import os

def check_path(path):
    if os.path.exists(path):
        print("Exists")
        directory = os.path.dirname(path)
        filename = os.path.basename(path)
        print("Directory:", directory)
        print("Filename:", filename)
    else:
        print("Doesn't exist")
    
   
path = "files/1.txt"
check_path(path)