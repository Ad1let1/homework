import re
string = "MyNameIsAibynKbtuFu"
split_string = re.findall('[A-Z][^A-Z]*', string)

print((split_string))