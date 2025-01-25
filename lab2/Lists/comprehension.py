fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

#1
for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) #['apple', 'banana', 'mango']

#2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) #['apple', 'banana', 'mango']

#3
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist) #['banana', 'cherry', 'kiwi', 'mango']

#4
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist) #['apple', 'banana', 'cherry', 'kiwi', 'mango']

#5
newlist = [x for x in range(10)]
print(newlist) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#6
newlist = [x for x in range(10) if x < 5]
print(newlist) #[0, 1, 2, 3, 4]

#7
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist) #['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

#8
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist) #['hello', 'hello', 'hello', 'hello', 'hello']

#9
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist) #['apple', 'orange', 'cherry', 'kiwi', 'mango']
