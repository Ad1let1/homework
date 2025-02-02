def solve(numheads, numlegs):
    y = int((numlegs - 2*numheads) / 2)
    x = numheads - y
    return x, y
a = int(input("Number of heads: "))
b = int(input("Number of legs: "))
print(solve(a, b))