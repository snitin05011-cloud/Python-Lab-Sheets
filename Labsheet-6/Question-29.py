# Program to find maximum and minimum values in a set
elements = input("Enter numeric elements separated by space: ").split()
num_set = {float(x) for x in elements}

if num_set:
    print("Maximum value:", max(num_set))
    print("Minimum value:", min(num_set))
else:
    print("The set is empty.")