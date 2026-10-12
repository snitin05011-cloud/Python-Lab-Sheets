# Program to create a set with different data types
# Note: Sets only store hashable (immutable) types (int, float, string, tuple, bool)
mixed_set = {10, 3.14, "Python", True, (1, 2)}

print("Mixed Data Type Set:", mixed_set)
for item in mixed_set:
    print(f"Value: {item}, Type: {type(item)}")