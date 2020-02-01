#!/usr/bin/env python3
vowels = 'aeiou'
found = ''

complete = False
tries = 0
fors = 0
while not complete:
    str = input('ur streng: ').lower()
    tries += 1
    for char in str:
        fors += 1
        if char in vowels and char not in found:
            found += char
        if len(vowels) == len(found):
            complete = True
            break

print('got all vowels after', tries, 'tries and', fors, 'processed letters')
print('order of finding:', found)

