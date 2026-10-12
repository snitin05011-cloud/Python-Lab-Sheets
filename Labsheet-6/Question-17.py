# Program to check if two sets are disjoint
set1 = set(input("Enter elements for set 1: ").split())
set2 = set(input("Enter elements for set 2: ").split())

if set1.isdisjoint(set2):
    print("The sets are disjoint (no common elements).")
else:
    print("The sets are not disjoint.")