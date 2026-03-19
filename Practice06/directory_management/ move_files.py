import shutil
import os

# Ensure directories exist
os.makedirs("source", exist_ok=True)
os.makedirs("destination", exist_ok=True)

# Create a sample file
with open("source/file.txt", "w") as f:
    f.write("This file will be moved.")

# Move file
shutil.move("source/file.txt", "destination/file.txt")
print("File moved.")

# Copy file back
shutil.copy("destination/file.txt", "source/file.txt")
print("File copied back.")