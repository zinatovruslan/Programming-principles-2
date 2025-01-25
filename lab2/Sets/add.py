#1
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset) #{'cherry', 'orange', 'apple', 'banana'}

#2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset) #{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

#3
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset) #{'banana', 'cherry', 'apple', 'orange', 'kiwi'}
