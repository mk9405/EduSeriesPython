# =====================================================
# PYTHON JSON
# =====================================================
# JSON (JavaScript Object Notation) is a syntax for storing and exchanging data.
# Python has a built-in module called `json` to work with JSON data.

import json

# =====================================================
# PARSE JSON (JSON -> Python)
# =====================================================
# If you have a JSON string, you can convert it into a Python object (dict or list)
# using json.loads()

# Example JSON string
json_string = '{ "name":"John", "age":30, "city":"New York"}'

# Convert JSON string to Python dictionary
python_dict = json.loads(json_string)

# Access values like a normal dictionary
print("Age from JSON:", python_dict["age"])  # Output: 30

# =====================================================
# CONVERT PYTHON TO JSON (Python -> JSON)
# =====================================================
# Use json.dumps() to convert Python objects into JSON strings

# Example Python dictionary
python_obj = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convert to JSON string
json_output = json.dumps(python_obj)
print("JSON string:", json_output)

# =====================================================
# CONVERT DIFFERENT PYTHON DATA TYPES TO JSON
# =====================================================
# Python -> JSON mapping:
# dict   -> Object
# list   -> Array
# tuple  -> Array
# str    -> String
# int    -> Number
# float  -> Number
# True   -> true
# False  -> false
# None   -> null

# Examples:
print(json.dumps({"name": "John", "age": 30}))      # dict
print(json.dumps(["apple", "bananas"]))            # list
print(json.dumps(("apple", "bananas")))            # tuple
print(json.dumps("hello"))                          # string
print(json.dumps(42))                               # int
print(json.dumps(31.76))                            # float
print(json.dumps(True))                             # boolean True
print(json.dumps(False))                            # boolean False
print(json.dumps(None))                             # None/null

# =====================================================
# COMPLEX PYTHON OBJECT TO JSON
# =====================================================
complex_obj = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

json_complex = json.dumps(complex_obj)
print("Complex JSON:", json_complex)

# =====================================================
# FORMATTING JSON (Make it readable)
# =====================================================
# Use the `indent` parameter for indentation
formatted_json = json.dumps(complex_obj, indent=4)
print("Formatted JSON:\n", formatted_json)

# Use `separators` to customize separators
custom_sep_json = json.dumps(complex_obj, indent=4, separators=(". ", " = "))
print("Custom Separator JSON:\n", custom_sep_json)

# =====================================================
# SORTING KEYS IN JSON
# =====================================================
# Use `sort_keys=True` to sort the JSON keys alphabetically
sorted_json = json.dumps(complex_obj, indent=4, sort_keys=True)
print("Sorted JSON:\n", sorted_json)
