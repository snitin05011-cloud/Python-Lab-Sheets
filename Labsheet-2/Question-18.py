# Q18_fibonacci.py
n = int(input("Enter number of terms: "))
a, b = 0, 1
print(f"Fibonacci series up to {n} terms:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()