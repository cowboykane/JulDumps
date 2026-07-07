# arg shit

import argparse 

# They should all be in different files but guess who has 
# the time for that? Right


# Greeting CLI

parser = argparse.ArgumentParser() # Createsparser menu 
parser.add_argument("--name") # Adds optional flag

args = parser.parse_args() # Pull terminal data into args container

greeting = f"Hello, {args.name}" # Access name variable 
print(greeting)


# Server Information Tool

parser = argparse.ArgumentParser()

parser.add_argument("--server")
parser.add_argument("--ip")

args = parser.parse_args()

server = f"Server: {args.server}"
ip = f"IP Address: {args.ip}"

print(server)
print(ip)


# Age Checker 

parser = argparse.ArgumentParser()

parser.add_argument("--name", default="Guest")
parser.add_argument("--age", type=int, required=True)

args = parser.parse_args()

if args.age >= 18:
    print(f"{args.name} is an adult.")
else:
    print(f"{args.name} is a minor.")



# Debug Mode

args = parser.parse_args()

if args.debug:
    print("Debug Mode Enabled")
else:
    print("Running Normally")