# Program to separate even and odd numbers from a list
elements = input("Enter integers separated by space: ").split()
even_list = []
odd_list = []

for x in elements:
    num = int(x)
    if num % 2 == 0: 
        even_list.append(num)
    else:
        odd_list.append(num)

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)