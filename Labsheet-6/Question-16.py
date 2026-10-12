# Program to check if a set is a superset of another set
set1 = set(input("Enter elements for set 1: ").split())
set2 = set(input("Enter elements for set 2: ").split())

if set1.issuperset(set2):
    print("Set 1 is a superset of Set 2.")
else:
    print("Set 1 is not a superset of Set 2.")