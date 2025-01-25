#1
fruits = ("apple", "banana", "cherry")
print(fruits) #('apple', 'banana', 'cherry')

#2
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green) #apple
print(yellow) #banana
print(red) #cherry

#3
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green) #apple
print(yellow) #banana
print(red) #['cherry', 'strawberry', 'raspberry']

#4
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green) #apple
print(tropic) #['mango', 'papaya', 'pineapple']
print(red) #cherry
