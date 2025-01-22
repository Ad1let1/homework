# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# As of Python version 3.7, dictionaries are ordered. This means that they have a defined order, and that will not change.
# In Python 3.6 and earlier, dictionaries are unordered.

# Access Items

car = {
  #key: value
  "brand": "Ford",
  "model": "Mustang",
  "year": 1954,
  "year": 1964 #duplicate key
}
x = car["year"]
y = car.get("model")
print(x) #1964
print(y) #Mustang

#keys
x = car.keys()
print(x) #dict_keys(['brand', 'model', 'year'])
car["color"] = "white"
print(x) #dict_keys(['brand', 'model', 'year', 'color'])

#values
x = car.values()
print(x) #dict_values(['Ford', 'Mustang', 1964, 'white'])

#items
x = car.items() #tuples in list
print(x) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'white')])

#change values
car["year"] = 2020
print(car["year"]) #2020
car.update({"year": 2020}) #same result and can be used as adding
print(car["year"]) #2020

car["type"] = "mechanic" 
car.update({"type": "mechanic"}) 
print(car)

#remove 
car.pop("model")
print(car) #remove model
car.popitem() #remove last item
print(car) #remove type
del car["brand"]
print(car) #remove brand
car.clear() #remove all items
print(car) #remove all items

#loop
#for x in car.values(), keys(), items():
 # print(x)

#copy
mydict = car.copy()
mydict = dict(car)

#nested dictionary
myfamily = { #like dictionary in dictionary
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"]) #Tobias 
for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])
'''
child1
name: Emil
year: 2004
child2
name: Tobias
year: 2007
child3
name: Linus
year: 2011
'''

#for loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)