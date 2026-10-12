# Q7_reverse_string.py
s = input("Enter a string: ")
rev = ""
for char in s:
    rev = char + rev
print(f"Reversed string: {rev}")