# Q21_sum_digits.py
num = int(input("Enter an integer: "))
digit_sum = 0
temp = abs(num)
while temp > 0:
    digit_sum += temp % 10
    temp //= 10
print(f"Sum of digits: {digit_sum}")