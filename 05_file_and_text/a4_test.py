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



# TODO avoid \W and go the more sophisticated route
split_pattern = '[\\s_' + string.punctuation.replace('.', '\\.') + ']+'
# pattern = '[^' + string.letters + ']'
# pattern = r'[\s_\W]+'
# pattern = r'[\s_\.,;:!?]+'

## Part 2 - Dictionary of word frequencies
#
# TODO too many words are found
# should be 5714 words in some dictionary that is 5718 with my code
def getwordfreqs(filename):
    freqs = Counter()

    # Open file (not using os.open, mind you)
    with open(filename, 'r') as file:
        # Iterate through it
        
        for line in file:
            line = line.rstrip().lower()
            for word in re.split(split_pattern, line):
                # Set value if not present
                # freqs.setdefault(word, 0)
                # Increment frequency of this word
                #if re.search('[]') == None: or something
                # TODO add check for non-alphanumeric values
                # empty string is falsy, yay!
                if word.isalnum():
                    freqs[word] += 1

    return freqs



## Part 3 - Most frequent words common to all dictionaries
#
# TODO fasit ['and', 'of', 'the', 'to'] but I get 20 words!
def getcommonwords(dicts):
    common = Counter()

    for freqs in dicts:
        # Look through the most common words
        for pair in freqs.most_common(10):
            present = True
            # If they are present in all the other dictionaries, add them
            for other_freqs in dicts:
                if not pair[0] in other_freqs:
                    present = False
            if present:
                common[pair[0]] += pair[1]
                    

    # for freqs in dicts:
    #     for pair in freqs.most_common(10):
    #         common[pair[0]] += pair[1]

    #print(common)
    
    return list(common)

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
for w in common:
    print(w)

print('found', len(common), 'common words')
