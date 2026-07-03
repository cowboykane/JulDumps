# 1 - Create a list of the numbers 1 through 20 using a list comprehension.

numbers_comp = [x for x in range(1, 21)]
print(numbers_comp)
print()

# 2 - Create a list where every number is divided by 2

numbers = [2, 4, 6, 8, 10]

div_comp = [x for x in numbers if x % 2 == 0]
print(div_comp)
print()


# 3 - Create a list containing only words with 5 or more letters.

words = ["apple", "banana", "kiwi", "pear", "watermelon"]

five_words = [x for x in words if len(x) == 5]
print(five_words)
print()

# 4 - Create a list containing only the names of the online servers.

servers = [
    {"name": "web01", "online": True},
    {"name": "db01", "online": False},
    {"name": "proxy01", "online": True}
]

# fail_id = [run["id"](["status"]["failed"]) for run in runs]

"""online_names = [server["name"](["offline"]) for server in servers]
print(online_names)"""


# Enumerate 

# 1 

services = [
    "nginx",
    "docker",
    "mysql"
]

for num, service in enumerate(services, start=1):
    print(f"Service {num}: {service}")
print()

# 2 

users = [
    "Alex",
    "Sarah",
    "Mike"
]

for num, user in enumerate(users, start=0):
    print(f"{num} -> {user}")
print()

# zip()

# 1

servers = [
    "web01",
    "db01",
    "proxy01"
]

ips = [
    "10.0.0.5",
    "10.0.0.10",
    "10.0.0.20"
]

for server, ip in zip(servers, ips):
    print(f"{server} - {ip}")
print()

# 2 - add enumerate 

for num, (server, ip) in enumerate(zip(servers, ips), start=1):
    print(f"{num}. {server} -> {ip}")
print()

# Sorted and Lambda

# 1 - Sort list normally

numbers = [15, 4, 9, 1, 20]

print(sorted(numbers))

# YEah got totally lost on the last few wbk

with open("3/sorted2.py", "w") as file:
    file.write("# Oh okay...")