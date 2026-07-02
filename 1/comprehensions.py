# Comprehension shit

# Regular code

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

sports = ["hockey", "soccer", "football", "basketball", "cricket"]

newlist = [x for x in sports if "o" in x]
print(newlist)