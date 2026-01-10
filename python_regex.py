# =====================================================
# PYTHON REGULAR EXPRESSIONS (RegEx)
# =====================================================
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# Python has a built-in module called `re` to work with Regular Expressions.

import re

# =====================================================
# BASIC REGEX SEARCH
# =====================================================
# Check if a string starts with "The" and ends with "Spain"
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print("Regex search example:", x)  # Returns a Match object if found

# =====================================================
# REGEX FUNCTIONS
# =====================================================
# findall(): Returns a list of all matches
# search(): Returns a Match object for the first match
# split(): Splits the string at each match
# sub(): Replaces matches with a string

# =====================================================
# METACHARACTERS
# =====================================================
# []   -> set of characters, e.g., [a-m]
# \    -> signals a special sequence, e.g., \d
# .    -> any character except newline
# ^    -> starts with
# $    -> ends with
# *    -> zero or more occurrences
# +    -> one or more occurrences
# ?    -> zero or one occurrence
# {}   -> exact number of occurrences
# |    -> either or
# ()   -> capture group

# =====================================================
# SPECIAL SEQUENCES
# =====================================================
# \d -> digit, \D -> non-digit
# \s -> whitespace, \S -> non-whitespace
# \w -> word character, \W -> non-word character
# \A -> start of string, \Z -> end of string
# \b -> word boundary, \B -> non-word boundary

# =====================================================
# FINDALL FUNCTION
# =====================================================
txt = "The rain in Spain"
matches = re.findall("ai", txt)
print("All matches for 'ai':", matches)  # ['ai', 'ai']

# Example: No match
no_match = re.findall("Portugal", txt)
print("No match found:", no_match)  # []

# =====================================================
# SEARCH FUNCTION
# =====================================================
first_space = re.search("\s", txt)
print("First whitespace at position:", first_space.start())

# No match returns None
no_search = re.search("Portugal", txt)
print("No match search result:", no_search)

# =====================================================
# SPLIT FUNCTION
# =====================================================
split_txt = re.split("\s", txt)
print("Split by whitespace:", split_txt)

# Split with maxsplit
split_first = re.split("\s", txt, 1)
print("Split at first whitespace only:", split_first)

# =====================================================
# SUB FUNCTION
# =====================================================
# Replace all whitespaces with 9
replaced_txt = re.sub("\s", "9", txt)
print("Replace all whitespaces:", replaced_txt)

# Replace first 2 whitespaces
replaced_count = re.sub("\s", "9", txt, 2)
print("Replace first 2 whitespaces:", replaced_count)

# =====================================================
# MATCH OBJECT
# =====================================================
# Match object contains information about the match
match_obj = re.search("ai", txt)
print("Match object:", match_obj)
print("Match start and end:", match_obj.span())
print("Original string:", match_obj.string)
print("Matched text:", match_obj.group())

# Example: Find word starting with uppercase "S"
match_obj2 = re.search(r"\bS\w+", txt)
print("Word starting with 'S' span:", match_obj2.span())
print("Word starting with 'S' string:", match_obj2.string)
print("Word starting with 'S' group:", match_obj2.group())

# =====================================================
# FLAGS
# =====================================================
# re.I      -> Ignore case
# re.M      -> Multiline
# re.S      -> Dot matches all characters including newline
# re.X      -> Verbose mode for readable patterns
# re.A      -> ASCII only
# re.U      -> Unicode (default Python 3)
