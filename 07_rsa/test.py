import unittest

from brute_force import brute_force
from encrypt_rsa import decrypt

CIPHER = [84620, 66174, 66174, 5926, 9175, 87925, 54744, 54744, 65916, 79243, 39613, 9932, 70186, 85020, 70186, 5926, 65916, 72060, 70186, 21706, 39613, 11245, 34694, 13934, 54744, 9932, 70186, 85020, 70186, 54744, 81444, 32170, 53121, 81327, 82327, 92023, 34694, 54896, 5926, 66174, 11245, 9175, 54896, 9175, 66174, 65916, 43579, 64029, 34496, 53121, 66174, 66174, 21706, 92023, 85020, 9175, 81327, 21706, 13934, 21706, 70186, 79243, 9175, 66174, 81327, 5926, 74450, 21706, 70186, 79243, 81327, 81444, 32170, 53121]
n = 100127
PLAINTEXT = 'https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Attacks_against_plain_RSA'

class TestDecryption(unittest.TestCase):

    def test_actual(self):
        # brute force the thing
        [pk] = list(brute_force((29815, n), CIPHER, 'h'))
        message = decrypt((pk, n), CIPHER)
        self.assertTrue(message.startswith('h'))
    
    def test_solution(self):
        message = decrypt((14599, n), CIPHER)
        self.assertTrue(message.startswith('h'))
        self.assertEqual(message, PLAINTEXT)
    
    def test_other_solutions(self):
        message = decrypt((31175, n), CIPHER)
        self.assertTrue(message.startswith('h'))
        self.assertEqual(message, 'h堦堦psⰓ녔녔鸿𖘺𗉁wi𒿘ip鸿֧i𑫂𗉁oֵg녔wi𒿘i녔R惊褏_员ֵ儧p堦os儧s堦鸿𘉉)䧍褏堦堦𑫂𒿘s_𑫂g𑫂i𖘺s堦_pl𑫂i𖘺_R惊褏')
        message = decrypt((47751, n), CIPHER)
        self.assertTrue(message.startswith('h'))
        self.assertEqual(message, 'h摭摭ps莺莺㢅𔮫wi𒎑ip㢅틜i𔨝𔮫o멜g莺wi𒎑i莺R镨貑_𖴳멜抱p摭os抱s摭㢅춢)𐀵貑摭摭𔨝𖴳𒎑s_𔨝g𔨝is摭_pl𔨝i_R镨貑')


if __name__ == '__main__':
    unittest.main()