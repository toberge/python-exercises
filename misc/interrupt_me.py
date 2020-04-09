from itertools import count, cycle
eh = 0
try:
    # infinite iterators
    for i, word in zip(count(100, 13), cycle(['cat', 'burglar', 'flashlight'])):
        eh = (i, word)
except KeyboardInterrupt as kyb:
    pass
finally:
    print(f'\nI found {eh[0]} {eh[1]}s in your closet')
