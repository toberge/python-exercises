import unittest
from ranges import myrange_list
from ranges import myrange_gen

LIST = [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2), (9, 1)]

class TestRanges(unittest.TestCase):

    def test_list(self):
        self.assertSequenceEqual(myrange_list(1, 10), LIST)
    
    def test_gen(self):
        self.assertSequenceEqual(list(myrange_gen(1, 10)), LIST)

if __name__ == '__main__':
    unittest.main()
