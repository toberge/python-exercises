#!/usr/bin/env python3
import math

odds = 0
evens = 0
squares = 0

for i in range(2, 26):
    if (i % 2 == 0):
        evens += 1
    else:
        odds += 1
    
    if (math.sqrt(i).is_integer()):
        squares += 1


# four square numbers: 4, 9, 16, 25
print(squares, 'squares')
