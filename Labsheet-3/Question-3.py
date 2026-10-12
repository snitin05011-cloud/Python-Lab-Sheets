# Q3_replace_spaces.py
s = input("Enter a string: ")
result = ""
for char in s:
    if char == " ":
        result += "_"
    else:
        result += char
print(f"Modified string: {result}")