from Internals.plugboard import Plugboard
from Internals.reflector import Reflector
from Internals.rotor import Rotor
from Internals.enigma import Enigma

pairs_def = [("A", "J"), ("C", "V"),
             ("X", "R"), ("T", "Z"),
             ("Q", "K"), ("G", "S"),
             ("B", "L"), ("M", "W"),
             ("P", "O"), ("D", "I")]

def console(rT1=0, rT2=1, rT3=2, rN1=0, rN2=0, rN3=0, refT="A", pairs=pairs_def, reset=False):
    rotor_1 = Rotor(type=rT1, initial_setting=rN1)
    rotor_2 = Rotor(type=rT2, initial_setting=rN2)
    rotor_3 = Rotor(type=rT3, initial_setting=rN3)
    reflector = Reflector(type=refT)
    plugboard = Plugboard(pairs=pairs)
    enigma = Enigma(
        rotors=[rotor_1, rotor_2, rotor_3],
        plugboard=plugboard,
        reflector=reflector
    )

    while(True):
        letters = input("enigma $> ")
        bad = False
        '''for val in ["\n"]:
            if val in letters:
                bad = True'''
        if bad: pass
        elif letters == 'reset()':
            enigma.reset()
        elif letters == 'quit()':
            exit(1)
        else:
            output = ""
            for letter in letters:
                out = enigma.process(letter.upper())
                output += out
            
            print(output)
            if reset: enigma.reset()