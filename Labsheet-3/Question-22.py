# Program to sort a list of integers in ascending and descending order
elements = input("Enter integers separated by space: ").split()
lst = [int(x) for x in elements]

print("Ascending order:", sorted(lst))
print("Descending order:", sorted(lst, reverse=True))