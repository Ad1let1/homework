import os

def check_access(path):
    print("Checking access: ", path)
    
    if(os.path.exists(path)):
        print("Exists")
    else:
        print("Doesn't exist")
    
    if(os.access(path, os.R_OK)):
        print("Readable")
    else:
        print("Not readable")
    
    if(os.access(path, os.W_OK)):
        print("Writable")
    else:
        print("Not writable")
    
    if(os.access(path, os.X_OK)):
        print("Executable")
    else:
        print("Not executable")


path = "files/1.txt"
check_access(path)