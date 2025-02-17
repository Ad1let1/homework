"""An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
Technically, in Python, an iterator is an object which implements 
the iterator protocol, which consist of the methods __iter__() and __next__().

Lists, tuples, dictionaries, and sets are all iterable objects. 
They are iterable containers which you can get an iterator from.
All these objects have a iter() method which is used to get an iterator:

"""

mytuple = ("apple", "banana", "cherry")
s = "Adilet"
myit = iter(mytuple)
myit2 = iter(s)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit2))
print(next(myit2))

for x in mytuple:
    print(x) #The for loop actually creates an iterator object and executes the next() method for each loop.

#example in class
#Create an iterator that returns numbers, starting with 1,
# and each sequence will increase by one (returning 1,2,3,4,5 etc.):
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter)) 

#StopIteration
class MyNumbers2:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if(x <= 20):
            x = self.a
            self.a += 1
            return x
        else: 
            raise StopIteration
myclass2 = MyNumbers2()
myiter2 = iter(myclass2)
for x in myiter2:
    print(x)

