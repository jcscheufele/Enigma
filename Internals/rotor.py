ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

RANGE = [i for i in range(26)]

CONVERSION_TOL = dict(zip(RANGE, ALPHABET))
CONVERSION_TOI = dict(zip(ALPHABET, RANGE))

#                           ABCDEFGHIJKLMNOPQRSTUVWXYZ                    ABCDEFGHIJKLMNOPQRSTUVWXYZ
I =    (dict(zip(ALPHABET, "EKMFLGDQVZNTOWYHXUSPAIBRCJ")), "Q", dict(zip("EKMFLGDQVZNTOWYHXUSPAIBRCJ", ALPHABET)))

#                           ABCDEFGHIJKLMNOPQRSTUVWXYZ                    ABCDEFGHIJKLMNOPQRSTUVWXYZ
II =   (dict(zip(ALPHABET, "AJDKSIRUXBLHWTMCQGZNPYFVOE")), "E", dict(zip("AJDKSIRUXBLHWTMCQGZNPYFVOE", ALPHABET)))

#                           ABCDEFGHIJKLMNOPQRSTUVWXYZ                    ABCDEFGHIJKLMNOPQRSTUVWXYZ
III =  (dict(zip(ALPHABET, "BDFHJLCPRTXVZNYEIWGAKMUSQO")), "V", dict(zip("BDFHJLCPRTXVZNYEIWGAKMUSQO", ALPHABET)))

#                           ABCDEFGHIJKLMNOPQRSTUVWXYZ                    ABCDEFGHIJKLMNOPQRSTUVWXYZ
IV =   (dict(zip(ALPHABET, "ESOVPZJAYQUIRHXLNFTGKDCMWB")), "J", dict(zip("ESOVPZJAYQUIRHXLNFTGKDCMWB", ALPHABET)))

#                           ABCDEFGHIJKLMNOPQRSTUVWXYZ                    ABCDEFGHIJKLMNOPQRSTUVWXYZ
V =    (dict(zip(ALPHABET, "VZBRGITYUPSDNHLXAWMJQOFECK")), "Z", dict(zip("VZBRGITYUPSDNHLXAWMJQOFECK", ALPHABET)))

#                           ABCDEFGHIJKLMNOPQRSTUVWXYZ                    ABCDEFGHIJKLMNOPQRSTUVWXYZ
VI =   (dict(zip(ALPHABET, "ENKQAUYWJICOPBLMDXZVFTHRGS")), "Z", dict(zip("ENKQAUYWJICOPBLMDXZVFTHRGS", ALPHABET)))

#                           ABCDEFGHIJKLMNOPQRSTUVWXYZ                    ABCDEFGHIJKLMNOPQRSTUVWXYZ
VII =  (dict(zip(ALPHABET, "NZJHGRCXMYSWBOUFAIVLPEKQDT")), "Z", dict(zip("NZJHGRCXMYSWBOUFAIVLPEKQDT", ALPHABET)))

#                           ABCDEFGHIJKLMNOPQRSTUVWXYZ                    ABCDEFGHIJKLMNOPQRSTUVWXYZ
VIII = (dict(zip(ALPHABET, "FKQHTLXOCBJSPDZRAMEWNIUYGV")), "Z", dict(zip("FKQHTLXOCBJSPDZRAMEWNIUYGV", ALPHABET)))

def int_to_letter(value):
    return CONVERSION_TOL[value]

def letter_to_int(value):
    return CONVERSION_TOI[value]

class Rotor:
    def __init__(self, type, initial_setting):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.set_type(type)
        self.setting = initial_setting
        self.wires = self.type[0]
        self.rev_wires = self.type[2]
        self.notch = letter_to_int(self.type[1])
        self.rotations = 0

    def set_type(self, type):
        possibleTypes = [i for i in range(8)]
        if type in possibleTypes:
            if   type == 0: self.type = I
            elif type == 1: self.type = II
            elif type == 2: self.type = III
            elif type == 3: self.type = IV
            elif type == 4: self.type = V
            elif type == 5: self.type = VI
            elif type == 6: self.type = VII
            elif type == 7: self.type = VIII
        else:
            raise Exception("Must provide correct reflector type")

    def reset(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.rotate(self.setting)
        self.rotations = 1

    def rotate(self, offset=1):
        if self.rotations == self.notch:
            self.alphabet = self.alphabet[offset:] + self.alphabet[:offset]
            self.rotations += offset

    def forward(self, letter):
        return self.wires[letter]

    def backward(self, letter):
        return self.rev_wires[letter]
