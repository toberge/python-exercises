#!/usr/bin/env python
import math

'''
pi.py

Letting radius of our symmetrical polygon be 1 and starting with 6 sides,
we approximate pi by calculating and finally applying the circumference after a number of iterations.

Simple use of the Pythagorean theorem leads to the current iteration's side length.

Seems to end up at 3.1415926535897936 after 25 iterations and beyond,
'till side_length becomes too small for Python to handle and we get 0.0

According to Wikipedia's estimate, the last digit is off (should be 2),
but this is to be expected with the somewhat rough granularity
of standard floating point data types.

Function returns pi = circumference / diameter
'''


def archimedes_pi(iterations):
    # radius is 1, diameter is 2
    side_length = 1
    sides = 6
    # in Python 2, you would have used xrange for this,
    # and range would have given a *list* of numbers in the range
    for i in range(iterations):
        sides *= 2  # we calculate side length with twice as many sides
        # first finding length of inner part of splitting ray,
        # knowing hypotenuse and one cathetus
        split_part = math.sqrt(1 - (side_length / 2)**2)
        # then finding side length for next iteration,
        # knowing both catheti
        side_length = math.sqrt((1 - split_part)**2 + (side_length / 2)**2)
        # print("Iteration", (i+1), "\twith sides", sides, "\tof length", side_length,
        #       "\tgives pi=", (side_length * sides) / 2)
    return (side_length * sides) / 2


print(archimedes_pi(10011))
