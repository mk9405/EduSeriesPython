# =====================================================
# PYTHON REGULAR EXPRESSIONS (RegEx)
# COMPLETE NOTES WITH BEST EXAMPLES
# =====================================================

# RegEx (Regular Expression) ek pattern hota hai
# jiska use string me search, match, extract aur replace ke liye hota hai

# Python me RegEx ke liye built-in module hota hai: re

import re

print("========== PYTHON REGEX NOTES ==========\n")

# =====================================================
# 1. BASIC REGEX SEARCH
# =====================================================
print("1. BASIC REGEX SEARCH")

txt = "The rain in Spain"

# ^The  -> string 'The' se start honi chahiye
# .*    -> beech me kuch bhi ho sakta hai
# Spain$-> string 'Spain' par end honi chahiye

x = re.search("^The.*Spain$", txt)

if x:
    print("Match found:", x.group())
else:
    print("No match found")

print("-" * 50)

# =====================================================
# 2. REGEX FUNCTIONS
# =====================================================
print("2. REGEX FUNCTIONS")

# re.findall() -> all matches ki list deta hai
# re.search()  -> first match ka Match object deta hai
# re.split()   -> pattern ke base par string tod deta hai
# re.sub()     -> pattern ko replace karta hai

print("Functions: findall, search, split, sub")
print("-" * 50)

# =====================================================
# 3. METACHARACTERS
# =====================================================
print("3. METACHARACTERS")

# []   -> set of characters
# .    -> any character except newline
# ^    -> start of string
# $    -> end of string
# *    -> zero or more times
# +    -> one or more times
# ?    -> zero or one time
# {}   -> exact number of times
# |    -> OR
# ()   -> group

txt2 = "apple, banana, mango"

# words starting with 'a'
result = re.findall(r"\ba\w+", txt2)
print("Words starting with 'a':", result)

print("-" * 50)

# =====================================================
# 4. SPECIAL SEQUENCES
# =====================================================
print("4. SPECIAL SEQUENCES")

# \d -> digit
# \D -> non-digit
# \s -> whitespace
# \S -> non-whitespace
# \w -> word character (a-z, A-Z, 0-9, _)
# \W -> non-word character
# \b -> word boundary

txt3 = "Order ID: 12345, Amount: 6789"

digits = re.findall(r"\d+", txt3)
print("Digits found:", digits)

words = re.findall(r"\b\w+\b", txt3)
print("Words found:", words)

print("-" * 50)

# =====================================================
# 5. FINDALL FUNCTION
# =====================================================
print("5. FINDALL FUNCTION")

txt4 = "The rain in Spain stays mainly in the plain"

matches = re.findall("ain", txt4)
print("All 'ain' matches:", matches)

no_match = re.findall("Portugal", txt4)
print("No match result:", no_match)

print("-" * 50)

# =====================================================
# 6. SEARCH FUNCTION
# =====================================================
print("6. SEARCH FUNCTION")

space = re.search(r"\s", txt4)
print("First space position:", space.start())

not_found = re.search("Germany", txt4)
print("Search not found:", not_found)

print("-" * 50)

# =====================================================
# 7. SPLIT FUNCTION
# =====================================================
print("7. SPLIT FUNCTION")

split_result = re.split(r"\s", txt4)
print("Split by space:", split_result)

split_once = re.split(r"\s", txt4, 1)
print("Split only once:", split_once)

print("-" * 50)

# =====================================================
# 8. SUB FUNCTION
# =====================================================
print("8. SUB FUNCTION")

replace_all = re.sub(r"\s", "-", txt4)
print("Replace spaces with - :", replace_all)

replace_two = re.sub(r"\s", "-", txt4, 2)
print("Replace first 2 spaces:", replace_two)

print("-" * 50)

# =====================================================
# 9. MATCH OBJECT DETAILS
# =====================================================
print("9. MATCH OBJECT DETAILS")

match_obj = re.search("Spain", txt4)

if match_obj:
    print("Match found:", match_obj.group())
    print("Start-End:", match_obj.span())
    print("Original string:", match_obj.string)
else:
    print("No match")

print("-" * 50)

# =====================================================
# 10. PRACTICAL EXAMPLES
# =====================================================
print("10. PRACTICAL EXAMPLES")

