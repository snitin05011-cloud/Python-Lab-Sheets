# Program to count distinct elements from a list using a set
elements = input("Enter elements of the list separated by space: ").split()
distinct_set = set(elements)

print("List of elements:", elements)
print(f"Number of distinct elements: {len(distinct_set)}")