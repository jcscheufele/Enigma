from Internals.plugboard import Plugboard
from Internals.reflector import Reflector
from Internals.rotor import Rotor
from Internals.enigma import Enigma


import argparse

class App:
    def __init__(self):
        parser = argparse.ArgumentParser(description='This is a simulation of an Enigma Machine. Run quit() to quit and reset() to reset.')
        parser.add_argument('-c', '--console', action="store_true", help='launch the colsole app')
        parser.add_argument('-f', '--file', type=str, nargs=1, help='launch the colsole app')
        parser.add_argument('-rS', '--rotorSettings', type=int, nargs=3, help='What three rotor settings to start.')
        parser.add_argument('-rT', '--rotorTypes', type=int, nargs=3, choices=range(8), help='What types of Rotor.')
        parser.add_argument('-rF', '--reflector', type=str, nargs=1, choices=['Beta', 'Gamma', 'A', 'B', 'C', 'B Thin', 'C Thin'], help='The value for the relfector.')
        parser.add_argument('-l', '--loop', action="store_true", help='Resets after each console input.')

        args = parser.parse_args()

        if args.loop:          self.loop = args.loop
        else:                  self.loop = False
        if args.reflector:     refT = args.reflector[0]
        else:                  refT = "A"
        if args.rotorSettings: rN1,rN2,rN3 = args.rotorSettings
        else:                  rN1,rN2,rN3 = 0, 0, 0
        if args.rotorTypes:    rT1,rT2,rT3 = args.rotorTypes
        else:                  rT1,rT2,rT3 = 0, 1, 2

        self.settings = [rT1, rT2, rT3, rN1, rN2, rN3, refT]
        self.run_console = args.console
        self.run_reader = args.file

        rotor_1 = Rotor(type=rT1, initial_setting=rN1)
        rotor_2 = Rotor(type=rT2, initial_setting=rN2)
        rotor_3 = Rotor(type=rT3, initial_setting=rN3)

        reflector = Reflector(type=refT)

        pairs = [
            ("A", "J"), ("C", "V"),
            ("X", "R"), ("T", "Z"),
            ("Q", "K"), ("G", "S"),
            ("B", "L"), ("M", "W"),
            ("P", "O"), ("D", "I")
        ]
        plugboard = Plugboard(pairs=pairs)

        self.enigma = Enigma(
            rotors=[rotor_1, rotor_2, rotor_3],
            plugboard=plugboard,
            reflector=reflector
        )

    def console(self, reset):
        print(f"Creating console app: rT1: {self.settings[0]}, rT2: {self.settings[1]}, rT3: {self.settings[2]}, rN1: {self.settings[3]}, rN2: {self.settings[4]}, rN3: {self.settings[5]}, refT: {self.settings[6]}, reset: {reset}")
        while(True):
            letters = input("enigma $> ")
            bad = False
            '''for val in ["\n"]:
                if val in letters:
                    bad = True'''
            if bad: pass
            elif letters == 'reset()':
                self.enigma.reset()
            elif letters == 'quit()':
                exit(1)
            else:
                output = ""
                for letter in letters:
                    out = self.enigma.process(letter.upper())
                    output += out
                
                print(output)
                if reset: self.enigma.reset()

    def reader(self, file):
        print(f"Creating reader app: file: {file}\n    rT1: {self.settings[0]}, rT2: {self.settings[1]}, rT3: {self.settings[2]}, rN1: {self.settings[3]}, rN2: {self.settings[4]}, rN3: {self.settings[5]}, refT: {self.settings[6]}")
        with open(file, 'r') as fp:
            lines = fp.readlines()
        string = f"\n\nSettings: rT1: {self.settings[0]}, rT2: {self.settings[1]}, rT3: {self.settings[2]}, rN1: {self.settings[3]}, rN2: {self.settings[4]}, rN3: {self.settings[5]}, refT: {self.settings[6]}"
        with open(f"{file.split('.')[0]}_enigma.txt", 'w') as fp:
            for line in lines:
                output = ""
                if "Settings" not in line:
                    for letter in line:
                        out = self.enigma.process(letter.upper())
                        output += out
                    fp.writelines(output)
                else:
                    break
            fp.writelines(string)
            
            
    def run(self):
        if self.run_console:
            self.console(reset=self.loop)
        elif self.run_reader:
            self.reader(file=self.run_reader[0])
        else:
            pass