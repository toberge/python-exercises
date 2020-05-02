import unittest

from capitalization import capitalize

class CapitalizationTest(unittest.TestCase):
    def test_capitalizes(self):
        self.assertEqual(
                capitalize('Surdeigsbrød', [0,0,1,1,1,0,1,0,1,1,0,1]),
                'suRDEiGsBRøD'
        )

    def test_skips_blanks(self):
        # as per my understanding...
        self.assertEqual(capitalize('Py t h o n', [0,1,0]), 'pY t h O n')
        self.assertEqual(capitalize('hi!!Iam$mART', [0,1]), 'hI!!iAm$mArT')

    def test_replicates_short_rule(self):
        self.assertEqual(capitalize('Python', [0,1,0]), 'pYthOn')

    def test_trunctates_long_rule(self):
        self.assertEqual(capitalize('hi', [1,0,1,0,1,0]), 'Hi')

if __name__ == '__main__':
    unittest.main(verbosity=2)
