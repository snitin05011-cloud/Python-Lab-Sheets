# Q2_palindrome.py
num_str = input("Enter a number: ")
if num_str == num_str[::-1]:
    print(f"{num_str} is a palindrome.")
else:
    print(f"{num_str} is not a palindrome.")