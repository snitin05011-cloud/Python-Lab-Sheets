# Q29_check_range.py
num = float(input("Enter a number to check: "))
low = float(input("Enter range lower bound: "))
high = float(input("Enter range upper bound: "))
if low <= num <= high:
    print(f"{num} is within the range [{low}, {high}].")
else:
    print(f"{num} is outside the range [{low}, {high}].")