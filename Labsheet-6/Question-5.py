# Program to remove an element from a set using remove()
my_set = {"apple", "banana", "cherry"}
print("Current set:", my_set)
item = input("Enter element to remove: ")

try:
    my_set.remove(item)
    print("Set after removal:", my_set)
except KeyError:
    print("Error: Element not found in the set.")