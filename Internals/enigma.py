ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

RANGE = [i for i in range(26)]

CONVERSION_TOL = dict(zip(RANGE, ALPHABET))
CONVERSION_TOI = dict(zip(ALPHABET, RANGE))

def int_to_letter(value):
    print(f"{value}, {CONVERSION_TOL[value]}")
    return CONVERSION_TOL[value]

def letter_to_int(value):
    print(f"{value}, {CONVERSION_TOI[value]}")
    return CONVERSION_TOI[value]

class Enigma:
    def __init__(self, rotors, plugboard, reflector):
        self.rotors = rotors
        self.plugboard = plugboard
        self.reflector = reflector
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def reset(self):
        for rotor in self.rotors:
            rotor.reset()

    def process(self, input):
        output = ""
        for letter in input:
            output += self.encrypt(letter)
        return output

    def encrypt(self, input):

        if input.upper() not in ALPHABET:
            return input
        else:
            input = input.upper()
        
        tmp = self.plugboard.output(input)
    
        contact_index = self.alphabet.index(tmp)
        for rotor in self.rotors:
            contact_letter = rotor.alphabet[contact_index]
            cipher_letter = rotor.forward(contact_letter)
            contact_index = rotor.alphabet.index(cipher_letter)

        contact_letter = self.alphabet[contact_index]
        tmp = self.reflector.reflect(contact_letter)
        contact_index = self.alphabet.index(tmp)

        for rotor in reversed(self.rotors):
            contact_letter = rotor.alphabet[contact_index]
            tmp = rotor.backward(contact_letter)
            contact_index = rotor.alphabet.index(tmp)

        tmp = self.alphabet[contact_index]
        
        turn_first = self.rotors[0].rotate(force=True)
        if turn_first: turn_next = True
        else: turn_next = False
        for rotor in self.rotors[1:]:
            turn_next = rotor.rotate(force=(turn_next and turn_first))

        tmp = self.plugboard.output(tmp)
        return tmp