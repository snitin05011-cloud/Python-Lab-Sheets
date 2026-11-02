# Q16: Display the first and last lines of a file
try:
    with open("sample.txt", encoding="utf-8") as f:
        lines = f.readlines()
    if lines:
        print("First line:", lines[0].rstrip("\n"))
        print("Last line:", lines[-1].rstrip("\n"))
    else:
        print("File is empty.")
except FileNotFoundError:
    print("File not found.")
except OSError as e:
    print("File error:", e)
