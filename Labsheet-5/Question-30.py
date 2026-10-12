# Program to find the element-wise sum of two tuples
t1 = tuple(float(x) for x in input("Enter numeric elements for tuple 1: ").split())
t2 = tuple(float(x) for x in input("Enter numeric elements for tuple 2: ").split())

if len(t1) == len(t2):
    sum_tuple = tuple(a + b for a, b in zip(t1, t2))
    print("Element-wise sum tuple:", sum_tuple)
else:
    print("Error: Both tuples must have the same length for element-wise addition.")