# Program to check if two strings are rotations of each other
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) == len(str2) and str2 in (str1 + str1):
    print("The strings are rotations of each other.")
else:
    print("The strings are not rotations of each other.")