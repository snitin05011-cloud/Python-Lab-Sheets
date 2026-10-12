# Q4_extract_uppercase.py
s = input("Enter a string: ")
upper_chars = ""
for char in s:
    if char.isupper():
        upper_chars += char
print(f"Uppercase characters: {upper_chars}")