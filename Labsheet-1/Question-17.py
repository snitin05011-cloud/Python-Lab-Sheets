# Q17_power.py
base = float(input("Enter base: "))
exponent = int(input("Enter integer exponent: "))
result = 1
for _ in range(abs(exponent)):
    result *= base
if exponent < 0:
    result = 1 / result
print(f"Result: {result}")