import re
string = "MyNameIsAibynKbtuFu"
split_string = re.findall('[A-Z][^A-Z]*', string)

print(" ".join(split_string))