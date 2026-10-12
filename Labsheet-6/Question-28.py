# Program to create a frozenset and demonstrate its properties
# Frozenset is immutable and hashable (can be used as dictionary keys)
elements = input("Enter elements for the frozenset separated by space: ").split()
fs = frozenset(elements)

print("Created Frozenset:", fs)
print("Type:", type(fs))

# Demonstrating immutability (uncommenting below line raises AttributeError)
try:
    fs.add("newItem")
except AttributeError as e:
    print("Error demonstrated successfully:", e)