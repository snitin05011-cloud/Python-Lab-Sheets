# Program to remove a key from a dictionary
d = {"a": 10, "b": 20, "c": 30}
print("Current dictionary:", d)
key_to_remove = input("Enter key to remove: ")

if key_to_remove in d:
    del d[key_to_remove]
    print("Dictionary after removal:", d)
else:
    print("Key not found.")