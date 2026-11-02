# Q17: Remove blank lines from a file
try:
    with open("sample.txt", encoding="utf-8") as f:
        lines = f.readlines()
    with open("sample.txt", "w", encoding="utf-8") as f:
        f.writelines(line for line in lines if line.strip())
    print("Blank lines removed.")
except FileNotFoundError:
    print("File not found.")
except OSError as e:
    print("File error:", e)
