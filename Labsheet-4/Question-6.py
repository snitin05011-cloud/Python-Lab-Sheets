# Program to split a list into two halves
elements = input("Enter elements of the list separated by space: ").split()
length = len(elements)
mid = length // 2

first_half = elements[:mid]
second_half = elements[mid:]

print("First half:", first_half)
print("Second half:", second_half)