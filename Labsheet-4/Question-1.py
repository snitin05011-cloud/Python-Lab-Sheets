# Program to find the sum and average of elements in a list
elements = input("Enter elements of the list separated by space: ").split()
lst = [float(x) for x in elements]

total_sum = 0.0
count = 0

for num in lst:
    total_sum += num
    count += 1

if count > 0:
    average = total_sum / count
    print(f"Sum of elements: {total_sum}")
    print(f"Average of elements: {average}")
else:
    print("The list is empty.")