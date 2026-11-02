# Q6: Display only even-numbered lines
try:
    with open("sample.txt", encoding="utf-8") as f:
        for number, line in enumerate(f, 1):
            if number % 2 == 0:
                print(line, end="")
except FileNotFoundError:
    print("File not found.")
except OSError as e:
    print("File error:", e)
