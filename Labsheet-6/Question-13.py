# Program to find the difference of two sets (set1 - set2)
set1 = set(input("Enter elements for set 1 separated by space: ").split())
set2 = set(input("Enter elements for set 2 separated by space: ").split())

diff_set = set1.difference(set2)
print("Difference (Set1 - Set2):", diff_set)