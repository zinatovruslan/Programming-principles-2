#1
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 
# apple
# banana
# cherry

#2
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i]) 
# apple
# banana
# cherry

#3
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i]) 
  i = i + 1
# apple
# banana
# cherry

#4
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] 
# apple
# banana
# cherry
