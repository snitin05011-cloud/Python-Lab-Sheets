# Program to update the value of a key in a dictionary
d = {"a": 10, "b": 20, "c": 30}
print("Current dictionary:", d)
key_to_update = input("Enter key to update: ")

if key_to_update in d:
    new_value = input("Enter new value: ")
    d[key_to_update] = new_value
    print("Dictionary after update:", d)
else:
    print("Key not found in the dictionary.")