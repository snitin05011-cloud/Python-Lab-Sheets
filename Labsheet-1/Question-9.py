# Q9_swap_without_temp.py
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Before swapping: a = {a}, b = {b}")
a, b = b, a  # Python tuple unpacking swap
print(f"After swapping: a = {a}, b = {b}")