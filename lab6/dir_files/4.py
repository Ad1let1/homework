import os

def count_lines(path):
    if os.path.exists(path):
        f = open(path, "r")
        lines = f.readlines()
        f.close()
        return len(lines)
    else:
        return -1

path = "files/1.txt"
print(count_lines(path))