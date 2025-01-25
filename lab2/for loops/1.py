#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
# apple
# banana
# cherry

#2
for x in "banana":
  print(x) 
# b
# a
# n
# a
# n
# a

#3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
# apple
# banana

#4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break 
  print(x) #apple

#5
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 
# apple
# cherry

#6
for x in range(6):
  print(x) 
# 0
# 1
# 2
# 3
# 4
# 5

#7
for x in range(2, 6):
  print(x) 
# 2
# 3
# 4
# 5

#8
for x in range(2, 30, 3):
  print(x) 
# 2
# 5
# 8
# 11
# 14
# 17
# 20
# 23
# 26
# 29

#9
for x in range(6):
  print(x)
else:
  print("Finally finished!")
# 0
# 1
# 2
# 3
# 4
# 5
# Finally finished!

#10
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
# 0
# 1
# 2
#If the loop breaks, the else block is not executed.

#11
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry

#12
for x in [0, 1, 2]:
  pass

# having an empty for loop like this, would raise an error without the pass statement
