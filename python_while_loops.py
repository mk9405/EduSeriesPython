# =====================================================
# PYTHON WHILE LOOPS
# =====================================================

# -----------------------------------------------------
# BASIC WHILE LOOP
# -----------------------------------------------------
# Execute a set of statements as long as a condition is true
i = 1
print("Basic while loop:")
while i < 6:
    print(i)
    i += 1  # Important: increment to avoid infinite loop

# -----------------------------------------------------
# BREAK STATEMENT
# -----------------------------------------------------
# Stop the loop even if the while condition is true
i = 1
print("\nUsing break statement:")
while i < 6:
    print(i)
    if i == 3:
        print("Breaking the loop at i =", i)
        break
    i += 1

# -----------------------------------------------------
# CONTINUE STATEMENT
# -----------------------------------------------------
# Skip the current iteration and continue with the next
i = 0
print("\nUsing continue statement:")
while i < 6:
    i += 1
    if i == 3:
        print("Skipping i =", i)
        continue
    print(i)

# -----------------------------------------------------
# WHILE ... ELSE
# -----------------------------------------------------
# Execute a block of code once the while condition becomes false
i = 1
print("\nUsing while...else statement:")
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# -----------------------------------------------------
# PRACTICAL EXAMPLES
# -----------------------------------------------------

# Example 1: Sum of numbers from 1 to 5
i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print("\nSum of numbers 1 to 5:", total)

# Example 2: Find first number divisible by 7
i = 1
while True:  # Infinite loop, must break manually
    if i % 7 == 0:
        print("\nFirst number divisible by 7 is:", i)
        break
    i += 1

# Example 3: Print only odd numbers less than 10
i = 0
print("\nOdd numbers less than 10:")
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# Example 4: Countdown
i = 5
print("\nCountdown:")
while i > 0:
    print(i)
    i -= 1
else:
    print("Blast off!")

# Example 5: User input until correct password
password = ""
correct_password = "python123"
while password != correct_password:
    # Simulating user input
    password = input("\nEnter password: ")
    if password == correct_password:
        print("Access granted")
    else:
        print("Incorrect password, try again!")

# -----------------------------------------------------
# PRACTICE QUESTIONS
# -----------------------------------------------------
# Q1. Use a while loop to print numbers from 10 to 1
# Q2. Use break to stop a loop when a number divisible by 13 is found
# Q3. Use continue to skip multiples of 3 while counting 1 to 20
# Q4. Use while...else to print a message after the loop ends
# Q5. Use an infinite loop with break to simulate a login system
