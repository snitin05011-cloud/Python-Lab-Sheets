# Program to merge two dictionaries into one
dict1 = {}
n1 = int(input("Enter number of elements in first dictionary: "))
for _ in range(n1):
    k = input("Enter key: ")
    v = input("Enter value: ")
    dict1[k] = v

dict2 = {}
n2 = int(input("Enter number of elements in second dictionary: "))
for _ in range(n2):
    k = input("Enter key: ")
    v = input("Enter value: ")
    dict2[k] = v

merged_dict = dict1.copy()
for k, v in dict2.items():
    merged_dict[k] = v

print("Merged dictionary:", merged_dict)