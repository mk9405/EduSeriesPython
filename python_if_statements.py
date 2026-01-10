# =====================================================
# PYTHON IF, ELIF, ELSE, LOGICAL OPERATORS, NESTED IF, PASS
# =====================================================

# =====================================================
# SIMPLE IF STATEMENT
# =====================================================
a = 33
b = 200
if b > a:
    print("b is greater than a")

number = 15
if number > 0:
    print("The number is positive")

# Multiple statements in if block
age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")

# Boolean variable in if
is_logged_in = True
if is_logged_in:
    print("Welcome back!")

# =====================================================
# ELIF STATEMENT
# =====================================================
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")

# =====================================================
# ELSE STATEMENT
# =====================================================
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Else without elif
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# =====================================================
# SHORTHAND IF / TERNARY OPERATOR
# =====================================================
a = 5
b = 2
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)

# =====================================================
# LOGICAL OPERATORS: AND, OR, NOT
# =====================================================
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

if a > b or a > c:
    print("At least one condition is True")

a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

age = 25
is_student = False
has_discount_code = True
if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount applies!")

temperature = 25
is_raining = False
is_weekend = True
if (temperature > 20 and not is_raining) or is_weekend:
    print("Great day for outdoor activities!")

username = "Tobias"
password = "secret123"
is_verified = True
if username and password and is_verified:
    print("Login successful")
else:
    print("Login failed")

score = 85
if score >= 0 and score <= 100:
    print("Valid score")
else:
    print("Invalid score")

# =====================================================
# NESTED IF STATEMENTS
# =====================================================
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

age = 25
has_license = True
if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")

score = 85
attendance = 90
submitted = True
if score >= 60:
    if attendance >= 80:
        if submitted:
            print("Pass with good standing")
        else:
            print("Pass but missing assignment")
    else:
        print("Pass but low attendance")
else:
    print("Fail")

# Nested if vs logical operators
temperature = 25
is_sunny = True
if temperature > 20:
    if is_sunny:
        print("Perfect beach weather!")

if temperature > 20 and is_sunny:
    print("Perfect beach weather!")

username = "Emil"
password = "python123"
is_active = True
if username:
    if password:
        if is_active:
            print("Login successful")
        else:
            print("Account is not active")
    else:
        print("Password required")
else:
    print("Username required")

score = 92
extra_credit = 5
if score >= 90:
    if extra_credit > 0:
        print("A+ grade")
    else:
        print("A grade")
elif score >= 80:
    print("B grade")
else:
    print("C grade or below")

# =====================================================
# PASS STATEMENT
# =====================================================
a = 33
b = 200
if b > a:
    pass

age = 16
if age < 18:
    pass # TODO: Add underage logic later
else:
    print("Access granted")

score = 85
if score > 90:
    pass
print("Score processed")

value = 50
if value < 0:
    print("Negative value")
elif value == 0:
    pass
else:
    print("Positive value")

def calculate_discount(price):
    pass # TODO: Implement discount logic

# =====================================================
# PRACTICE QUESTIONS
# =====================================================
# Q1. Check if a number is positive, negative, or zero
# Q2. Grade calculator using if-elif-else
# Q3. Shorthand if to print max of two numbers
# Q4. Login validation using username and password
# Q5. Check if a user is eligible for a discount (age & student status)
# Q6. Nested if to validate driving eligibility
# Q7. Use pass as placeholder for a TODO in if statement
# Q8. Use logical operators to check multiple conditions in one statement
# Q9. Create a shorthand ternary to assign bigger value
# Q10. Classify temperature ranges with if-elif-else

