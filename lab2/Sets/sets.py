#1
thisset = {"apple", "banana", "cherry"}
print(thisset) #{'apple', 'cherry', 'banana'}

#2
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) #{'banana', 'cherry', 'apple'}

#3
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset) #{True, 2, 'banana', 'cherry', 'apple'}

#4
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset) #{False, True, 'cherry', 'apple', 'banana'}

#5
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) #3

#6
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1) #{'cherry', 'apple', 'banana'}
print(set2) #{1, 3, 5, 7, 9}
print(set3) #{False, True}

#7
set1 = {"abc", 34, True, 40, "male"}
print(set1) #{True, 34, 40, 'male', 'abc'}

#8
myset = {"apple", "banana", "cherry"}
print(type(myset)) #<class 'set'>

#9
thisset = set(("apple", "banana", "cherry"))
print(thisset) #{'cherry', 'apple', 'banana'}
# Note: the set list is unordered, so the result will display the items in a random order.
