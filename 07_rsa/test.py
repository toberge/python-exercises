import unittest

from brute_force import brute_force
from encrypt_rsa import decrypt

CIPHER = [84620, 66174, 66174, 5926, 9175, 87925, 54744, 54744, 65916, 79243, 39613, 9932, 70186, 85020, 70186, 5926, 65916, 72060, 70186, 21706, 39613, 11245, 34694, 13934, 54744, 9932, 70186, 85020, 70186, 54744, 81444, 32170, 53121, 81327, 82327, 92023, 34694, 54896, 5926, 66174, 11245, 9175, 54896, 9175, 66174, 65916, 43579, 64029, 34496, 53121, 66174, 66174, 21706, 92023, 85020, 9175, 81327, 21706, 13934, 21706, 70186, 79243, 9175, 66174, 81327, 5926, 74450, 21706, 70186, 79243, 81327, 81444, 32170, 53121]
n = 100127
PLAINTEXT = 'https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Attacks_against_plain_RSA'

class TestDecryption(unittest.TestCase):

    def test_actual(self):
        # brute force the thing
        pk = brute_force((29815, n), CIPHER, 'h')
        message = decrypt((pk, n), CIPHER)
        self.assertTrue(message.startswith('h'))
    
    def test_solution(self):
        message = decrypt((14599, n), CIPHER)
        self.assertTrue(message.startswith('h'))
        self.assertEqual(message, PLAINTEXT)

if __name__ == '__main__':
    unittest.main()