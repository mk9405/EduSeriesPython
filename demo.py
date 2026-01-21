import re

# text = "hello, i am learning python"

# result = re.search("^hello.*python$", text)

# print(result)

# if result:
#     print("match found: ", result.group())

# else:
#     print("not matched:")

# txt2 = "apple_123, banana, mango"

# # words starting with 'a'
# result = re.findall(r"\ba\w+", txt2)
# print("Words starting with 'a':", result)

# txt3 = "Order ID: #$ 12345, Amount: 6789"

# # digits = re.findall(r"\d+", txt3)
# # print("Digits found:", digits)


# words = re.findall(r"\b\W+", txt3)
# print("Words found:", words)

txt4 = "The rain, in,  Spain,    stays,  mainly in the plain"

# matches = re.findall("ain", txt4)
# print("All 'ain' matches:", matches)

# space = re.search(r"\s", txt4)
# print("First space position:", space.start())

# not_found = re.search("Germany", txt4)
# print("Search not found:", not_found)

# split_result = re.split(r"\b\w+", txt4)
# print("Split by space:", split_result)

# replace_all = re.sub(r"\s", "*", txt4, 4)
# print("Replace spaces with - :", replace_all)

# mobile = "98765432102"
# if re.fullmatch(r"\d{10}", mobile):
#     print("Valid Mobile Number", "+91: ", mobile )
# else:
#     print("Invalid Mobile Number")


email = "test123@gmail.com"
if re.fullmatch(r"[a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]+", email):
    print("Valid Email")
else:
    print("Invalid Email")

















