# Q19_emi.py
p = float(input("Enter loan principal amount: "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = float(input("Enter tenure in years: "))
r = annual_rate / (12 * 100)
n = years * 12
emi = (p * r * ((1 + r) ** n)) / (((1 + r) ** n) - 1)
print(f"Monthly EMI: {emi:.2f}")