import unittest

# Uncomment below for testing only, comment out before upload
from rle import RLEString

ALPHABETIC = ["aaa", "a", "TTTTTeeeesssst", "AAAABBBBCCCCDEFGHIIIIIIJJ", "abcdefghjiklmno"]
COMPRESSED = ['3a', '1a', '5T4e4s1t', '4A4B4C1D1E1F1G1H6I2J', '1a1b1c1d1e1f1g1h1j1i1k1l1m1n1o']

NONALPHABETIC = ['2', '    ', '!!"#¤"/%=)', 'æøå', 'abcdef defgh', 'There are more than 3 non-alphabeticals in this one when we count spaces!']

class Assignment8Tests(unittest.TestCase):
    # Place your unit tests in this class
    # ...
    # ...
    # ...
    def test_throws_exception_if_empty(self):
        with self.assertRaises(Exception):
            RLEString('')

    def test_raises_if_nonalphabetic(self):
        for s in NONALPHABETIC:
            with self.assertRaises(Exception):
                RLEString(s)
    
    def test_iscompressed_after_compress(self):
        s = RLEString('abcddd')
        s.compress()
        self.assertTrue(s.iscompressed())
    
    def test_cannot_compress_twice(self):
        s = RLEString('hellllotherre')
        s.compress()
        with self.assertRaises(Exception):
            s.compress()
    
    def test_cannot_decompress_when_uncompressed(self):
        s = RLEString('iamverycompressed')
        with self.assertRaises(Exception):
            s.decompress()
    
    def test_can_compress_after_decompress(self):
        s = RLEString('iwillbecompressed')
        s.compress()
        s.decompress()
        try:
            s.compress()
        except Exception:
            self.fail('Unable to compress after decompress')
    
    def test_compresses_correctly(self):
        for string, comp in zip(ALPHABETIC, COMPRESSED):
            s = RLEString(string)
            s.compress()
            self.assertEqual(str(s), comp)

    def test_decompresses_correctly(self):
        for string in ALPHABETIC:
            s = RLEString(string)
            s.compress()
            s.decompress()
            self.assertEqual(str(s), string)

if __name__ == '__main__':
    # Start the unit test
    unittest.main(verbosity=2)