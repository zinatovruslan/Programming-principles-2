#1
import math

a = [1, 2, 3, 4, 5, 6]
result = math.prod(a)
print(result)
# Output
# 720

#2
def letters(s):
    sumUpper = 0
    sumlower = 0
    for char in s:
        if char.islower():
            sumlower += 1
        elif char.isupper():
            sumUpper += 1
    return sumUpper, sumlower

s = ("Python PRogram 12")
upper, lower = letters(s)
print("upper numbers: ", upper, "and\n", "lower numbers: ", lower)
# Output
# upper numbers:  3 and
#  lower numbers:  10

#3
 def palindrome(s):
    a = ''.join(filter(str.isalnum,s.lower()))
    if a == a[::-1]:
        return "it is a Palindrome"
    else:
        return "it is not a Palindrome"
 s = input("Enter the string: ")
# print(palindrome(s))
# Output
# Enter the string: ana
# it is a Palindrome

#4
import time
import math

def invoke_square(a, b):
    time.sleep(b/ 1000)
    return math.sqrt(a)

n1 = int(input("Input the 1st number: "))
n2 = int(input("Input the 2nd number: "))
result = invoke_square(n1, n2)
print(f"Square root of {n1} after {n2} milliseconds is {result}")
# Output
# Input the 1st number: 12155
# Input the 2nd number: 85
# Square root of 12155 after 85 milliseconds is 110.24971655292362

#5
def convert(v):
    if v.isdigit():
        return int(v)
    elif v.lower() == "false":
        return False
    elif v.lower() == "true":  
        return True  
    else:
        return v

def true(a):
    return all(a)

a = tuple(map(convert, input("Enter elements: ").split()))
print(true(a))
# Output
# Enter elements: football 1 5 hello
# True
