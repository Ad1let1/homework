#Home
print("Hello, world!")

#Correct Syntax 
if 5 > 2:
  print("Five is greater than two!")
if 5 > 2:
        print("Five is greater than two!") 

#Basic Comment
"""
Big comment
qwerty
"""

#Variables
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(type(x), type(y), type(z))


#Variable Names
#legal:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
""" illegal:
2myvar = "John"
my-var = "John"
my var = "John"
"""
#Multiple Values
a = b = c = "Orange"
print(a)
print(b)
print(c)

#Output Variables
x = 5
y = "John"
print(x, y) #print separeted by space

#Global Variables
x = "awesome"
def myfunc():
  global x #to change global variable inside function
  x = "fantastic"
myfunc()
print("Python is " + x)

#Data Types
x = "Hello World"	#str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"] #list	
x = ("apple", "banana", "cherry") #tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36} #dict	
x = {"apple", "banana", "cherry"} #set	
x = frozenset({"apple", "banana", "cherry"}) #frozenset	
x = True #bool	
x = b"Hello" #bytes	
x = bytearray(5) #bytearray	
x = memoryview(bytes(5)) #memoryview	
x = None #NoneType
print(type(x))

#Casting
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x, y, z)

#Strings
txt = "The best things in life are free!"
print("free" in txt) #check if free is in txt

#string slicing
b = "Hello, World!"
print(b[:5]) #Hello
print(b[::5]) #H,Wd

#modify string
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
print(a.replace("H", "J")) # returns Jello, World!

#String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#String Format
price = 59
txt = f"The price is {price} dollars" #no decimal places
print(txt)
txt = f"The price is {price:.2f} dollars" #2 decimal places
print(txt)

#Excape Character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
r"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
"""

#string method
"""
capitalize()	Converts the first character to upper case
isdigit()	Returns True if all characters in the string are digits
"""