#!/usr/bin/env python3
import sys # for args and stdin
import argparse

def print_usage():
    print('Usage: tee [-a] [FILE]\n-a: Append to file\nIf -a is set FILE must be present')

def read_and_output(outfile=None):
    """Read from stdin and write to stdout + file if any"""
    for line in sys.stdin:
        # Using write() to avoid having end=''
        sys.stdout.write(line)
        if outfile:
            outfile.write(line)

if __name__ == '__main__':
    # Set default values for variables...
    file_mode = 'w+'
    filename = ''
    # Check for the only cmd-option and wether a file is provided or not
    # (this is simple enough that argparser is not needed)
    if len(sys.argv) == 3 and sys.argv[1] == '-a':
        # Append!
        file_mode = 'a+'
        filename = sys.argv[2]
    elif len(sys.argv) == 2:
        # Overwrite!
        filename = sys.argv[1]
    elif len(sys.argv) != 1:
        # Without a file, there should be no arguments!
        print_usage()
        exit(1)
    
    # Write to file if and only if a file is provided!
    if filename:
        try:
            # try opening file (with automatically closes it afterwards)
            with open(filename, file_mode) as file:
                read_and_output(outfile=file)
        except OSError as error:
            # This would happen if, say, the user does not have permission to access that file
            # or there is an I/O error of some kind
            print(f'Error: Could not write to file!\nReason: {error}')
            exit(1)
    else:
        # Otherwise, no file.
        read_and_output()