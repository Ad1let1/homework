import re

string1 = ["a", "ab", "abb", "bb", "aaa", "abbb"]

proverka = r'ab{2,3}'

for x in string1:
    if re.fullmatch(proverka, x):
        print(f"{x} соответсвует")
    else:
        print(f"{x} несоотвествует")