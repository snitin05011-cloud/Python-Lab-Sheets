# Program to check if an element exists in a set
my_set = {"python", "java", "c++"}
print("Current set:", my_set)
search_item = input("Enter element to search: ")

if search_item in my_set:
    print(f"'{search_item}' exists in the set.")
else:
    print(f"'{search_item}' does not exist in the set.")