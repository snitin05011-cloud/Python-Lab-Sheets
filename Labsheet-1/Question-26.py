# Q26_largest_three.py
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a >= b and a >= c:
    print(f"The largest number is {a}")
elif b >= a and b >= c:
    print(f"The largest number is {b}")
else:
    print(f"The largest number is {c}")