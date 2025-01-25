#1
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y) 
print(z) #True

#2
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x <= y
print(z) #True

#3
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y) 
print(z) #False

#3
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y) 
print(x) #{'microsoft', 'cherry', 'banana', 'google'}

#4
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x ^= y
print(x) #{'microsoft', 'banana', 'cherry', 'google'}
