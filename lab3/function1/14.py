def gramToOunce(grams):
    return grams * 28.3495231
def f_to_c(f):
    return (f - 32) * 5 / 9

def volume(r):
    return (4/3) * 3.14 * r**3

a = int(input("Fahrenheit: "))
print(f_to_c(a))
b = int(input("Grams: "))
print(gramToOunce(b))
x = int(input("Radius: "))
print(volume(x))