# Program to find the difference between two tuples (t1 - t2)
t1 = tuple(input("Enter elements for tuple 1: ").split())
t2 = tuple(input("Enter elements for tuple 2: ").split())

difference = tuple(item for item in t1 if item not in t2)
print("Tuple Difference (t1 - t2):", difference)