import sys, os
import unittest
from reflector import Reflector

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class TestReflector(unittest.TestCase):

    def setUp(self):
        self.reflector = Reflector(type='Beta')

    def test_reflector(self):
        swapped = []
        types = ['Beta', 'Gamma', 'A', 'B', 'C', 'B Thin', 'C Thin']#, 'ETW']
        bool = True
        for type in types:
            self.reflector.set_type(type)
            for letter in ALPHABET:
                swap = self.reflector.reflect(letter)
                if swap in swapped:
                    bool = False
                    break
                swapped.append(swap)
            if not bool:
                break
            else:
                swapped = []

        self.assertTrue(bool)

    



if __name__ == '__name__':
    unittest.main()