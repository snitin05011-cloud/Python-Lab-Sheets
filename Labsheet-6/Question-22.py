# Program to find duplicate elements in a list using a set
elements = input("Enter elements of the list separated by space: ").split()
seen = set()
duplicates = set()

for item in elements:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print("Duplicate elements found:", duplicates)