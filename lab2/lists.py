'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members. 
'''
# A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]
print(list1) #['abc', 34, True, 40, 'male']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #['cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[:2]) #['apple', 'banana']
thislist.insert(2, "watermelon")
print(thislist) # ['apple', 'banana', 'watermelon', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
thislist.append("orange")
print(thislist) #['apple', 'banana', 'watermelon', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'orange']
thislist.remove("banana")
print(thislist) #['apple', 'watermelon', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'orange']

#extend
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) #['apple', 'banana', 'cherry', 'kiwi', 'orange']

#remove
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) #remove the first of banana ['apple', 'cherry', 'banana', 'kiwi']

#pop
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #['apple', 'cherry']
#del
del thislist[0]
print(thislist) #['cherry']

thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist) #this will cause an error because you have succsesfully deleted "thislist".

#clear
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #[]

#using loops: 
#1 print each el by loop
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] #apple banana cherry

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x] 
#newlist = [expression for item in iterable if condition == True]
#same with this:
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
print(newlist) #['apple', 'banana', 'mango']

#sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) #['banana', 'kiwi', 'mango', 'orange', 'pineapple'] 
thislist.sort(reverse = True) #or thislist.reverse()
print(thislist) #['pineapple', 'orange', 'mango', 'kiwi', 'banana']

#costumize sort like comparator
def myfunc(n): #sort by distance from 50
  return abs(n - 50) 
thislist = [100, 50, 65, 82, 23] #50 0 15 32 27
thislist.sort(key = myfunc)
print(thislist) #[50, 65, 23, 82, 100]
#lowercase sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower) #by default it is the upper
print(thislist) #['banana', 'cherry', 'Kiwi', 'Orange']

#copy
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
mylist = list(thislist)
mylist = thislist[:] #all are same
print(mylist) #['apple', 'banana', 'cherry']

#join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) #['a', 'b', 'c', 1, 2, 3]
list1.extend(list2)
print(list1) #['a', 'b', 'c', 1, 2, 3]
