# Q18_bmi.py
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi = weight / (height ** 2)
print(f"Body Mass Index (BMI): {bmi:.2f}")