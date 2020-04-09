import re

class RLEString:
    """Stores a string
    and compresses or decompresses it
    using run-length encoding"""

    # regex patterns for validation and splitting
    NONALPHA_PATTERN = r'[^A-Za-z]+'
    ENCODED_PATTERN = r'\d+[A-Za-z]'
    
    def __init__(self, string):
        """Takes a string of _exclusively_ alphabetic characters"""
        if not string:
            raise ValueError('Empty string')
        elif re.findall(RLEString.NONALPHA_PATTERN, string):
            raise ValueError('One or more nonalphabetic char')

        self.__mystring = string
        self.__iscompressed = False
    
    def compress(self):
        """Compresses the internal string if not compressed"""
        # Should not proceed if already compressed!
        if self.__iscompressed:
            raise Exception('Already compressed')

        current = ''
        compressed = []
        for c in self.__mystring:
            # upon finding a new char
            if c != current:
                if current:
                    # add occurence count and char to list
                    compressed.append(f'{counter}{current}')
                # reset state
                counter = 1
                current = c
            else:
                # nothing new, increment occurence count
                counter += 1
        # one last addition since nothing new could have been found
        compressed.append(f'{counter}{current}')

        # Store new state
        self.__mystring = ''.join(compressed)
        self.__iscompressed = True
    
    def decompress(self):
        """Decompresses the internal string if compressed"""
        # Should not proceed if not yet compressed!
        if not self.__iscompressed:
            raise Exception('Is not compressed')

        decompressed = []
        # Find by int followed by char
        for s in re.findall(RLEString.ENCODED_PATTERN, self.__mystring):
            # Extract number from start to second last
            occurences = int(s[:-1])
            char = s[-1]
            # Decompress to repetitions of the char
            decompressed.append(char * occurences)

        # Store new state
        self.__mystring = ''.join(decompressed)
        self.__iscompressed = False

    def iscompressed(self):
        return self.__iscompressed

    def __str__(self):
        return self.__mystring

if __name__ == '__main__':
    RLEString('abcdef defgh')
    pass