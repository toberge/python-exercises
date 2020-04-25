#!/usr/bin/env python3
import sys
import os
from collections import defaultdict

"""
Python for Programmers
Exam: File Magic
Done in about an hour
"""

# map of byte sequences to file type
# used to build the tree
TYPE_MAP = {
    b'\xff\xd8\xff\xe0': 'JPEG',
    bytes.fromhex('89 50 4E 47 0D 0A 1A 0A'): 'PNG',
    bytes.fromhex('49 49 2A 00'): 'TIFF',
    bytes.fromhex('47 49 46 38 39 61'): 'GIF89a'
}

class ByteNode:
    """Inner node in identification tree"""
    def __init__(self, byte: bytes):
        self.children = {}
        self.byte = byte

    def isleaf(self):
        return False

    def addchild(self, child):
        self.children[child.byte] = child
    
    def getchild(self, byte):
        try:
            return self.children[byte]
        except KeyError:
            return None
    
    def __str__(self):
        return f'{self.byte.hex()} -> {len(self.children)} children'

class TypeNode(ByteNode):
    """Leaf node in identification tree"""
    def __init__(self, byte: bytes, text):
        super().__init__(byte)
        self.type = text

    def isleaf(self):
        return True
    
    def __str__(self):
        return f'{self.byte.hex()} -> {self.type}'

# It does not matter what the root node is
root = ByteNode(0x0)

# Add nodes to the tree
for magic, filetype in TYPE_MAP.items():
    current = root
    # All n-1 first bytes as inner nodes
    for byte in magic[:-1]:
        # Convert int to byte...
        byte = byte.to_bytes(1, sys.byteorder)
        # Each byte in the sequence becomes a node
        newnode = current.getchild(byte)
        # If not already present, add it
        if not newnode:
            newnode = ByteNode(byte)
            current.addchild(newnode)
        current = newnode
        #print(current)
    # lastly, add the type
    typenode = TypeNode(magic[-1].to_bytes(1, sys.byteorder), filetype)
    current.addchild(typenode)
    #print(typenode, '\n')

# Walk tree based on bytes from file
def walk_tree(file) -> str:
    current: ByteNode = root
    # Read from file, one byte at a time
    while file.readable():
        byte = file.read(1)
        # Attempt to find next node
        current = current.getchild(byte)

        # If no more nodes are found, unknown type
        if not current:
            return 'UNKNOWN'
        # If a TypeNode is found, return the type
        elif current.isleaf():
            return current.type
    else:
        return 'UNKNOWN'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No files specified')
        exit(1)
    
    files = sys.argv[1:]

    filemap = defaultdict(list)

    # Part 1: Identify file types
    for filename in files:
        # Open each file and identify type
        try:
            with open(filename, 'rb') as file:
                filetype = walk_tree(file)
                # Add file to type list
                filemap[filetype].append(filename)
                print(f'File {filename} is of type {filetype}')
        except OSError as e:
            print(f'Problem reading file {filename}')

    # Part 2: Create directories and move files
    for filetype, array in filemap.items():
        os.mkdir(f'sorted/{filetype}')
        for file in array:
            os.rename(file, f'sorted/{filetype}/{file}')
    