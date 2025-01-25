#1
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) #{1, 'a', 'c', 2, 'b', 3}

#2
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3) #{2, 3, 1, 'c', 'a', 'b'}

#3
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset) #{Elena, 'b', 2, 'a', apple, 'c', banana, 1, 3, John, cherry}

#4
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset) #{Elena, 'c', banana, John, cherry, 1, 'a', 3, 2, apple, 'b'}

#5
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z) #{3, 'b', 'c', 'a', 2, 1}

#6
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1) #{3, 1, 'c', 'a', 2, 'b'}

#7
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3) #{'apple'}

#8
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3) #{'apple'}

#9
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)
print(set1) #{'apple'}

#10
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", "microsoft", "apple", True}

set3 = set1.intersection(set2)
print(set3) #{False, True, 'apple'}

#11
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3) #{'banana', 'cherry'}

#12
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3) #{'banana', 'cherry'}

#13
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set1) #{'banana', 'cherry'}

#14
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3) #{'google', 'banana', 'microsoft', 'cherry'}

#15
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2

print(set3) #{'google', 'banana', 'microsoft', 'cherry'}

#16
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)
print(set1) #{'google', 'banana', 'microsoft', 'cherry'}
