# Program to sort a dictionary by values
n = int(input("Enter number of elements: "))
d = {}
for _ in range(n):
    k = input("Enter key: ")
    v = input("Enter value (numeric for proper sort): ")
    try:
        v = float(v)
    except ValueError:
        pass
    d[k] = v

sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
print("Dictionary sorted by values:", sorted_dict)