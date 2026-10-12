# Program to convert two lists into a dictionary
keys = input("Enter keys separated by space: ").split()
values = input("Enter values separated by space: ").split()

if len(keys) == len(values):
    result_dict = {}
    for i in range(len(keys)):
        result_dict[keys[i]] = values[i]
    print("Created dictionary:", result_dict)
else:
    print("Error: Both lists must have the same number of elements.")