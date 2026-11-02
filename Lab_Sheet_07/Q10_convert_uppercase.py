# Q10: Display file content in uppercase
try:
    with open("sample.txt", encoding="utf-8") as f:
        print(f.read().upper())
except FileNotFoundError:
    print("File not found.")
except OSError as e:
    print("File error:", e)
