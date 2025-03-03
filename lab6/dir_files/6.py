import os


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for arip in alphabet:
    filename = arip + ".txt"
    file = open(filename, "w")
    file.write("")  
    file.close()

