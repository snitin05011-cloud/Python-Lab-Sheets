# Program to check if an element exists in a tuple
elements = input("Enter elements separated by space: ").split()
my_tuple = tuple(elements)
search_item = input("Enter element to search: ")

if search_item in my_tuple:
    print(f"'{search_item}' exists in the tuple.")
else:
    print(f"'{search_item}' does not exist in the tuple.")