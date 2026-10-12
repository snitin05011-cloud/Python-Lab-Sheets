# Program to remove an element from a set using discard()
my_set = {"apple", "banana", "cherry"}
print("Current set:", my_set)
item = input("Enter element to discard: ")

my_set.discard(item)  # Does not raise an error if element is missing
print("Set after discard:", my_set)