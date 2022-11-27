from Externals.console import console
import sys

import argparse

parser = argparse.ArgumentParser(description='This is a simulation of an Enigma Machine. Run quit() to quit and reset() to reset.')
parser.add_argument('-c', '--console', action="store_true",
                    help='launch the colsole app')
parser.add_argument('-rS', '--rotorSettings', type=int, nargs=3,
                    help='What three rotor settings to start.')
parser.add_argument('-rT', '--rotorTypes', type=int, nargs=3, choices=range(8),
                    help='What types of Rotor.')
parser.add_argument('-rF', '--reflector', type=str, nargs=1, choices=['Beta', 'Gamma', 'A', 'B', 'C', 'B Thin', 'C Thin'],
                    help='The value for the relfector.')
parser.add_argument('-l', '--loop', action="store_true",
                    help='Resets after each console input.')

if __name__ == "__main__":
    args = parser.parse_args()
    if args.console:
        if args.loop:
            loop = args.loop
        else:
            loop = False
        if args.rotorSettings:
            rN1,rN2,rN3 = args.rotorSettings
        else:
            rN1,rN2,rN3 = 0, 0, 0
        if args.rotorTypes:
            rT1,rT2,rT3 = args.rotorTypes
        else:
            rT1,rT2,rT3 = 0, 1, 2
        if args.reflector:
            refT = args.reflector[0]
        else:
            refT = "A"
        print(f"Creating console app: rT1: {rT1}, rT2: {rT2}, rT3: {rT3}, rN1: {rN1}, rN2: {rN2}, rN3: {rN3}, refT: {refT[0]}, reset: {loop}")
        console(rT1=rT1, rT2=rT2, rT3=rT3,
                rN1=rN1, rN2=rN2, rN3=rN3, 
                refT=refT, reset=loop)