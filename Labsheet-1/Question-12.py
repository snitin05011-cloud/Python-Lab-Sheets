# Q12_simple_interest.py
p = float(input("Enter principal amount: "))
r = float(input("Enter annual rate of interest (%): "))
t = float(input("Enter time period (years): "))
si = (p * r * t) / 100
print(f"Simple Interest: {si:.2f}")