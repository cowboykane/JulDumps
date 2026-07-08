# my cicciolina.. everything is physical....

from pathlib import Path

path = Path()

current_dir = path.cwd()

if current_dir.exists():
    print(f"Folder exists in {current_dir}")
    print(current_dir.stat().st_size)
else:
    print("Error, folder doesn't exist.")

for file in current_dir.glob("*.log"):
    print(file)
    
#Lets try folder-specifics 

folder_choice = input("Insert a folder to search: ")
extension = input("Insert an extension to search: ")
extension = "*" + extension

py_folder = Path(folder_choice)

for num, file in enumerate(py_folder.glob(extension), start=1):
    print(f"{num}: {file}")

