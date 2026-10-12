# Program to unzip a list of tuples into individual lists
tuple_list = [('A', 1), ('B', 2), ('C', 3)]

list1, list2 = zip(*tuple_list)
print("List 1:", list(list1))
print("List 2:", list(list2))