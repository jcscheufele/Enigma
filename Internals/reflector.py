ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#                            ABCDEFGHIJKLMNOPQRSTUVWXYZ
BETA =   dict(zip(ALPHABET, "LEYJVCNIXWPBQMDRTAKZGFUHOS"))

#                            ABCDEFGHIJKLMNOPQRSTUVWXYZ
GAMMA =  dict(zip(ALPHABET, "FSOKANUERHMBTIYCWLQPZXVGJD"))

#                            ABCDEFGHIJKLMNOPQRSTUVWXYZ
A =      dict(zip(ALPHABET, "EJMZALYXVBWFCRQUONTSPIKHGD"))

#                            ABCDEFGHIJKLMNOPQRSTUVWXYZ
B =      dict(zip(ALPHABET, "YRUHQSLDPXNGOKMIEBFZCWVJAT"))

#                            ABCDEFGHIJKLMNOPQRSTUVWXYZ
C =      dict(zip(ALPHABET, "FVPJIAOYEDRZXWGCTKUQSBNMHL"))

#                            ABCDEFGHIJKLMNOPQRSTUVWXYZ
B_THIN = dict(zip(ALPHABET, "ENKQAUYWJICOPBLMDXZVFTHRGS"))

#                            ABCDEFGHIJKLMNOPQRSTUVWXYZ
C_THIN = dict(zip(ALPHABET, "RDOBJNTKVEHMLFCWZAXGYIPSUQ"))
#ETW = dict(zip(ALPHABET, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

class Reflector:
    def __init__(self, type):
        self.set_type(type)

    def set_type(self, val):
        possibleTypes = ["Beta", "Gamma", "A", "B", "C", "B Thin", "C Thin"]#, 'ETW']
        if val in possibleTypes:
            if   val == "Beta":   self.type = BETA
            elif val == "Gamma":  self.type = GAMMA
            elif val == "A":      self.type = A
            elif val == "B":      self.type = B
            elif val == "C":      self.type = C
            elif val == "B Thin": self.type = B_THIN
            elif val == "C Thin": self.type = C_THIN
            #elif type == "ETW":    self.type = ETW
            self.typeStr = val
        else:
            raise Exception("Must provide correct reflector type")

    def reflect(self, letter):
        return self.type[letter]
