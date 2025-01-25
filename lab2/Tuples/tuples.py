#1
thistuple = ("apple", "banana", "cherry")
print(thistuple) #('apple', 'banana', 'cherry')

#2
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) #('apple', 'banana', 'cherry', 'apple', 'cherry')

#3
thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple)) #3

#4
thistuple = ("apple",)
print(type(thistuple)) #<class 'tuple'>

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) #<class 'str'>

#5
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1) #('apple', 'banana', 'cherry')
print(tuple2) #(1, 5, 7, 9, 3)
print(tuple3) #(True, False, False)

#6
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1) #('abc', 34, True, 40, 'male')

#7
mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) #<class 'tuple'>

#8
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple) #('apple', 'banana', 'cherry')
