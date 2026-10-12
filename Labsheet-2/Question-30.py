# Q30_strong_number.py
num = int(input("Enter an integer: "))
temp = abs(num)
strong_sum = 0

while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    strong_sum += fact
    temp //= 10

if strong_sum == num and num > 0:
    print(f"{num} is a Strong number.")
else:
    print(f"{num} is not a Strong number.")