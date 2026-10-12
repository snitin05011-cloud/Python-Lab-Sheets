# Q1_palindrome.py
s = input("Enter a string: ")
rev = ""
for char in s:
    rev = char + rev
if s == rev:
    print(f"'{s}' is a palindrome.")
else:
    print(f"'{s}' is not a palindrome.")