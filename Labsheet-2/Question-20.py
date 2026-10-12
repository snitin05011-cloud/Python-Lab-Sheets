# Q20_count_digits.py
num = int(input("Enter an integer: "))
if num == 0:
    count = 1
else:
    count = 0
    temp = abs(num)
    while temp > 0:
        count += 1
        temp //= 10
print(f"Number of digits: {count}")