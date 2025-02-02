import math
def filter_prime(lst):
    ans = {}
    for el in lst:
        f = True
        for i in range(2, int(math.sqrt(el)) + 1):
            if(el % i == 0):
                f = False
                break
                
        if(f == True): ans.add(el)
    return ans

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

a = filter_prime(mylist)
print(a)