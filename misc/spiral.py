#!/usr/bin/env python3

def spiral(stairs):
    """prints a Zettai Unmei Mokushiroku-esque word spiral"""
    ws = ''
    
    print(' '.join(stairs))
    for _ in range(1, len(stairs)):
        stairs.append(stairs[0])
        ws += ' ' * (1 + len(stairs[0]))
        del stairs[0]
        print(ws + ' '.join(stairs))

if __name__ == '__main__':
    # The origin
    spiral(['mo', 'ku', 'shi'])
    spiral(['ku', 'mo', 'shi'])
    spiral(['mo', 'ku', 'shi'])
    spiral(['ku', 'mo', 'shi'])
    # Drumming on

    print()
    spiral(['eg', 'heiter', 'anne', 'knutsdotter'])
    spiral(['kari', 'er', 'mi', 'mor'])
