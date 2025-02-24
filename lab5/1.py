import re

string = ["a", "ab", "abb", "bb", "aaa"]

proverka = r'ab*'

for x in string:
    if re.fullmatch(proverka, x):
        print(f"{x} соответсвует")
    else:
        print(f"{x} несоотвествует")