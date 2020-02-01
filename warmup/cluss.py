#!/usr/bin/env python


class Fish:
    __name = "Olaf"
    __parent = None
    __size = 3
    # __ means private
    # --> need setters and getters...

    def __init__(self, name, size):
        self.__name = name
        self.__size = size

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def toString(self):
        return "{} of size {} has {} parent".format(
                self.__name, self.__size, self.__parent)


class Bubblefish(Fish):
    __poison = 0

    def __init__(self, name, size, poison):
        self.__poison = poison
        super(Bubblefish, self).__init__(name, size)

    def poisonate(self, increment=1):
        self.__poison += increment

    def toString(self):
        return super(Bubblefish, self).toString() + \
               " and is {} poisonous".format(self.__poison)


bub = Bubblefish("Jacob", 6, 3)
print(bub.toString())
bub.poisonate()
print(bub.toString())
bub.poisonate(6)
print(bub.toString())
