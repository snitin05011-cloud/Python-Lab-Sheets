# Q13_compound_interest.py
p = float(input("Enter principal amount: "))
r = float(input("Enter annual rate of interest (%): "))
t = float(input("Enter time period (years): "))
n = int(input("Enter compounding frequency per year: "))
ci = p * (1 + (r / (100 * n))) ** (n * t) - p
print(f"Compound Interest: {ci:.2f}")