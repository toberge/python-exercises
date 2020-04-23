#!/usr/bin/env python3
import sys
import os
import re
from collections import Counter

"""
this thing will handle the tex
"""

GRAPHIC_EXTENSTIONS = {'eps', 'tif', 'png', 'jpg'}
# all uncommented lines with filenames with these extensions
LATEX_PATTERN = f'\s*[^%].+\.({"|".join(GRAPHIC_EXTENSTIONS)}).*'

def getfiles(path: str) -> list:
    files = []
    for item in os.scandir(path):
        if item.is_dir():
            files.extend(getfiles(f'{item.name}'))
        else:
            files.append(f'{item.name}')
    return files

def searchlatex(path: str) -> list:
    filenames = []
    with open(path, 'r') as latex:
        for line in latex.readlines():
            if re.match(LATEX_PATTERN, line):
                line = line.split('{')[-1][:-3]
                print(line)
                filenames.append(line)
    return filenames

if __name__ == '__main__':
    if len(sys.argv) == 2:
        path = sys.arg[2]
    else:
        path = './examFiles_43590097_1556880827788'
    # List all files
    files = getfiles(path)
    # List all graphics files
    graphics_files = [f for f in files if f[-3:].lower() in GRAPHIC_EXTENSTIONS]

    # Open the .tex file(s) and search...
    # okay, it's probably just GSGradientFromColor.tex
    #latex_files = []
    #for texfile in (f for f in files if f[-3:] == 'tex'):
        #print(texfile)
        #latex_files.extend(searchlatex(f'{path}/{texfile}'))
    latex_files = searchlatex(f'{path}/GSGradientFromColor.tex')

    # mkdirs
    for folder in ['dump'] + list(GRAPHIC_EXTENSTIONS):
        print('mk', folder)

    folder_counts = Counter()

    for f in graphics_files:
        if f in latex_files:
            # Move the rest to their file extension's baluba.
            folder = f[-3:].lower()
        else:
            # Move graphics files NOT in .tex files to dump
            folder = 'dump'
        print(f'move {f} to {folder}')
        # make folder if not yet made
        if folder not in folder_counts:
            os.mkdir(f'{path}/{folder}')
        # mv the file
        os.rename(f'{path}/{f}', f'{path}/{folder}/{f}')
        folder_counts[folder] += 1

    # Print # graphics files and # moved to each folder
    print(f'Total files moved: {len(graphics_files)}')
    for k, v in folder_counts.items():
        print('Moved', v, 'files to', k)

