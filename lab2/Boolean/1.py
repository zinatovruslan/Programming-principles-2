print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False

#1
 a = 200
 b = 33
 if b > a:
   print("b is greater than a")
 else:
   print("b is not greater than a")

print(bool("Hello")) #True
print(bool(15)) #True

#2
x = "Hello"
y = 15

print(bool(x)) #True
print(bool(y)) #True

print(bool("abc")) #True
print(bool(123)) #True
print(bool(["apple", "cherry", "banana"])) #True

bool(False) #False
bool(None) #False
bool(0) #False
bool("") #False
bool(()) #False
bool([]) #False
bool({}) #False

#3
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) #False

#4
def myFunction() :
  return True

print(myFunction()) #True

#5
def myFunction() :
  return True

if myFunction():
  print("YES!") #YES because function returns True
else:
  print("NO!")

#6
x = 200
print(isinstance(x, int)) #True
