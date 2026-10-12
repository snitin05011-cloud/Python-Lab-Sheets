# Program to convert vowels to uppercase and consonants to lowercase
string = input("Enter a string: ")
result = ""

for char in string:
    if char.lower() in "aeiou":
        result += char.upper()
    elif char.isalpha():
        result += char.lower()
    else:
        result += char

print("Modified string:", result)