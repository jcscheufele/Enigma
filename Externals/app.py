import time
import keyboard
from Internals.plugboard import Plugboard
from Internals.reflector import Reflector
from Internals.rotor import Rotor
from Internals.enigma import Enigma
from Externals.display import Display


import argparse

class App:
    def __init__(self):
        parser = argparse.ArgumentParser(description='This is a simulation of an Enigma Machine. Run quit() to quit, edit() to edit the enigma machine, inter() to switch into an interactive mode, and reset() to reset.')
        parser.add_argument('-c', '--console', action="store_true", help='launch the colsole app')
        parser.add_argument('-i', '--interactive', action="store_true", help='launch the interactive colsole app.')
        parser.add_argument('-l', '--loop', action="store_true", help='Resets after each console input.')
        parser.add_argument('-f', '--file', type=str, nargs=1, help='launch the colsole app')
        
        parser.add_argument('-rS', '--rotorSettings', type=int, nargs=3, help='What three rotor settings to start.')
        parser.add_argument('-rT', '--rotorTypes', type=int, nargs=3, choices=range(8), help='What types of Rotor.')
        parser.add_argument('-rF', '--reflector', type=str, nargs=1, choices=['Beta', 'Gamma', 'A', 'B', 'C', 'B Thin', 'C Thin'], help='The value for the relfector.')

        args = parser.parse_args()

        if args.loop:          self.loop = args.loop
        else:                  self.loop = False
        if args.reflector:     refT = args.reflector[0]
        else:                  refT = "A"
        if args.rotorSettings: rN1,rN2,rN3 = args.rotorSettings
        else:                  rN1,rN2,rN3 = 1, 1, 1
        if args.rotorTypes:    rT1,rT2,rT3 = args.rotorTypes
        else:                  rT1,rT2,rT3 = 0, 1, 2

        self.settings = [rT1, rT2, rT3, rN1, rN2, rN3, refT]
        self.run_console = args.console or args.interactive
        self.run_reader = args.file
        self.interactive = args.interactive

        rotor_1 = Rotor(type=rT1, initial_setting=rN1)
        rotor_2 = Rotor(type=rT2, initial_setting=rN2)
        rotor_3 = Rotor(type=rT3, initial_setting=rN3)

        reflector = Reflector(type=refT)

        self.pairs = [
            ("A", "J"), ("C", "V"),
            ("X", "R"), ("T", "Z"),
            ("Q", "K"), ("G", "S"),
            ("B", "L"), ("M", "W"),
            ("P", "O"), ("D", "I")
        ]
        plugboard = Plugboard(pairs=self.pairs)

        self.enigma = Enigma(
            rotors=[rotor_1, rotor_2, rotor_3],
            plugboard=plugboard,
            reflector=reflector
        )

    def checkInput(self, prompt, list, default):
        good = False
        while not good:
            tmp = input(prompt)
            if tmp in list:
                return tmp
            elif tmp == " ":
                return default
            else:
                print("Please enter a valid value.")

    def edit_enigma(self):
        print("Editing Enigma Machine Settings...")
        print("Enter choices for rotor types: 1-8")
        acceptableTypes = [str(i) for i in range(1,9)]
        rT1 = int(self.checkInput(" Rotor 1 Type> ", acceptableTypes, 1))-1
        rT2 = int(self.checkInput(" Rotor 2 Type> ", acceptableTypes, 2))-1
        rT3 = int(self.checkInput(" Rotor 3 Type> ", acceptableTypes, 3))-1
        
        print("Enter choices for rotor starting positions: (1-26)")
        acceptableSettings = [str(i) for i in range(1,26)]
        rN1 = int(self.checkInput(" Rotor 1 Setting> ", acceptableSettings, 1))-1
        rN2 = int(self.checkInput(" Rotor 2 Setting> ", acceptableSettings, 1))-1
        rN3 = int(self.checkInput(" Rotor 3 Setting> ", acceptableSettings, 1))-1

        print("Enter choice for reflector: {Beta, Gamma, A, B, C, B Thin, C Thin}")
        acceptableRefs = ["Beta", "Gamma", "A", "B", "C", "B Thin", "C Thin"]
        refT = self.checkInput(" Reflector Type> ", acceptableRefs, "A")
        print(refT)
        self.settings = [rT1, rT2, rT3, rN1, rN2, rN3, refT]
        rotor_1 = Rotor(type=rT1, initial_setting=rN1)
        rotor_2 = Rotor(type=rT2, initial_setting=rN2)
        rotor_3 = Rotor(type=rT3, initial_setting=rN3)

        reflector = Reflector(type=refT)

        self.pairs = [
            ("A", "J"), ("C", "V"),
            ("X", "R"), ("T", "Z"),
            ("Q", "K"), ("G", "S"),
            ("B", "L"), ("M", "W"),
            ("P", "O"), ("D", "I")
        ]
        plugboard = Plugboard(pairs=self.pairs)

        self.enigma = Enigma(
            rotors=[rotor_1, rotor_2, rotor_3],
            plugboard=plugboard,
            reflector=reflector
        )

        if self.interactive: tmp = ' Interactive'
        else: tmp = ''
        print(f"Creating{tmp} console app: rT1: {self.settings[0]}, rT2: {self.settings[1]}, rT3: {self.settings[2]}, rN1: {self.settings[3]}, rN2: {self.settings[4]}, rN3: {self.settings[5]}, refT: {self.settings[6]}, reset: {self.loop}")
        

    def exitingApp(self):
        string = 'Exiting Application'
        print(f"{string}                                                                                                                                              ", end='\r')
        time.sleep(.5)
        print(f"{string}.                                                                                                                                              ", end='\r')
        time.sleep(.5)
        print(f"{string}..                                                                                                                                             ", end='\r')
        time.sleep(.5)
        print(f"{string}...                                                                                                                                            ", end='\r')

    def console(self):
        if self.interactive: tmp = ' Interactive'
        else: tmp = ''
        print(f"Creating{tmp} console app: rT1: {self.settings[0]}, rT2: {self.settings[1]}, rT3: {self.settings[2]}, rN1: {self.settings[3]}, rN2: {self.settings[4]}, rN3: {self.settings[5]}, refT: {self.settings[6]}, reset: {self.loop}")
        if not self.interactive: 
            print("General Console Controls: Type input and press enter to see output, type quit() to quit, reset() to reset machine, edit() to edit machine, and inter() to start the interactive mode.")
        while(True):
            if not self.interactive:
                print(f"                                                                                                                                              ", end='\r')
                letters = input(f" |{self.enigma.rotors[0].rotations+1:02}-{self.enigma.rotors[0].type[3]}|{self.enigma.rotors[1].rotations+1:02}-{self.enigma.rotors[1].type[3]}|{self.enigma.rotors[2].rotations+1:02}-{self.enigma.rotors[2].type[3]}|{self.enigma.reflector.typeStr}| enigma $> ")
                bad = False
                '''for val in ["\n"]:
                    if val in letters:
                        bad = True'''
                if bad: pass
                elif letters == 'inter()': self.interactive = True
                elif letters == 'reset()': self.enigma.reset()
                elif letters == "edit()": 
                    self.edit_enigma()
                    letters = ""
                    self.enigma.reset()
                elif letters == 'quit()': 
                    self.exitingApp()
                    exit(1)
                else:
                    output = ""
                    for letter in letters:
                        out = self.enigma.process(letter)
                        output += out
                    print(output)
                    if self.loop: self.enigma.reset()
            else:
                print("Interactive Console Controls: Alt -> Edit Machine, Esc -> Exit, Press any key to see the cipher.")
                inter_console = Display(self.settings, self.enigma, self.pairs, self.loop, self.interactive)
                self.interactive = inter_console.headless()
                if self.interactive != 0 and self.interactive != 1:
                    if self.interactive == 2:
                        self.edit_enigma()
                    elif self.interactive == 3:
                        exit(1)




    def reader(self, file):
        print(f"Creating reader app: file: {file}\n    rT1: {self.settings[0]}, rT2: {self.settings[1]}, rT3: {self.settings[2]}, rN1: {self.settings[3]}, rN2: {self.settings[4]}, rN3: {self.settings[5]}, refT: {self.settings[6]}")
        print(self.enigma.rotors[0].rotations, self.enigma.rotors[1].rotations, self.enigma.rotors[2].rotations)
        with open(file, 'r') as fp:
            lines = fp.readlines()
        string = f"\n\nSettings: rT1: {self.settings[0]}, rT2: {self.settings[1]}, rT3: {self.settings[2]}, rN1: {self.settings[3]}, rN2: {self.settings[4]}, rN3: {self.settings[5]}, refT: {self.settings[6]}"
        with open(f"{file.split('.')[0]}_enigma.txt", 'w') as fp:
            for line in lines:
                output = ""
                if "Settings" not in line:
                    for letter in line:
                        out = self.enigma.process(letter)
                        output += out
                    fp.writelines(output)
                else:
                    break
            fp.writelines(string)
        print(self.enigma.rotors[0].rotations, self.enigma.rotors[1].rotations, self.enigma.rotors[2].rotations)
            
    def display(self):
        gui = Display(self.settings, self.enigma, self.pairs, self.loop, self.run_console)
        gui.run()
            
    def run(self):
        if self.run_reader or self.run_console:
            print(f"Current Pairs: {self.pairs}")
            if self.run_console:
                self.console()
            elif self.run_reader:
                self.reader(file=self.run_reader[0])
        else:
            self.display()