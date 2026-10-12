# Program to check if a substring exists in a given string
main_str = input("Enter the main string: ")
sub_str = input("Enter the substring to check: ")

if sub_str in main_str:
    print("Substring exists in the main string.")
else:
    print("Substring does not exist in the main string.")