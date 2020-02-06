#!/usr/bin/env python3

'''
https://www.youtube.com/watch?v=OSGv2VnC0go

just some notes about sweet&consise things in Python
'''

# after 6:43 

# Using iter() with a sentinel (stop) value!
# partial() takes function with many args + those args and creates function with no args!
things = []
for thing in iter(partial(f.read, 32), ''):
    things.append(thing)

# I know of for-else, yay

# stuff about looping over dicts, keys by default, use of iteritems() ++

###########################################

# Creating dict from 2 arrays:
keys = ['abc', 'def', 'ghi']
values = [2, 4, 9]
dictionary = dict(izip(keys, values))

# instead of setdefault: d[k] = d.get(k, 0) + 1
# that will set d[k] to zero if not present
# even better:
d1 = defaultdict(int)
for key in keys:
    d1[key] += 1
# defaultdica sets default, int w/o arg resolves to 0

# in case of lists:
names = ['Roger', 'Pete', 'Susan', 'Gabrielle', 'Lydia']
d2 = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)
# becomes
d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)

# leaving off after 28:00

