# Q7_triangle_type.py
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
if a + b > c and b + c > a and c + a > b:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or c == a:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("The given sides do not form a valid triangle.")