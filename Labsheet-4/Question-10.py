# Program to convert a list into a string without using join()
elements = input("Enter list elements separated by space: ").split()
result_str = ""

for item in elements:
    result_str += str(item) + " "

print("Converted string:", result_str.strip())