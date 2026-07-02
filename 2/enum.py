# quick diagnostic test 


"""# 1 

numbers = [x for x in range(1, 16)]
print(numbers)

# 2

num_mult = [x * 3 for x in numbers]
print(num_mult)

numbers = list(range(1, 21))

# 3

div_four = [x for x in numbers if x % 4 == 0]
print(div_four)


# 4 

users = ["alice", "bob", "charlie", "david"]

cap_users = [x.capitalize() for x in users]
print(cap_users)

# 5 

logs = [
    "INFO Login",
    "ERROR Disk Full",
    "WARNING CPU High",
    "ERROR Timeout",
    "INFO Logout"
]

levels = [line.split()[0] for line in logs]
print(levels)
"""

# Enumerate

servers = [
    "web01",
    "web02",
    "db01"
]

for num, server in enumerate(servers, start=1):
    print(f"Checking server {num}: {server}")
print()   



fruits = ["apple", "banana", "orange", "grape"]

for num, fruit in enumerate(fruits, start=1):
    print(f"{num}. {fruits}")
print()

users = ["Alex", "Bob", "Charlie", "David"]

for num, user in enumerate(users, start=0):
    print(f"User {num}: {users}")
print()


errors = [
    "Disk Full",
    "Connection Timeout",
    "Permission Denied"
]

for num, error in enumerate(errors, start=1):
    print(f"ERROR {num}: {errors}")