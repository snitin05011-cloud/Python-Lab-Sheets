# Q10_smallest_three.py
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a <= b and a <= c:
    print(f"The smallest number is {a}")
elif b <= a and b <= c:
    print(f"The smallest number is {b}")
else:
    print(f"The smallest number is {c}")