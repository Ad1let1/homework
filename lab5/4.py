import re

string1 = "Alternating caps, also known as studly Caps or Sticky caps."

proverka = r'[A-Z][a-z]+'


sequence = re.findall(proverka, string1)


print("Нашлось:")
for x in sequence:
    print(x)