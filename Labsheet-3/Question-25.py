# Program to count the frequency of each element in a list
elements = input("Enter elements separated by space: ").split()
freq = {}

for item in elements:
    freq[item] = freq.get(item, 0) + 1

print("Element frequencies:")
for item, count in freq.items():
    print(f"'{item}': {count}")