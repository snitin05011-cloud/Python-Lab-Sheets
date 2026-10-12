# Q1_multiple_3_7.py
num = int(input("Enter an integer: "))
if num % 3 == 0 and num % 7 == 0:
    print(f"{num} is a multiple of both 3 and 7.")
else:
    print(f"{num} is not a multiple of both 3 and 7.")