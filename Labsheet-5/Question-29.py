# Program to check if all elements in a tuple are the same
elements = input("Enter elements separated by space: ").split()
my_tuple = tuple(elements)

if not my_tuple:
    print("The tuple is empty.")
else:
    all_same = all(x == my_tuple[0] for x in my_tuple)
    if all_same:
        print("All elements in the tuple are the same.")
    else:
        print("Not all elements in the tuple are the same.")