# Program to convert a tuple into a string
elements = input("Enter string characters/words separated by space: ").split()
my_tuple = tuple(elements)

result_string = "".join(my_tuple)
print("Converted String (without spaces):", result_string)

space_separated = " ".join(my_tuple)
print("Converted String (with spaces):", space_separated)