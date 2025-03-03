import os

def delete(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print("Deleted")
    else:
        print("Doesn't exist")

path = "files/3.txt"
delete(path)