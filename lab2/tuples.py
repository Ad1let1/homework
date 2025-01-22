#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

thistuple = ("apple", "banana", "cherry")
print(thistuple) #('apple', 'banana', 'cherry')
#if one item: there must be a ','
thistuple = ("apple",)
print(type(thistuple)) #<class 'tuple'>
thistuple = ("apple")
print(type(thistuple)) #<class 'str'>

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) #('apple', 'kiwi', 'cherry')

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple) #('apple', 'banana', 'cherry', 'orange')

#remove, delete same as the lists

#unpacking
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green) #apple
print(yellow) #banana
print(red) #cherry

#unpacking with *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits #red is a list
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits #tropic is a list and red is cherry
print(green)
print(tropic)
print(red)

#another things same as the list
