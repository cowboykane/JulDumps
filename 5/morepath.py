from pathlib import Path

path = Path("logs") # Becomes a path object
print(path)

print(Path.cwd()) # Prints current working directory. Linux CLI

print(Path.home()) # Prints home directroy

log_file = Path("logs") / "today.log" # Join paths
print(log_file)

print(path.exists()) # check if Path exists

# Path("reports").mkdir(exist_ok=True) # Create directory and prevent crashing

path = Path("server.log") 
print(path.is_file()) # Check if path is a file

path = Path("logs")
print(path.is_dir()) # Check if path is a directory

log_folder = Path("2")

for file in log_folder.glob("*py"): # Find files
    print(file)