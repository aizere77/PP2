import os

# Create nested directories
os.makedirs("test_dir/sub_dir", exist_ok=True)
print("Directories created.")

# List files and folders
items = os.listdir("test_dir")
print("Contents of test_dir:", items)