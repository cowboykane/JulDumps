# Lambda

def add (x, y):
    return x + y
print(add(5, 10))

print((lambda x, y: x + y) (4, 5))

# Anonymous functions are made to be passd into higher order functions. 

def square(x):
    return x * x
square = lambda x: x * x
print(square(5))


servers = [
    {"name": "web-01", "cpu": 82},
    {"name": "db-01", "cpu": 45},
    {"name": "cache-01", "cpu": 91},
]

sorted(servers, key=lambda x: x["cpu"])
print(servers)

servers = [
    {"name": "web-01", "cpu": 82, "ram_gb": 16, "region": "eu"},
    {"name": "db-01", "cpu": 45, "ram_gb": 64, "region": "us"},
    {"name": "cache-01", "cpu": 91, "ram_gb": 8, "region": "eu"},
    {"name": "api-01", "cpu": 60, "ram_gb": 32, "region": "us"},
]

# TODO: 1. Sort servers by "ram_gb", in ascending order. store result in "by_ram"

by_ram = sorted(servers, key=lambda x: x["ram_gb"])
print(by_ram)


# TODO: 2. Sort servers by "cpu" in descending  order. Store result in by_cpu_desc

by_cpu_desc = sorted(servers, reverse=True, key = lambda x: x["cpu"])
print(by_cpu_desc)


# TODO: 3. Sort servers by "region" in alphabetically. For servers in the same region.
# break the tie by cpu descending. 

sorted(servers, key=lambda x: x["region"])