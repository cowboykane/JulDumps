# Gotta clean up my directory afterwards so I'll run these and delete
# Excess files afterwards

from pathlib import Path

# Create a new folder without crashing the dir
"""
Path("backup").mkdir(exist_ok=True)
Path("backup/archive").mkdir(exist_ok=True)

"""

# Check if a file exits

crypto_file = Path("crypto.py")

if crypto_file.exists():
    print("File Found!")
    
# Find specific files with glob 

home_dir = Path()
print(f"Looking for files inside: {home_dir.resolve()}")

for file in home_dir.rglob("*py"):
    print(file.name)
    
