# Program to remove duplicate values from a dictionary
n = int(input("Enter number of elements: "))
d = {}
for _ in range(n):
    k = input("Enter key: ")
    v = input("Enter value: ")
    d[k] = v

unique_dict = {}
seen_values = set()

for k, v in d.items():
    if v not in seen_values:
        unique_dict[k] = v
        seen_values.add(v)

print("Dictionary after removing duplicate values:", unique_dict)