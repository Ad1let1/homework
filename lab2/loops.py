#while
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#for
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)