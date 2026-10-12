# Program to flatten a nested tuple
def flatten_tuple(t):
    flat = []
    for item in t:
        if isinstance(item, tuple):
            flat.extend(flatten_tuple(item))
        else:
            flat.append(item)
    return tuple(flat)

nested = ((1, 2), (3, 4, 5), (6,))
print("Original nested tuple:", nested)
print("Flattened tuple:", flatten_tuple(nested))