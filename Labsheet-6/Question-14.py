# Program to find the symmetric difference of two sets
set1 = set(input("Enter elements for set 1 separated by space: ").split())
set2 = set(input("Enter elements for set 2 separated by space: ").split())

sym_diff_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", sym_diff_set)