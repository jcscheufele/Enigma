from Externals.console import console
import sys

import argparse

parser = argparse.ArgumentParser(description='This is a simulation of an Enigma Machine.')
parser.add_argument('-c', '--console', action="store_true",
                    help='launch the colsole app')
parser.add_argument('-r', '--rotor_settings', 
                    help='Rotor 1, Rotor 2, Rotor 3')
parser.add_argument('-l', '--loop', action="store_true",
                    help='Resets after each console input.')

if __name__ == "__main__":
    args = parser.parse_args()
    
    if args.console:
        console(reset=args.loop)