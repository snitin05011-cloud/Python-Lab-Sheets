# Program to perform all basic set operations in one program
set1 = set(input("Enter elements for set 1: ").split())
set2 = set(input("Enter elements for set 2: ").split())

print("\n--- Results of Basic Set Operations ---")
print("Set 1:", set1)
print("Set 2:", set2)
print("1. Union:", set1.union(set2))
print("2. Intersection:", set1.intersection(set2))
print("3. Difference (Set1 - Set2):", set1.difference(set2))
print("4. Symmetric Difference:", set1.symmetric_difference(set2))