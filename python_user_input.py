# =====================================================
# PYTHON USER INPUT
# =====================================================
# Python allows the program to take input from the user using the input() function.
# The input is always returned as a string, and can be converted to other types if needed.

# =====================================================
# BASIC USER INPUT
# =====================================================
print("Enter your name:")
name = input()  # Waits for user input
print(f"Hello {name}")

# =====================================================
# USING PROMPT IN input()
# =====================================================
# You can add a prompt directly inside the input() function
name = input("Enter your name: ")
print(f"Hello {name}")

# =====================================================
# MULTIPLE INPUTS
# =====================================================
# You can take as many inputs as you want, Python will stop execution at each input
name = input("Enter your name: ")
print(f"Hello {name}")

fav1 = input("What is your favorite animal? ")
fav2 = input("What is your favorite color? ")
fav3 = input("What is your favorite number? ")

print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

# =====================================================
# INPUT NUMBERS
# =====================================================
# Input from user is treated as a string by default.
# To perform numerical operations, you must convert the input into int or float
import math

x = input("Enter a number: ")
y = math.sqrt(float(x))  # Convert input to float before calculation
print(f"The square root of {x} is {y}")

# =====================================================
# VALIDATING INPUT
# =====================================================
# Good practice: validate input to prevent errors
# Keep asking the user until they enter a valid number

valid_input = False
while not valid_input:
    x = input("Enter a number: ")
    try:
        x = float(x)  # Try to convert input to float
        valid_input = True  # Conversion successful, exit loop
    except:
        print("Wrong input, please try again.")  # Conversion failed, ask again

print("Thank you! You entered a valid number:", x)
