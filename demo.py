import re

# txt = "The rain in gmail.com"
# x = re.search("^The.*gmail.com$", txt)
# print("Regex search example:", x) 

txt = "The rain in a Spain  "
# matches = re.findall("rain", txt)
# print("All matches for 'ai':", matches)

first_space = re.search("\s", txt)
print("First whitespace at position:", first_space.start(), first_space)