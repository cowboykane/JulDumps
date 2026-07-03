# Comprehension shit

# Regular code

import os, shutil

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

sports = ["hockey", "soccer", "football", "basketball", "cricket"]

newlist = [x for x in sports if "o" in x]
print(newlist)

os.makedirs("3", exist_ok=True)

with open("3/review.py", "w") as f:
    f.write("# wot")
