import unittest
from plugboard import Plugboard

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class TestRotor(unittest.TestCase):

    def setUp(self):
        pairs = [("A", "J"), ("C", "V"), ("X", "R"), ("T", "Z"), ("Q", "K"),
                 ("G", "S"), ("B", "L"), ("M", "W"), ("P", "O"), ("D", "I")]
        self.plugboard = Plugboard(pairs=pairs)

    def test_plugboard_output(self):
        self.assertEqual(self.plugboard.board["A"], 'J')
        self.assertEqual(self.plugboard.board["J"], "A")


if __name__ == '__name__':
    unittest.main()