# Task 1
class StringHandler:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Enter a string: ")

    def printString(self):
        print(self.s.upper())

# Example Usage
# handler = StringHandler()
# handler.getString()
# handler.printString()

# Task 2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

# Example Usage
# square = Square(4)
# print(square.area())

# Task 3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example Usage
# rect = Rectangle(4, 5)
# print(rect.area())

# Task 4
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# Example Usage
# p1 = Point(1, 2)
# p2 = Point(4, 6)
# p1.show()
# p2.show()
# print(p1.dist(p2))

# Task 5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}. New balance: ${self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds. Current balance: ${self.balance}.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}.")

# Example Usage
# acc = Account("John Doe", 100)
# acc.deposit(50)
# acc.withdraw(30)
# acc.withdraw(150)

# Task 6
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)
