import math
import time


def product(numbers):
    return math.prod(numbers)

def cnt(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return {"Uppercase": upper_count, "Lowercase": lower_count}

def is_palindrome(s):
    return s == s[::-1]


def sqr(number, delay_ms):
    time.sleep(delay_ms / 1000)  
    result = math.sqrt(number)
    return result

def all_true(t):
    return all(t)

print(product([1, 2, 3, 4]))  
print(cnt("TEST string")) 
print(is_palindrome("ababa")) 
print(sqr(25100,2123))
print(all_true((True, True, False)))  
