# Program to find common elements between two tuples
t1 = tuple(input("Enter elements for tuple 1: ").split())
t2 = tuple(input("Enter elements for tuple 2: ").split())

common = tuple(set(t1).intersection(set(t2)))
print("Common elements:", common)