# Program to rotate a list by n positions
elements = input("Enter elements of the list separated by space: ").split()
n = int(input("Enter number of positions to rotate: "))
direction = input("Enter direction (left/right): ").strip().lower()

length = len(elements)
if length > 0:
    n = n % length  # Handle rotations greater than list length
    if direction == "left":
        rotated_list = elements[n:] + elements[:n]
    else:  # right rotation
        rotated_list = elements[-n:] + elements[:-n]
    print("Rotated list:", rotated_list)
else:
    print("The list is empty.")