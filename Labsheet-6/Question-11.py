# Program to find the union of two sets
set1 = set(input("Enter elements for set 1 separated by space: ").split())
set2 = set(input("Enter elements for set 2 separated by space: ").split())

union_set = set1.union(set2)
print("Union of sets:", union_set)