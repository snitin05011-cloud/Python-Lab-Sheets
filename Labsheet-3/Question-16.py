# Program to count the number of digits, alphabets, and special characters
string = input("Enter a string: ")
digits = alphabets = specials = 0

for char in string:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        alphabets += 1
    else:
        specials += 1

print(f"Alphabets: {alphabets}")
print(f"Digits: {digits}")
print(f"Special Characters: {specials}")