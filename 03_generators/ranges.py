#!/usr/bin/env python

"""
Written - List the advantages and disadvantages of each function. Consider the following scenarios:

    You wish to generate a list of tuples with start=1 and end=1000.
    You will reference randomly chosen elements of the list several times in your code.

    You wish to generate a list of tuples with start=1 and end=10**15.
    You will reference the elements in the list only once, and in order.
"""

def myrange_list(start,end):
    """Returns a list of tuples blah blah

    A: n=1000, random access
    Accessing elements in a list by index is an O(1) operation,
    and storing 1000 elements in memory does not fill that much space.
    Space complexity: O(n)
    Time complexity: O(a) where a is number of accesses, if a >> 1000

    B: n=10**15, sequential access
    A list this large would take up a lot of memory, and when the elements are acccessed sequentially,
    the performance of list access dwindles in importance.
    Space complexity: O(n)
    Time complexity: O(n) plus the cost of accessing data outside cache (and possibly memory)
    """
    list = []
    # With i as an increasing number in the range of the interval
    for i in range(0, end - start):
        # Append a tuple where i is added to start
        # and subtracted from end-1
        list.append((start + i, end - 1 - i))
    return list

def myrange_gen(start,end):
    """Returns a generator that yields tuples that blah blah

    A: n=1000, random access
    Somewhat disadvantageous.
    Generators are practically made for sequential access
    and do not *need* to store any more than the current element's value in memory. 
    Randomly accessing the elements of a generator would require
    creating a list of the generated elements,
    otherwise the generator would have to be run an absurd amount of times
    (one for each access of an element that lies *before* the current element).
    In this case, the generator might as well have created a list in the first place.
    Space complexity: O(n) if turned into a list, O(1) otherwise
    Time complexity: O(n) if turned into a list, *way worse* otherwise

    B: n=10**15, sequential access
    Definitely advantageous.
    Iterating through each element only once and in the order they are produced
    will require running the entire process *only once*,
    while having the significant advantage of not storing all the elements in memory.
    Space complexity: O(1) or so
    Time complexity: O(n)
    """
    # With i as an increasing number in the range of the interval
    for i in range(0, end - start):
        # Generate a tuple where i is added to start
        # and subtracted from end-1
        yield start + i, end - 1 - i

if __name__ == '__main__':
    print(myrange_list(1, 10))
    print(list(myrange_gen(1, 10)))
    print([(1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2), (9, 1)])
