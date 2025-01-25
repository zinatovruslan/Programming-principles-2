#1
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) #['banana', 'kiwi', 'mango', 'orange', 'pineapple']

#2
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) #[23, 50, 65, 82, 100]

#3
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) #['pineapple', 'orange', 'mango', 'kiwi', 'banana']

#4
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) #[100, 82, 65, 50, 23]

#5
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) #[50, 65, 23, 82, 100]

#6
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) #['Kiwi', 'Orange', 'banana', 'cherry']

#7
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) #['banana', 'cherry', 'Kiwi', 'Orange']

#8
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) #['cherry', 'Kiwi', 'Orange', 'banana']
