snake_case = "I_believe_that_it_is_snake_case_string"


string = snake_case.split('_')

camel_case = string[0]

for x in string[1:]:
    camel_case += x.capitalize()

print(camel_case)