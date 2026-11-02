# Q2: Read the entire content of a text file
try:
    with open("sample.txt", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found. Run Q1 first.")
except OSError as e:
    print("File error:", e)
