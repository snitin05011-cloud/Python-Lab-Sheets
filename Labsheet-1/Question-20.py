# Q20_percentage.py
max_marks = float(input("Enter maximum marks per subject: "))
s1 = float(input("Marks in Subject 1: "))
s2 = float(input("Marks in Subject 2: "))
s3 = float(input("Marks in Subject 3: "))
s4 = float(input("Marks in Subject 4: "))
s5 = float(input("Marks in Subject 5: "))
total_obtained = s1 + s2 + s3 + s4 + s5
total_max = max_marks * 5
percentage = (total_obtained / total_max) * 100
print(f"Total Percentage: {percentage:.2f}%")