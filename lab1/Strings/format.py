age = 36
txt = "My name is John, I am " + age
print(txt) 
#Traceback (most recent call last):
  File "demo_string_format_error.py", line 2, in <module>
    txt = "My name is John, I am " + age
TypeError: must be str, not int

age = 36
txt = f"My name is John, I am {age}"
print(txt) #My name is John, I am 36

price = 59
txt = f"The price is {price} dollars"
print(txt) #The price is 59 dollars

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) #The price is 59.00 dollars

txt = f"The price is {20 * 59} dollars"
print(txt) #The price is 1180 dollars
