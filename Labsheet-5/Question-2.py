# Program to create a tuple with different data types
# Storing an integer, float, string, and boolean
mixed_tuple = (42, 3.14159, "Python", True)

print("Mixed Data Type Tuple:", mixed_tuple)
for item in mixed_tuple:
    print(f"Value: {item}, Type: {type(item)}")