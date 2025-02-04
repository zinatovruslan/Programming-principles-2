#Task 1
def grams_to_ounces(grams):
    return 28.3495231 * grams

grams = 100
print(grams_to_ounces(grams))  # Ожидаемый вывод: 2834.95231

#Task 2
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

fahrenheit_temp = 68
print(fahrenheit_to_celsius(fahrenheit_temp))  # Output: 20.0

#Task 3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None  

num_heads = 35
num_legs = 94
print(solve(num_heads, num_legs))  # Output: (23, 12)

#Task 4
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(filter_prime(numbers))  # Output: [2, 3, 5, 7]

#Task 5
import itertools

def print_permutations():
    s = input("Enter a string: ")
    permutations = itertools.permutations(s)
    for p in permutations:
        print(''.join(p))

print_permutations()
# Enter a string: abc
# abc
# acb
# bac
# bca
# cab
# cba

#Task 6
def reverse_words():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

print(reverse_words())
# Enter a sentence: We are ready
# ready are We

#Task 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3])) #True
print(has_33([1, 3, 1, 3])) #False
print(has_33([3, 1, 3])) #False

#Task 8
def spy_game(nums):
    code = [0, 0, 7]
    idx = 0
    for num in nums:
        if num == code[idx]:
            idx += 1
        if idx == 3:
            return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False

#Task 9
def sphere_volume(radius):
    return (4/3) * 3.14 * radius**3

print(sphere_volume(3))  # Output: 113.04

#Task 10
def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

print(unique_elements([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]

#Task 11
def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Removing spaces and converting to lowercase
    return s == s[::-1]  # Check if string is equal to its reverse

print(is_palindrome("madam"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("A man a plan a canal Panama"))  # True

#Task 12
def histogram(lst):
    for num in lst:
        print('*' * num)

histogram([4, 9, 7])  # Output:
# ****
# *********
# *******

#Task 13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    number = random.randint(1, 20)
    print("Well, " + name + ", I am thinking of a number between 1 and 20.")

    guesses_taken = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1
        
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print("Good job, " + name + "! You guessed my number in " + str(guesses_taken) + " guesses!")
            break

guess_the_number()


