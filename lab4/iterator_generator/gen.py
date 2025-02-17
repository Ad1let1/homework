"""
Пример использования генераторов
"""

def example_generator():
    for i in range(5):
        yield i ** 2

# Демонстрация:
mygen = example_generator()
print(next(mygen))
print(next(mygen))

for val in mygen:
    print(val)
