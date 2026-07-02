# fuuuuck


people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 19},
    {"name": "Charlie", "age": 30}
]

# Use a lamba to print the age 

people = sorted(people, key=lambda person: person["age"])

print(people)