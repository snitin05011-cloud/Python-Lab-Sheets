# Program to check if a set is a subset of another set
set1 = set(input("Enter elements for set 1: ").split())
set2 = set(input("Enter elements for set 2: ").split())

if set1.issubset(set2):
    print("Set 1 is a subset of Set 2.")
else:
    print("Set 1 is not a subset of Set 2.")