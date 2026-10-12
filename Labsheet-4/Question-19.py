# Program to check if a key exists in a dictionary
d = {"name": "Alice", "age": 22, "course": "MCA"}
key = input("Enter key to search: ")

if key in d:
    print(f"Key '{key}' exists with value: {d[key]}")
else:
    print(f"Key '{key}' does not exist.")