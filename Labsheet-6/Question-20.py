# Program to find the Cartesian product of two sets
set1 = set(input("Enter elements for set 1: ").split())
set2 = set(input("Enter elements for set 2: ").split())

cartesian_product = {(x, y) for x in set1 for y in set2}
print("Cartesian Product:", cartesian_product)