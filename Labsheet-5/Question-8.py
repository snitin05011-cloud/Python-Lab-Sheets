# Program to find the index of an element in a tuple
elements = input("Enter elements separated by space: ").split()
my_tuple = tuple(elements)
target = input("Enter element to find index: ")

if target in my_tuple:
    idx = my_tuple.index(target)
    print(f"First occurrence of '{target}' is at index {idx}.")
else:
    print(f"'{target}' is not present in the tuple.")