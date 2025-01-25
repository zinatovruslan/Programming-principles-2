#1
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) #("apple", "kiwi", "cherry")

#2
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple) #('apple', 'banana', 'cherry', 'orange')

#3
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple) #('apple', 'banana', 'cherry', 'orange')

#4
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple) #('banana', 'cherry')

#5
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
