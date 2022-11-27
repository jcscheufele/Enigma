import unittest
from rotor import Rotor

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class TestRotor(unittest.TestCase):

    def setUp(self):
        self.rotor = Rotor(type=0, initial_setting=10)

    def test_rotor_output(self):
        output = self.rotor.output(True, "A")
        self.assertEqual(output[1], "T")
        self.assertFalse(output[0])

    '''def test_rotor(self):
        letters = []
        types = [i for i in range(8)]
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

        self.assertTrue(bool)'''


if __name__ == '__name__':
    unittest.main()