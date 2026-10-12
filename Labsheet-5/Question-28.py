# Program to find repeated items in a tuple
elements = input("Enter elements separated by space: ").split()
my_tuple = tuple(elements)

repeated = set(x for x in my_tuple if my_tuple.count(x) > 1)
print("Repeated items:", tuple(repeated))