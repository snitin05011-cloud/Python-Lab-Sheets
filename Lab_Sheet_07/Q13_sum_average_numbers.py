# Q13: Calculate sum and average of numbers stored in a file
try:
    with open("numbers.txt", encoding="utf-8") as f:
        numbers = [float(x) for x in f.read().split()]
    if numbers:
        print("Sum:", sum(numbers))
        print("Average:", sum(numbers) / len(numbers))
    else:
        print("No numbers found.")
except FileNotFoundError:
    print("numbers.txt not found.")
except ValueError:
    print("File contains invalid numeric data.")
except OSError as e:
    print("File error:", e)
