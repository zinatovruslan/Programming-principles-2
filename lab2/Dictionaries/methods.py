#fromkeys
#1
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)


print(thisdict) #{'key1': 0, 'key2': 0, 'key3': 0}

#2
x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict) #{'key1': None, 'key2': None, 'key3': None}

#items
#1
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

#2
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

car["year"] = 2018

print(x) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2018)])
