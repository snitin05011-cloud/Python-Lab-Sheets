# Program to find the product of all elements in a list
elements = input("Enter numeric elements separated by space: ").split()
lst = [float(x) for x in elements]

product = 1.0
if lst:
    for num in lst:
        product *= num
    print("Product of all elements:", product)
else:
    print("The list is empty.")