# Mobile number validation
mobile = "9876543210"
if re.fullmatch(r"\d{10}", mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")

# Email validation
email = "test123@gmail.com"
if re.fullmatch(r"[a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]+", email):
    print("Valid Email")
else:
    print("Invalid Email")

# Password validation
password = "Python@123"
pattern = r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}"

if re.fullmatch(pattern, password):
    print("Strong Password")
else:
    print("Weak Password")

print("-" * 50)

# =====================================================
# 11. FLAGS
# =====================================================
print("11. REGEX FLAGS")

# re.I -> ignore case
# re.M -> multiline
# re.S -> dot matches newline

txt5 = "python is Easy"

match_flag = re.search("PYTHON", txt5, re.I)
print("Ignore case match:", match_flag.group())

print("\n========== END OF REGEX NOTES ==========")


# =====================================================
# PYTHON REGEX METACHARACTERS
# =====================================================

import re

print("\n========== REGEX METACHARACTERS EXAMPLES ==========\n")

# =====================================================
# 1. []  -> SET OF CHARACTERS
# =====================================================
print("1. []  -> Set of characters")

text = "cat bat rat mat"
result = re.findall("[cb]at", text)
print("Input :", text)
print("Pattern: [cb]at")
print("Output :", result)
print("Explanation: c ya b se start hone wale words match hue\n")

# =====================================================
# 2. .  -> ANY CHARACTER (except newline)
# =====================================================
print("2. .  -> Any character")

text = "cat bat rat"
result = re.findall("c.t", text)
print("Output :", result)
print("Explanation: '.' kisi bhi ek character ko represent karta hai\n")

# =====================================================
# 3. ^  -> START OF STRING
# =====================================================
print("3. ^  -> Start of string")

text = "Python is easy"
result = re.search("^Python", text)
print("Input :", text)
print("Pattern: ^Python")
print("Output :", result.group())
print("Explanation: string Python se start ho rahi hai\n")

# =====================================================
# 4. $  -> END OF STRING
# =====================================================
print("4. $  -> End of string")

text = "Learning Python"
result = re.search("Python$", text)
print("Input :", text)
print("Pattern: Python$")
print("Output :", result.group())
print("Explanation: string Python par end ho rahi hai\n")

# =====================================================
# 5. *  -> ZERO OR MORE TIMES
# =====================================================
print("5. *  -> Zero or more times")

text = "ca cat caaat"
result = re.findall("ca*t", text)
print("Input :", text)
print("Pattern: ca*t")
print("Output :", result)
print("Explanation: 'a' zero ya multiple times aa sakta hai\n")

# =====================================================
# 6. +  -> ONE OR MORE TIMES
# =====================================================
print("6. +  -> One or more times")

text = "cat caaat ct"
result = re.findall("ca+t", text)
print("Input :", text)
print("Pattern: ca+t")
print("Output :", result)
print("Explanation: kam se kam ek 'a' hona zaroori hai\n")

# =====================================================
# 7. ?  -> ZERO OR ONE TIME
# =====================================================
print("7. ?  -> Zero or one time")

text = "color colour"
result = re.findall("colou?r", text)
print("Input :", text)
print("Pattern: colou?r")
print("Output :", result)
print("Explanation: 'u' optional hai\n")

# =====================================================
# 8. {}  -> EXACT NUMBER OF TIMES
# =====================================================
print("8. {}  -> Exact number of times")

text = "999 99 9999"
result = re.findall(r"\d{3}", text)
print("Input :", text)
print("Pattern: \\d{3}")
print("Output :", result)
print("Explanation: sirf exact 3 digits match honge\n")

# =====================================================
# 9. |  -> OR OPERATOR
# =====================================================
print("9. |  -> OR operator")

text = "dog cat cow"
result = re.findall("dog|cat", text)
print("Input :", text)
print("Pattern: dog|cat")
print("Output :", result)
print("Explanation: dog ya cat dono me se koi bhi match hoga\n")

# =====================================================
# 10. ()  -> GROUP
# =====================================================
print("10. ()  -> Group")

text = "abc123 abc456"
result = re.findall("(abc)\d+", text)
print("Input :", text)
print("Pattern: (abc)\\d+")
print("Output :", result)
print("Explanation: sirf group ke andar ka part return hota hai\n")

print("========== END OF FILE ==========\n")
