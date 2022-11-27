from Internals.plugboard import Plugboard
from Internals.reflector import Reflector
from Internals.rotor import Rotor
from enigma import Enigma

if __name__ == "__main__":
    rotor_1 = Rotor(type=0, initial_setting=1)
    rotor_2 = Rotor(type=1, initial_setting=5)
    rotor_3 = Rotor(type=2, initial_setting=20)
    reflector = Reflector(type="A")
    pairs = [("A", "J"), ("C", "V"),
             ("X", "R"), ("T", "Z"),
             ("Q", "K"), ("G", "S"),
             ("B", "L"), ("M", "W"),
             ("P", "O"), ("D", "I")]
    plugboard = Plugboard(pairs=pairs)
    enigma = Enigma(
        rotors=[rotor_1, rotor_2, rotor_3],
        plugboard=plugboard,
        reflector=reflector
    )

    while(True):
        letters = input("enigma $> ")
        output = ""
        for letter in letters:
            out = enigma.process(letter.upper())
            output += out
        print(output)
        enigma.reset()