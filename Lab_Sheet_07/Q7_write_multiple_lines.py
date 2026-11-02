# Q7: Write multiple lines entered by the user
try:
    count = int(input("How many lines? "))
    with open("multiple_lines.txt", "w", encoding="utf-8") as f:
        for i in range(count):
            f.write(input(f"Enter line {i + 1}: ") + "\n")
    print("Lines written successfully.")
except ValueError:
    print("Enter a valid number.")
except OSError as e:
    print("File error:", e)
