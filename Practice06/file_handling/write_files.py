# Create a file and write sample data

with open("sample.txt", "w") as f:
    f.write("Hello, this is a sample file.\n")
    f.write("Second line.\n")

print("File created and written successfully.")