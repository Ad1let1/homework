
class MyClass:
    def getString ():
        s = input("Enter a string: ")
        return s
    def printString(s):
        print(s.upper())
a = MyClass.getString()
MyClass.printString(a)
