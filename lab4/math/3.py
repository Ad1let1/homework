import math

def degtorad(deg):
    return deg*(math.pi/180)

n = int(input("Input number of sides: "))
a = int(input("Input the length of a side: "))
apothem = a/(2*math.tan(degtorad(180/n)))
print("The area of the polygon is: ", n*a*apothem/2)