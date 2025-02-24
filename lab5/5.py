import re

string1 = "This is a sample text with ab at the end."


proverka = r'a.*?b$'

x = re.findall(proverka, string1)

for y in x:
    print("Match found:",y)