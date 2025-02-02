def check(x):
    for i in range(2, x):
        if(x % 2 == 0):
            return False
    return True

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

print(list(filter(lambda ai: check(ai), mylist)))