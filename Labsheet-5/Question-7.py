# Program to count the occurrences of an element in a tuple
elements = input("Enter elements separated by space: ").split()
my_tuple = tuple(elements)
target = input("Enter element to count: ")

count = my_tuple.count(target)
print(f"'{target}' occurs {count} time(s) in the tuple.")