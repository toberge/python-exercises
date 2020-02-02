## Imports here:
import os
import re
import sys
import string
from collections import Counter

## Part 1 - Listing files
#
def getfilelist(pathname):
    # Get full path
    cwd = os.getcwd()
    # Enter directory
    os.chdir(pathname)
    files = []

    # Recursively scan directories for files
    for entry in os.scandir():
        if entry.is_file() and re.match(r'.+\.txt', entry.name):
            # Add file to list
            files.append('./' + pathname + '/' + entry.name)
        elif entry.is_dir():
            # Must be a folder, recurse and append
            os.chdir(cwd)
            files.extend(getfilelist(pathname + '/' + entry.name))
    os.chdir(cwd)

    return sorted(files)


# Graveyard of old patterns
# split_pattern = '[\\s_' + string.punctuation.replace('.', '\\.') + ']+'
# pattern = '[^' + string.letters + ']'
# pattern = r'[\s_\W]+'
# pattern = r'[\s_\.,;:!?]+'

# Splitting at non-alphanumeric values
split_pattern = r'[^a-zA-Z0-9]+'

## Part 2 - Dictionary of word frequencies
#
def getwordfreqs(filename):
    freqs = Counter()

    # Open file (not using os.open, mind you)
    # Using with to automatically close it
    with open(filename, 'r') as file:
        # Iterate through it
        for line in file:
            line = line.rstrip().lower()
            # Split into words then iterate
            for word in re.split(split_pattern, line):
                # Increment frequency of this word if not empty
                if word:
                    freqs[word] += 1

    return freqs



## Part 3 - Most frequent words common to all dictionaries
#
# TODO fasit ['and', 'of', 'the', 'to'] but I get 20 words!
def getcommonwords(dicts):
    common = set()

    for freqs in dicts:
        # Look through the most common words
        for pair in freqs.most_common(3):
            present = True
            # If they are present in the top 10 of
            # all the other dictionaries, add them
            for other_freqs in dicts:
                words = []
                # Creating a list of top 10 words
                for thing in other_freqs.most_common(10):
                    words.append(thing[0])
                # If not in this list, it is not present in all
                if not pair[0] in words:
                    present = False
            # Add word to set if it passed (set => no duplicates)
            if present:
                common.add(pair[0])
    
    # Return sorted list of common words
    return sorted(list(common))

# print(getwordfreqs('ovinger/05_file_and_text/test.txt'))
# print(getfilelist('ovinger/05_file_and_text/books'))

#exit(0)

    
dicts = []
# Get the list of files
for f in getfilelist(sys.argv[1]):
    # Get word frequencies
    dicts.append(getwordfreqs(f))

# Verbose result
for freqs in dicts:
    print('total', len(freqs), 'top 10:', freqs.most_common(10))

# Get common words
common = getcommonwords(dicts)
# for w in common:
    # print(w)

print(common)
print('found', len(common), 'common words')
