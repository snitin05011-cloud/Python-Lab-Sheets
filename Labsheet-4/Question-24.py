# Program to invert a dictionary (keys become values and values become keys)
n = int(input("Enter number of elements: "))
d = {}
for _ in range(n):
    k = input("Enter key: ")
    v = input("Enter value: ")
    d[k] = v

inverted_dict = {}
for k, v in d.items():
    inverted_dict[v] = k

print("Inverted dictionary:", inverted_dict)