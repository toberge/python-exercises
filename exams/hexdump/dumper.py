#!/usr/bin/env python3

"""
Python for Programmers
Exam: hexdump

Repeat lines an amount of times.
Should be simple enough.
"""

import math
import sys

STEP = 16 # address jump

def readbin(filename):
    address = 0x0
    lastline = 'nah'
    should_repeat = False
    # outfile...
    outfilename = f'{filename.replace(".bin.hex", "")}-expanded.hex' 
    with open(filename, 'r') as infile: #, open(outfilename, 'w') as outfile:
        for line in infile:
            if line.strip() == '*':
                should_repeat = True
                continue

            next_address = int(line.split()[0], 16)

            if should_repeat:
                # repeat lastline a given amount of times...
                # repeat _blindly_ until rest
                for i in range(address, next_address - next_address % STEP, STEP):
                    print('%07x %s' % (i, lastline))

                if next_address % STEP != 0:
                    # then repeat only leftover stuff
                    # from start of tokens to 
                    count = math.ceil((next_address % STEP) / 4)
                    print('%07x' % (next_address - next_address % STEP), end='')
                    for s in lastline.split()[:count+1]:
                        print(' ' + s, end='')
                    print()
                    should_repeat = False

            # remember address and line 4 next time
            address = next_address
            lastline = ' '.join(line.split()[1:])
            # print *this* line
            print(line, end='')

if __name__ == '__main__':
    for filename in sys.argv[1:]:
        readbin(filename)
        
