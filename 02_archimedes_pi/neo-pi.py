#!/usr/bin/env python
from decimal import *
from math import sqrt

# really specific settings to get the exact detail we want
# must be at precision 102 to prevent rounding errors for some reason
# (dunno if that counts anymore doe)
getcontext().prec = 102

def archimedes_pi(iterations):
    # radius is 1, diameter is 2
    side_length = Decimal(1)
    sides = Decimal(6)
    # in Python 2, you would have used xrange for this,
    # and range would have given a *list* of numbers in the range
    for i in range(iterations):
        sides *= 2  # we calculate side length with twice as many sides
        # first finding length of inner part of splitting ray,
        # knowing hypotenuse and one cathetus
        temp = Decimal(side_length) / Decimal(2)
        temp = 1 - (temp * temp)
        split_part = temp.sqrt()
        # then finding side length for next iteration,
        # knowing both catheti
        side_length = (Decimal(1 - split_part) * Decimal(1 - split_part) + Decimal(side_length / 2) * Decimal(side_length / 2)).sqrt()
        #side_length = sqrt((1 - split_part)**2 + (side_length / 2)**2)
        # print("Iteration", (i+1), "\twith sides", sides, "\tof length", side_length,
        #       "\tgives pi=", (side_length * sides) / 2)
    return (side_length * sides) / 2

pi = round(archimedes_pi(1000), 99)
#print(pi.to_eng_string()[:102])
print(pi)

# this is wroooong it's just the first that is the one true answer
min_pi = Decimal('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117068')
max_pi = Decimal('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342123846')

print(len(min_pi.to_eng_string()))

#getcontext().prec = 100

print('Diffing:')
for p in [min_pi, pi, max_pi]:
    print(p.to_eng_string()[90:102])

print('Result:')
if pi < min_pi or pi > max_pi:
    print('Failed')
else:
    print('Passed')
