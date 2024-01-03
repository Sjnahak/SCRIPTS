####create multiple file inside a folder with separate function and module is created
#example
#-->New-Modules-folder
#  ->helpers.py
     def extract_upper(phrase):
     return list(filter(str.isupper, phrase))

     def extract_lower(phrase):
     return list(filter(str.islower, phrase))

########create a new file as main.py and find few examples of impoting module
import import helpers 
name = "Doctor Strange"

print(f"Lowercase letters: {helpers.extract_lower(name)}")
print(f"Uppercase letters: {helpers.extract_upper(name)}")

import helpers as h
print(f"Lowercase letters: {h.extract_lower(name)}")
print(f"Uppercase letters: {h.extract_upper(name)}")

from helpers import extract_lower, extract_upper

print(f"Lowercase letters: {extract_lower(name)}")
print(f"Uppercase letters: {extract_upper(name)}")

###Package
#If a directory has __init__py file it is considered as package
