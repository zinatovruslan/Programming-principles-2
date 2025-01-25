#1
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) #['apple', 'banana', 'cherry', 'orange']

#2
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) #['apple', 'orange', 'banana', 'cherry']

#3
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) #['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

#4
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) #['apple', 'banana', 'cherry', 'kiwi', 'orange']
