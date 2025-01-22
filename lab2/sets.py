#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Set items are unordered, unchangeable, and do not allow duplicate values.
thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "banana", True, 1, 2, False, 0}
print(thisset)

#add items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) #{'banana', 'apple', 'cherry', 'orange'}

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) #set1.update(set2)
print(thisset) #{'banana', 'apple', 'cherry', 'mango', 'papaya', 'pineapple'}

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)#set1.update(list1)
print(thisset) #{'banana', 'apple', 'cherry', 'kiwi', 'orange'}

#remove, discard, pop, clear, del

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
thisset.discard("banana")
print(thisset)
# If the item to remove does not exist, remove() will raise an error. But discard() will not.

#pop removes the random item

thisset = {"apple", "banana", "cherry"}
thisset.pop()
print(thisset)
thisset.clear() 
print(thisset)
#del thisset error

#join
#union() - allows you to join a set with other data types, like lists or tuples.
#| - only allows you to join sets with sets
#update() or (|=) -  inserts all items from one set into another.
#changes the original set, and does not return a new set.

x = {"a", "b", "c"}
y = (1, 2, 3)
z = {4, 5, 6}
d = x.union(y) 
e = x | z
print(d)
print(e)

#intersection
#intersection() - keeps only duplicates
#& - only keeps duplicates but only with sets
# intersection_update() (or &=) method will also keep ONLY the duplicates,
# but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3) #{'apple'}
set1.intersection_update(set2)
print(set1) #{'apple'}

#difference
#difference() - returns a set containing the difference between two or more sets.
# '-' is the same but only with sets
#difference_update() (or -=) - removes the items that exist in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3) #{'banana', 'cherry'}

#symmetric_difference() - keep only the elements that are NOT present in both sets.
# ^ is the same but only with sets 
#symmetric_difference_update()(or ^=) - removes the items that are present in both sets, and inserts the other items.
set3 = set1.symmetric_difference(set2)
print(set3) #{'banana', 'cherry', 'google', 'microsoft'}
