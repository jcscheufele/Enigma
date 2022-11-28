import threading
import time
from pynput import keyboard
from tkinter import *
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


class Display:
    def __init__(self, settings, enigma, pairs, reset, console):
        self.rT1, self.rN1 = settings[0], settings[3]
        self.rT2, self.rN2 = settings[1], settings[4]
        self.rT3, self.rN3 = settings[2], settings[5]
        self.refT = settings[6]
        self.enigma = enigma
        self.pairs = pairs
        self.reset = reset
        self.console = console
        self.line = ""
        self.exit_code = 0
        
    def editEnigma(self):
        pass

    def interactiveConsole(self, key):
        try:
            if key.char in ALPHABET:
                self.line += self.enigma.process(key.char)
                print(f" |{self.enigma.rotors[0].rotations+1:02}|{self.enigma.rotors[1].rotations+1:02}|{self.enigma.rotors[2].rotations+1:02}| enigma £> {key.char} | {self.line}      ", end='\r')
        except:
            #print(f"Not a valid key.")
            if (key == keyboard.Key.alt_l) or (key == keyboard.Key.alt_r):
                # editing mode
                self.exit_code = 2
                exit(1)
            elif key == keyboard.Key.space:
                self.line += "_"
                print(f" |{self.enigma.rotors[0].rotations+1:02}|{self.enigma.rotors[1].rotations+1:02}|{self.enigma.rotors[2].rotations+1:02}| enigma £> _ | {self.line}      ", end='\r')
                
            elif key == keyboard.Key.shift:
                '''self.exit_code = 3
                exit(1)'''
                pass
            elif key == keyboard.Key.enter:
                self.enigma.reset()
                cipher = self.enigma.process(self.line)
                print(f"\n{cipher}      ")
                
                if self.reset: self.enigma.reset()
                self.line = ""
                print(f" |{self.enigma.rotors[0].rotations+1:02}|{self.enigma.rotors[1].rotations+1:02}|{self.enigma.rotors[2].rotations+1:02}| enigma £>                       ", end='\r')
            elif key == keyboard.Key.backspace:
                if (self.line != ""):
                    if (self.line[-1] != "_"):
                        turn_first = self.enigma.rotors[0].rotate(force=True, offset=-1)
                        if turn_first: turn_next = True
                        else: turn_next = False
                        for rotor in self.enigma.rotors[1:]:
                            turn_next = rotor.rotate(force=(turn_next and turn_first), offset=-1)
                    self.line = self.line[:-1]
                
                print(f" |{self.enigma.rotors[0].rotations+1:02}|{self.enigma.rotors[1].rotations+1:02}|{self.enigma.rotors[2].rotations+1:02}| enigma £> - | {self.line}      ", end='\r')
            elif key == keyboard.Key.esc:
                self.exit_code = 0
                exit(1)
            else:
                pass

    def userInterface(self, key):
        if key == keyboard.Key.esc:
            exit(1)

    def start_thread(self):
        self.root = Tk()
        self.root.geometry("800x1000")

        editing = Tk.frame(self.root)

        #Create a canvas object
        c= Canvas(self.root,width=400, height=400)
        c.pack()
        c.create_oval(60,60,210,210)
        self.root.mainloop()
        
    def on_press(self, key):
        if self.console:
            self.interactiveConsole(key)
        else:
            self.userInterface(key)
    

    def headless(self):
        # aka interactive console
        print("Starting interactive console.    ", end='\r')
        time.sleep(1)
        print("Starting interactive console..   ", end='\r')
        time.sleep(1)
        print("Starting interactive console...  ", end='\r')
        time.sleep(1)
        print("                                                                                                      ", end='\r')
        print(f" |{self.enigma.rotors[0].rotations+1:02}|{self.enigma.rotors[1].rotations+1:02}|{self.enigma.rotors[2].rotations+1:02}| enigma £>                 ", end='\r')
        listener = keyboard.Listener(on_press=self.on_press, suppress=True)
        listener.start()
        listener.join()
        print("Returning to non-interactive console.    ", end='\r')
        time.sleep(1)
        print("Returning to non-interactive console..   ", end='\r')
        time.sleep(1)
        print("Returning to non-interactive console...  ", end='\r')
        time.sleep(1)
        print("                                                                                                      ", end='\r')
        print("General Console Controls: Type input and press enter to see output, type quit() to quit, reset() to reset machine, edit() to edit machine, and inter() to start the interactive mode.")

        return self.exit_code
    
    def run(self):
        thread = threading.Thread(target=self.start_thread)
        thread.start()
        listener = keyboard.Listener(on_press=self.on_press, suppress=True)
        listener.start()
        listener.join()
        thread.join()