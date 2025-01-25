#1
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) #{'apple', 'cherry'}

#2
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) #{'apple', 'cherry'}

#3
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item -- cherry
print(thisset) #the set after removal -- {'apple', 'banana'}

#4
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) #set()

#5
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #this will raise an error because the set no longer exists
