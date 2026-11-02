# Q1: Create a file and write text into it
try:
    with open("sample.txt", "w", encoding="utf-8") as f:
        f.write(input("Enter text: "))
    print("Data written successfully.")
except OSError as e:
    print("File error:", e)
