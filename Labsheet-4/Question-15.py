# Program to sort a dictionary by keys
n = int(input("Enter number of elements: "))
d = {}
for _ in range(n):
    k = input("Enter key: ")
    v = input("Enter value: ")
    d[k] = v

sorted_dict = dict(sorted(d.items()))
print("Dictionary sorted by keys:", sorted_dict)