#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

# ^  -> start of string
# a  -> letter 'a'
# b* -> zero or more 'b'
# $  -> end of string
pattern = r"^ab*$"

text = input("Enter string: ")

if re.match(pattern, text):
    print("Match found")
else:
    print("No match")

#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

# b{2,3} -> 'b' must appear at least 2 times and at most 3 times
pattern = r"^ab{2,3}$"

text = input("Enter string: ")

if re.match(pattern, text):
    print("Match found")
else:
    print("No match")

#Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

# \b        -> word boundary
# [a-z]+    -> one or more lowercase letters
# _         -> underscore
# [a-z]+    -> one or more lowercase letters
# \b        -> word boundary
pattern = r"\b[a-z]+_[a-z]+\b"

text = input("Enter text: ")

matches = re.findall(pattern, text)
print(matches)

#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

# [A-Z]   -> exactly one uppercase letter
# [a-z]+  -> one or more lowercase letters
pattern = r"\b[A-Z][a-z]+\b"

text = input("Enter text: ")

matches = re.findall(pattern, text)
print(matches)

#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

# a    -> must start with 'a'
# .*   -> any characters (zero or more)
# b    -> must end with 'b'
pattern = r"^a.*b$"

text = input("Enter string: ")

if re.match(pattern, text):
    print("Match found")
else:
    print("No match")

#Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re

# [ ,.]  -> matches space OR comma OR dot
pattern = r"[ ,.]"

text = input("Enter text: ")

# re.sub replaces all matches with ":"
result = re.sub(pattern, ":", text)

print(result)


#Write a python program to convert snake case string to camel case string.

import re

def snake_to_camel(text):
    # _([a-z])  -> underscore followed by lowercase letter
    # group(1)  -> letter after underscore
    # lambda    -> convert that letter to uppercase
    return re.sub(r"_([a-z])", lambda x: x.group(1).upper(), text)

text = input("Enter snake_case string: ")

print(snake_to_camel(text))


#Write a Python program to split a string at uppercase letters.

import re

# [A-Z]     -> uppercase letter
# [^A-Z]*   -> zero or more characters that are NOT uppercase
pattern = r"[A-Z][^A-Z]*"

text = input("Enter camelCase string: ")

result = re.findall(pattern, text)

print(result)

#Write a Python program to insert spaces between words starting with capital letters.

import re

# (?<!^)    -> negative lookbehind (not start of string)
# ([A-Z])   -> uppercase letter
pattern = r"(?<!^)([A-Z])"

text = input("Enter text: ")

# add space before each capital letter
result = re.sub(pattern, r" \1", text)

print(result)


#Write a Python program to convert a given camel case string to snake case.

import re

def camel_to_snake(text):
    # ([A-Z]) -> find uppercase letter
    # _\1     -> add underscore before it
    # .lower() -> convert entire string to lowercase
    return re.sub(r"([A-Z])", r"_\1", text).lower()

text = input("Enter camelCase string: ")

print(camel_to_snake(text))