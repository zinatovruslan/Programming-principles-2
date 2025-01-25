#1
a = 33
b = 200

if b > a:
  print("b is greater than a") #b is greater than a

#2
a = 33
b = 200

if b > a:
print("b is greater than a") #it is error because of no indentation was done

#3
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal") #this will be output

#4
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b") #this will be output

#5
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") #this will be output

#6
a = 200
b = 33

if a > b: print("a is greater than b") #this how we can write

#7
a = 2
b = 330

print("A") if a > b else print("B") #B

#8
a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B") #=

#9
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True") #Both conditions are True

#10
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True") #this is true

#11
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b") #this is true

#12
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!") #this is true
  else:
    print("but not above 20.")
# Above ten,
# and also above 20!

#13
a = 33
b = 200

if b > a:
  pass

# having an empty if statement like this, would raise an error without the pass statement
