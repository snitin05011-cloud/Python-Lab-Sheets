# Program to remove all punctuation from a string
import string as str_module
string = input("Enter a string: ")
result = ""

for char in string:
    if char not in str_module.punctuation:
        result += char

print("String without punctuation:", result)