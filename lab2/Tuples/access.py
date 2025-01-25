#1
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #banana

#2
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) #cherry

#3
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) #('cherry', 'orange', 'kiwi')

#4
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) #('apple', 'banana', 'cherry', 'orange')

#5
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) #('cherry', 'orange', 'kiwi', 'melon', 'mango')

#6
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) #('orange', 'kiwi', 'melon')

#7
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") #Yes, 'apple' is in the fruits tuple
