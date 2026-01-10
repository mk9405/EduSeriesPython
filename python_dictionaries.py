# =====================================================
# PYTHON DICTIONARIES – COMPLETE NOTES + EXECUTABLE CODE
# =====================================================

# Dictionaries store data in key:value pairs
# Ordered (Python 3.7+), changeable, no duplicate keys
# Written with curly brackets {}

# =====================================================
# CREATE DICTIONARY
# =====================================================
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Access value by key
print(thisdict["brand"])

# Using get() method
x = thisdict.get("model")
print(x)

# Duplicate keys overwrite values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# Dictionary length
print(len(thisdict))

# Values can be any data type
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(thisdict))

# Using dict() constructor
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)


# =====================================================
# GET KEYS, VALUES, ITEMS
# =====================================================
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# keys() - returns view of keys
x = car.keys()
print(x)
car["color"] = "white"
print(x)  # reflects change

# values() - returns view of values
x = car.values()
print(x)
car["year"] = 2020
print(x)
car["color2"] = "red"
print(x)

# items() - returns key:value pairs as tuples
x = car.items()
print(x)
car["year"] = 2025
print(x)
car["color3"] = "blue"
print(x)


# =====================================================
# CHECK IF KEY EXISTS
# =====================================================
if "model" in thisdict:
    print("Yes, 'model' is a key in thisdict")


# =====================================================
# CHANGE DICTIONARY ITEMS
# =====================================================
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict["year"] = 2018
print(thisdict)

# update() method
thisdict.update({"year": 2020})
print(thisdict)


# =====================================================
# ADD DICTIONARY ITEMS
# =====================================================
thisdict["color"] = "red"
print(thisdict)

# update() can also add items
thisdict.update({"color2": "blue"})
print(thisdict)


# =====================================================
# REMOVE DICTIONARY ITEMS
# =====================================================
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# pop() removes item by key
thisdict.pop("model")
print(thisdict)

# popitem() removes last inserted item
thisdict.popitem()
print(thisdict)

# del removes key or entire dictionary
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict["model"]
print(thisdict)

# del dictionary completely
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# del thisdict
# print(thisdict)  # will raise error

# clear() empties dictionary
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)


# =====================================================
# LOOP THROUGH DICTIONARY
# =====================================================
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# keys
for x in thisdict:
    print(x)

# values
for x in thisdict:
    print(thisdict[x])

# using values()
for x in thisdict.values():
    print(x)

# using keys()
for x in thisdict.keys():
    print(x)

# keys and values
for x, y in thisdict.items():
    print(x, y)


# =====================================================
# COPY DICTIONARY
# =====================================================
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# using copy()
mydict = thisdict.copy()
print(mydict)

# using dict()
mydict2 = dict(thisdict)
print(mydict2)


# =====================================================
# NESTED DICTIONARIES
# =====================================================
# dictionary containing dictionaries
myfamily = {
  "child1": {"name": "Emil", "year": 2004},
  "child2": {"name": "Tobias", "year": 2007},
  "child3": {"name": "Linus", "year": 2011}
}

print(myfamily["child2"]["name"])  # access nested value

# nested loop
for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])


# =====================================================
# DICTIONARY METHODS
# =====================================================
# clear(), copy(), fromkeys(), get(), items(), keys(), pop(), popitem(), setdefault(), update(), values()
mydict = {"a": 1, "b": 2, "c": 3}
print(mydict.get("a"))
mydict.update({"d": 4})
print(mydict)
print(mydict.keys())
print(mydict.values())
print(mydict.items())
mydict.pop("b")
print(mydict)
mydict.setdefault("e", 5)
print(mydict)


# =====================================================
# PRACTICE QUESTIONS
# =====================================================
# Q1. Create a dictionary for a car with brand, model, year
# Q2. Access the model using both [] and get()
# Q3. Add a color to the car dictionary
# Q4. Remove the year key
# Q5. Loop through keys and values
# Q6. Copy the dictionary
# Q7. Create a nested dictionary for 2 children
# Q8. Update the brand using update()
# Q9. Check if a key 'model' exists
# Q10. Clear the dictionary

# =====================================================
# HINTS / ANSWERS
# =====================================================
# A1. car = {"brand":"Ford","model":"Mustang","year":2020}
# A2. car["model"], car.get("model")
# A3. car["color"] = "red"
# A4. car.pop("year") or del car["year"]
# A5. for k,v in car.items(): print(k,v)
# A6. car_copy = car.copy() or dict(car)
# A7. family = {"child1":{"name":"Emil"}, "child2":{"name":"Tobias"}}
# A8. car.update({"brand":"BMW"})
# A9. if "model" in car: print("exists")
# A10. car.clear()
