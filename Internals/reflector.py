ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

BETA =   dict(zip(ALPHABET, "LEYJVCNIXWPBQMDRTAKZGFUHOS"))
GAMMA =  dict(zip(ALPHABET, "FSOKANUERHMBTIYCWLQPZXVGJD"))
A =      dict(zip(ALPHABET, "EJMZALYXVBWFCRQUONTSPIKHGD"))
B =      dict(zip(ALPHABET, "YRUHQSLDPXNGOKMIEBFZCWVJAT"))
C =      dict(zip(ALPHABET, "FVPJIAOYEDRZXWGCTKUQSBNMHL"))
B_THIN = dict(zip(ALPHABET, "ENKQAUYWJICOPBLMDXZVFTHRGS"))
C_THIN = dict(zip(ALPHABET, "RDOBJNTKVEHMLFCWZAXGYIPSUQ"))
#ETW = dict(zip(ALPHABET, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

class Reflector:
    def __init__(self, type):
        self.set_type(type)

    def set_type(self, type):
        possibleTypes = ['Beta', 'Gamma', 'A', 'B', 'C', 'B Thin', 'C Thin']#, 'ETW']
        if type in possibleTypes:
            if   type == "Beta":   self.type = BETA
            elif type == "Gamma":  self.type = GAMMA
            elif type == "A":      self.type = A
            elif type == "B":      self.type = B
            elif type == "C":      self.type = C
            elif type == "B Thin": self.type = B_THIN
            elif type == "C Thin": self.type = C_THIN
            #elif type == "ETW":    self.type = ETW
        else:
            raise Exception("Must provide correct reflector type")

    def reflect(self, letter):
        return self.type[letter]
