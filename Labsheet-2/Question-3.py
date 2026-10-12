# Q3_armstrong.py
num_str = input("Enter an integer: ")
power = len(num_str)
num = int(num_str)
temp = num
sum_val = 0
while temp > 0:
    digit = temp % 10
    sum_val += digit ** power
    temp //= 10
if sum_val == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")