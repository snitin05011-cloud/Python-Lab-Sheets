# Q8_substring.py
main_str = input("Enter the main string: ")
sub_str = input("Enter the substring to check: ")
if sub_str in main_str:
    print(f"'{sub_str}' is found inside the string.")
else:
    print(f"'{sub_str}' is not found inside the string.")