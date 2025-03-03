import os

subjects = ["pp2", "discrete math", "english", "sociology"]

f = open("files/2.txt", "w")
f.write(str(subjects))
f.close()

f = open("files/2.txt", "r")
print(f.read())