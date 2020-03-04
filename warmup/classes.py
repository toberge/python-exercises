'''
hey hey people
notes from another talk by Raymond Hettinger
https://www.youtube.com/watch?v=HTLu2DFOdTg
'''
from datetime import datetime

# YAGNI - ya ain't gonna need it

# Constructor war - different needs and thus several conversions passed to your constructor
# Solution - give it to them!
# Using @classmethod
# AND set first argument to be the class!!!
# - to allow correct subclassing

datetime(2013, 3, 16)
datetime.fromordinal(734000)

class Thing:
    'docstrings yeah'
    version = '0.2'

    a_lot = 55

    def __init__(self, arg):
        self.arg = arg

    @classmethod
    def from_whatever(cls, whatever):
        return cls(whatever * Thing.a_lot)

    def something(self):
        return self.arg / 3

# there is @staticmethod
# put all the related tools in the toolbox
# even if they aren't exactly completely related?
# (angle conversion related to circles)

# Prevent breaking methods of subclasses
# create class local reference, a spare copy
# _perimeter = perimeter
# but that'll lead to playing the copying game
# so do _circle_perimeter = perimeter
# oh bloody hell
# but this is automated --> use __perimeter()
# the dunder method...
# making sure self *actually* refers to you
# a proper class local reference
# this is NOT about privacy

# and instead of GETTERS AND BLOODY SETTERS
# we got @property and @something.setter

class Whoopsie:

    def __init__(self, radius):
        # this still works!
        self.radius = radius

    @property
    def radius(self):
        return self.diameter / 2

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2

# oh yes baby

# many many instances --> flyweight design pattern
# do __slots__ then
# but ONLY do them LAST cuz u lose way to inspect dictionary
# also: __slots__ is NOT inherited

class Many:
    __slots__ = ['attribute']

    def __init(self, attribute):
        self.attribute = attribute

# yay yay


