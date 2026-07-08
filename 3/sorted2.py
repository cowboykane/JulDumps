# Sorting stuff

# sorting 101...

numbers = [9, 4, 6, 2]
print(sorted(numbers))

names = [
    "Sebastian",
    "Kane",
    "Yolk"
]

print(sorted(names))

# Reversing

numbers = [8, 3, 12, 1, 6]

print(sorted(numbers, reverse=True))

print()

numbers = [12, 7, 20, 3, 15]

print(sorted(numbers, reverse=True))
print(sorted(numbers))

print()

employees = [
    {"name":"John","salary":50000},
    {"name":"Sarah","salary":70000},
    {"name":"Mike","salary":60000}
]

def get_salary(employee):
    return employee["salary"]

sorted_employees = sorted(employees, key=get_salary)
print(sorted_employees)

