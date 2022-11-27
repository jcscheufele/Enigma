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
        self.full = []
        self.backspaces = 0
        
    def editEnigma(self):
        pass

    def interactiveConsole(self, key):
        try:
            if key.char in ALPHABET:
                self.line += self.enigma.process(key.char)
                self.full.append(1)
                #print(" enigma $>", f"{self.line}      ", end='\r')
                output = ""
                for i in range(len(self.full)):
                    if self.full[i]:
                        output += self.line[i]
                print(f" i-enigma $> {output}      ", end='\r')
        except:
            #print(f"Not a valid key.")
            if key == keyboard.Key.alt:
                # editing mode
                pass
            elif key == keyboard.Key.space:
                self.line += "_"
                #print(" enigma $>", f"{self.line}      ", end='\r')
                self.full.append(1)
                output = ""
                for i in range(len(self.full)):
                    if self.full[i]:
                        output += self.line[i]
                print(f" i-enigma $> {output}      ", end='\r')
            elif key == keyboard.Key.shift:
                pass
            elif key == keyboard.Key.enter:
                self.enigma.reset()
                if 1 in self.full:
                    output = ""
                    cipher = self.enigma.process(self.line)
                    for i in range(len(self.full)):
                        if self.full[i]:
                            output += cipher[i]
                    print(f"\n {output}")
                if self.reset: self.enigma.reset()
                self.line = ""
                self.full = []
                self.backspaces = 0
                print(f" i-enigma $> ", end='\r')
            elif key == keyboard.Key.backspace:
                if 1 in self.full:
                    #self.line = self.line[:-1]
                    self.backspaces += 1
                    self.full[len(self.line)-self.backspaces] = 0
                    output = ""
                    for i in range(len(self.full)):
                        if self.full[i]:
                            output += self.line[i]
                    print(f" i-enigma $> {output}      ", end='\r')
            elif key == keyboard.Key.esc:
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
        print(" i-enigma $>                 ", end='\r')
        listener = keyboard.Listener(on_press=self.on_press, suppress=True)
        listener.start()
        listener.join()
        return False
    
    def run(self):
        thread = threading.Thread(target=self.start_thread)
        thread.start()
        listener = keyboard.Listener(on_press=self.on_press, suppress=True)
        listener.start()
        listener.join()
        thread.join()