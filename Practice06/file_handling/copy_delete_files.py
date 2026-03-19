import shutil
import os

# Append new line
with open("sample.txt", "a") as f:
    f.write("Appended line.\n")

# Copy file
shutil.copy("sample.txt", "backup_sample.txt")
print("File copied.")

# Delete file safely
if os.path.exists("backup_sample.txt"):
    os.remove("backup_sample.txt")
    print("Backup file deleted.")
else:
    print("File does not exist.")