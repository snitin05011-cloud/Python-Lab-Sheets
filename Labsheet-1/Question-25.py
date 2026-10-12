# Q25_largest_two.py
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if a > b:
    print(f"The largest number is {a}")
elif b > a:
    print(f"The largest number is {b}")
else:
    print("Both numbers are equal.")