# Program to swap two tuples
t1 = tuple(input("Enter elements for tuple 1: ").split())
t2 = tuple(input("Enter elements for tuple 2: ").split())

print(f"Before swap -> t1: {t1}, t2: {t2}")
t1, t2 = t2, t1
print(f"After swap -> t1: {t1}, t2: {t2}")