#1
import math
 
def square(n, N):
    for i in range(n, N):
        yield i**2
 
n = int(input("Enter the init_number: "))
N = int(input("Enter the N: "))
s = square(n, N)
 
for i in s:
    print(i)
 
#2
def even(n):
    for i in range(1, n):
        if i % 2 == 0:
            yield i
 
n = int(input("Enter the number: "))
s = even(n)
k = []
 
for d in s:
    k.append(d)
print(k, sep=",")
 
#3
def div(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
 
n = int(input("Enter the number: "))
s = div(n)
k = []
 
for d in s:
    print(d)
 
#4
import math
 
def squares(a, b):
    for i in range(a, b+1):
        yield i**2
 
n = int(input("Enter the a: "))
N = int(input("Enter the b: "))
s = squares(n, N)
 
for i in s:
    print(i)
 
#5
def minus(n):
    for i in range(n, -1, -1):
        yield i
 
n = int(input("Enter the number: "))
s = minus(n)
 
for i in s:
    print(i)
