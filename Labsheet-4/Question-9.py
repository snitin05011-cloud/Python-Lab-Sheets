# Program to flatten a nested list using recursion
def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

print("Enter a nested list structure (e.g., [1, [2, 3], [4, [5, 6]]]):")
user_input = input("Nested list: ")
try:
    nested_list = eval(user_input)
    if isinstance(nested_list, list):
        flattened = flatten(nested_list)
        print("Flattened list:", flattened)
    else:
        print("Input is not a list.")
except Exception as e:
    print("Invalid input format:", e)