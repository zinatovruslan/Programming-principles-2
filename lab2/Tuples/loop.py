#1
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x) 
# apple
# banana
# cherry

#2
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
# apple
# banana
# cherry

#3
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
# apple
# banana
# cherry
