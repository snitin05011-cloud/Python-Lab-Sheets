# Q5_remove_duplicates.py
s = input("Enter a string: ")
unique_str = ""
for char in s:
    if char not in unique_str:
        unique_str += char
print(f"String after removing duplicates: {unique_str}")