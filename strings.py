#Strings
print("I'm a dog")
str1="hihello"
mystr='abcdefg'
print(mystr)

#indexing
print(mystr[0])
print(mystr[(len(mystr)-1)//2]) #prints midle char from str

#Slicing
print(mystr[4::])

#Basic methods
print(mystr.upper())
print(mystr.lower())
print(mystr.capitalize())
print(mystr.join(str1))
print(mystr.count("s"))
print(mystr.split())

#printformating
x="Insert another thing here: {}".format("Inserted Me!")
print(x)

y="Item one: {} Item two: {}".format("dog","cat")
print(y)

z="Item one: {y} Item two: {x}".format(x="dog",y="cat")
print(z)