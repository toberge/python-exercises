#!/usr/bin/env python

name = input("Your name, please: ").strip()

if len(name) == 0:
    print("You gave no name.")
    exit(1)

initials = ""
for i in name.split():
    initials += i[0]

print(initials)
print("Hello %s, welcome to Python programming!" % name)
