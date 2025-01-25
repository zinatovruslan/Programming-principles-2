print(10 + 5)

#1
x = 2
y = 5

print(x ** y) #same as 2*2*2*2*2 and result is 32

#2
x = 5
y = 2

print(x % y) #1

#3
x = 15
y = 2

print(x // y) #7

#4
x = 5
y = 3

print(x == y) #False

#5
x = 5
y = 3

print(x != y) #True

#6
x = 5
y = 3

print(x >= y) #True

#7
x = 5
y = 3

print(x <= y) #False

#8
x = 5

print(x > 3 and x < 10) #True

#9
x = 5

print(x > 3 or x < 4) #True

#10
x = 5

print(not(x > 3 and x < 10)) #False

#11
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z) #False
print(x is not y) #True
print(x != y) #False

#12
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) #True
print(x is y) #False
print(x == y) #True

#13
x = ["apple", "banana"]

print("banana" in x) #True

#14
x = ["apple", "banana"]

print("pineapple" not in x) #True

#15
print((6 + 3) - (6 + 3)) #0

#16
print(100 + 5 * 3) #115

#17
print(5 + 4 - 7 + 3) #5
