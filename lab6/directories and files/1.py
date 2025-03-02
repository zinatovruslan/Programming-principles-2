#1
import os

path = input("Enter the directory path: ")

if os.path.exists(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    print("Directories:", directories)

    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print("Files:", files)

    all_items = os.listdir(path)
    print("All items:", all_items)
else:
    print("Invalid path! Directory does not exist.")

#2
import os

path = input("Enter the file or directory path: ")

print("Exists:", os.path.exists(path))
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))

#3
import os

path = input("Enter the file path: ")

if os.path.exists(path):
    print("File exists!")
    print("Directory portion:", os.path.dirname(path))
    print("Filename portion:", os.path.basename(path))
else:
    print("Path does not exist.")

#4
file_path = input("Enter the file path: ")

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        line_count = len(file.readlines())
    print("Number of lines:", line_count)
else:
    print("File does not exist.")

#5
file_path = input("Enter the filename to save data: ")

data = input("Enter items separated by commas: ").split(",")  

with open(file_path, "w") as file:
    for item in data:
        file.write(item.strip() + "\n")  

print(f"Data has been written to {file_path}.")

#6
import string

for letter in string.ascii_uppercase:  
    with open(f"{letter}.txt", "w") as file:
        file.write(f"This is {letter}.txt")

print("26 files (A-Z) have been created.")

#7
source = input("Enter the source file path: ")
destination = input("Enter the destination file path: ")

if os.path.exists(source):
    with open(source, "r") as src, open(destination, "w") as dest:
        dest.write(src.read())
    print(f"File copied from {source} to {destination}.")
else:
    print("Source file does not exist.")

#8import os

file_path = input("Enter the file path to delete: ")

if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):  
        os.remove(file_path)
        print("File deleted successfully.")
    else:
        print("No permission to delete this file.")
else:
    print("File does not exist.")
