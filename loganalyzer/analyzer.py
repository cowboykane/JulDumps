import argparse, logging, os, shutil
from pathlib import Path

# Log Analyzer CLI Project 

parser = argparse.ArgumentParser(
    description="Scanning log files for specific levels")


# CLI Arguments
parser.add_argument("--folder", required=True)
parser.add_argument("--level", required=True)

# Parsing the elements
args = parser.parse_args()

folder = Path(args.folder)

print(f"Scanning folder: {folder}")
print(f"Searching for log level: {args.level}")