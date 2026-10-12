# Program to find common letters in two strings using sets
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

common_letters = set(str1).intersection(set(str2))
print("Common letters:", common_letters)