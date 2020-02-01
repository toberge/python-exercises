#!/usr/bin/env python
import os

sentence_list = ["hello", "you", "are", "bad", "really"]
sentence_list[3] = sentence_list[4]
sentence_list[4] = "bad"

print(sentence_list[0:3])  # up till 3
print(' '.join(sentence_list))
print(' '.join(sentence_list[0:3]), "not too bad")

# we have dicts:
le_dict = {
    'rose': 'violet',
    'wisteria': 'red',
    'sunflower': 'black',
}

print(le_dict.keys(), le_dict.values())

le_string = "Hello from the other side"

print("I am " + le_string[6:len(le_string)])
print(le_string[:-4] + "world")
print('a' + le_string[-4:])
print(le_string[:6] + "there")

print("Only nums?", le_string.isalnum())
print("Only nums?", '23'.isalnum())

file = open("test.txt", "ab+")  # appends and creates file, wb writes?
print("Opened", file.name, "with mode", file.mode)

file.write(bytes("This will be the content of the file", 'UTF-8'))

file.close()

file = open("test.txt", "r+")  # read&write
print(file.read(4))
print(file.read())
file.close()

os.remove("test.txt")
