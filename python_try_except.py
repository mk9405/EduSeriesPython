# =====================================================
# PYTHON TRY / EXCEPT / ELSE / FINALLY
# =====================================================
# Exception handling in Python allows you to handle errors
# gracefully without crashing the program.

# =====================================================
# BASIC TRY / EXCEPT
# =====================================================
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.

try:
    # This will raise an error because x is not defined
    print(x)
except:
    print("An exception occurred")

# Without try/except, the program would crash:
# print(x)  # Uncommenting this will raise a NameError

# =====================================================
# MULTIPLE EXCEPT BLOCKS
# =====================================================
# You can handle different error types differently

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# =====================================================
# ELSE BLOCK
# =====================================================
# The else block runs if no exception occurs

try:
    print("Hello")  # No error here
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")  # Runs because try succeeded

# =====================================================
# FINALLY BLOCK
# =====================================================
# The finally block always runs, whether an exception occurs or not

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' block is finished")

# Useful for cleaning up resources, like closing files
try:
    f = open("demofile.txt", "r")  # Open file
    try:
        f.write("Lorum Ipsum")  # Will raise an error (file is read-only)
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()  # Ensure file is always closed
except:
    print("Something went wrong when opening the file")

# =====================================================
# RAISE AN EXCEPTION
# =====================================================
# You can raise your own exceptions with the raise keyword

# Example: Stop program if number is negative
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")

# Example: Raise a TypeError if x is not an integer
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")

# =====================================================
# NOTES
# =====================================================
# - try: Block of code to attempt
# - except: Block executed if error occurs
# - else: Block executed if no error occurs
# - finally: Block executed no matter what
# - raise: Manually throw an exception
