# zip()

movies = ("star wars", "coyote ugly", "pulp fiction")
books = ("harrow the ninth", "gideon the ninth", "no longer human")

for movies, books, in zip(movies, books):
    print(movies, books)
print()



animals = ["Dog", "Cat", "Bird"]
sounds = ["Bark", "Meow", "Tweet"]

for animal, sound, in zip(animals, sounds):
    print(f"{animal} says {sound}")
print()
    
    

students = ["Alex", "Sarah", "Mike"]
grades = [88, 94, 76]

for student, grade, in zip(students, grades):
    print(f"{student}: {grade}")
print()



servers = [
    "web01",
    "db01",
    "proxy01"
]

ips = [
    "192.168.1.10",
    "192.168.1.20",
    "192.168.1.30"
]

for num, (server, ip), in enumerate(zip(servers, ips), start=1):
    print(f"Server {num}: {server} -> {ip}")