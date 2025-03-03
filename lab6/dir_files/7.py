
path1 = 'files/2.txt'
path2 = 'files/3.txt'

f1 = open(path1, 'r')
f2 = open(path2, 'w')
content = f1.read()
f2.write(content)

f1.close()
f2.close()

f2 = open(path2, 'r')
print(f2.read())
f2.close()