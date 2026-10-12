# Program to create the power set of a given set
from itertools import combinations

elements = input("Enter elements of the set separated by space: ").split()
my_set = set(elements)
lst = list(my_set)
power_set = []

for r in range(len(lst) + 1):
    for combo in combinations(lst, r):
        power_set.append(set(combo))

print("Power Set:")
for s in power_set:
    print(s)