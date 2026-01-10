# =====================================================
# PYTHON MATCH STATEMENT
# =====================================================

# -----------------------------------------------------
# SIMPLE MATCH STATEMENT
# -----------------------------------------------------
day = 4

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

# -----------------------------------------------------
# DEFAULT CASE USING UNDERSCORE (_)
# -----------------------------------------------------
day = 4

match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:  # acts as default
        print("Looking forward to the Weekend")

# -----------------------------------------------------
# COMBINE VALUES USING PIPE (|)
# -----------------------------------------------------
day = 4

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")

# -----------------------------------------------------
# IF STATEMENTS AS GUARDS
# -----------------------------------------------------
month = 5
day = 4

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")

# -----------------------------------------------------
# EXAMPLES WITH STRINGS
# -----------------------------------------------------
fruit = "apple"

match fruit:
    case "apple":
        print("Fruit is apple")
    case "banana":
        print("Fruit is banana")
    case _:
        print("Unknown fruit")

# -----------------------------------------------------
# MULTIPLE CONDITIONS WITH GUARDS
# -----------------------------------------------------
score = 85
grade = 'B'

match grade:
    case "A" if score >= 90:
        print("Excellent! You scored an A")
    case "B" if 80 <= score < 90:
        print("Good job! You scored a B")
    case "C" if 70 <= score < 80:
        print("You scored a C")
    case _:
        print("Score not classified")

# -----------------------------------------------------
# PRACTICE QUESTIONS
# -----------------------------------------------------
# Q1. Use match to print day of the week for a given number
# Q2. Add a default case for numbers outside 1-7
# Q3. Combine weekdays and weekends in one case using |
# Q4. Use a guard to check both day and month
# Q5. Use match for string values like fruits or colors
# Q6. Use match to classify exam scores into grades
# Q7. Use _ as a fallback for unexpected inputs
