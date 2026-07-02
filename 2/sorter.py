

# Return only py files using list comprehension
print("-- SUPER BASICS --")

files = ["main.py", "README.md", "utils.py", "config.yaml", "test_app.py"]

pylist = []

for x in files:
    if x.endswith(".py"):
        pylist.append(x)

print(pylist)

pylist_comp = [x for x in files if x.endswith(".py")]
print(pylist_comp)

print()

# Price filtering 

prices = [12.50, 65.00, 105.99, 8.25, 50.00, 95.50]

expensive_prices = []

for p in prices:
    if p > 50:
        expensive_prices.append(p)

print(expensive_prices)

expensive_prices_comp = [p for p in prices if p > 50]
print(expensive_prices_comp)

print()

# Taxes


prices = [12.50, 65.00, 105.99, 8.25, 50.00, 95.50]

taxes = []

for p in prices:
    taxes.append(p * 0.10)

print(taxes)

taxes_comp = [p * 0.10 for p in prices]
print(taxes_comp)

print()

# Price Labeling

prices = [12.50, 65.00, 105.99, 8.25, 50.00, 95.50]

labels = []

for p in prices:
    if p > 50:
        labels.append("Expensive")
    else:
        labels.append("Cheap")

print(labels)
# Expected Output: ['Cheap', 'Expensive', 'Expensive', 'Cheap', 'Cheap', 'Expensive']

labels_comp = ["Expensive" if p > 50 else "Cheap" for p in prices]
print(labels_comp)


print()
print("-- DICTIONARY COMPREHENSION --")

# Scenario: key = empoyee ID, Value = name
# Create a new list containing only the names of employees where  their ID > 100

employees = {
    99: "Alice",
    101: "Bob",
    102: "Charlie",
    95: "David"
}

high_id_names = []

for k, v in employees.items():
    if k > 100:
        high_id_names.append(v)

print(high_id_names)

high_id_names_comp = [v for k, v in employees.items() if k > 100]
print(high_id_names)

print()

# WHATEVERRRRR 

files = ["main.py", "README.md", "utils.py", "config.yaml", "test_app.py"]

pylist = [x for x in files if x.endswith(".py")]
print(pylist)


# return only status values 

runs = [
    {"id": 1, "status": "success"},
    {"id": 2, "status": "failed"},
    {"id": 3, "status": "success"},
]

all_status = [run["status"] for run in runs]
print(all_status)

# return id of failed runs 

fail_id = [run["id"](["status"]["failed"]) for run in runs]




# return name values 

servers = [
    {"name": "web-01", "region": "us-east"},
    {"name": "web-02", "region": "us-west"},
    {"name": "db-01", "region": "us-east"},
]

all_names = [server["name"] for server in servers]
print(all_names)
