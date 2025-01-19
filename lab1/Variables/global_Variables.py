#1
x = "awesome"

def myfunc():
  print("Python is " + x) # Python is awesome

myfunc()

#2
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x) # Python is fantastic

myfunc()

print("Python is " + x) # Python is awesome

#3
def myfunc():
  global x  #If you use the global keyword, the variable belongs to the global scope
  x = "fantastic"

myfunc()

print("Python is " + x) #Python is fantastic

#4
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) #Python is fantastic
