import re

camel_case = "IAmAibynSagimovKbtu"

snake_case = '_'.join(re.findall(r'[A-Z][a-z0-9]*', camel_case)).lower()

print(snake_case)