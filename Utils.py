import random
import time
import sys
from os import path
sys.path.append(path.abspath("C:/Users/jayol/OneDrive/Documents/School/Informatica/P3P3P3/Oy"))


def ToLower(i):
    try:
        i = str(i)
    except ValueError:
        print("Fout: kan invoer niet veranderen naar 'string'")
    return i.lower()

def ToUpper(i):
    try:
        i = str(i)
    except ValueError:
        print("Fout: kan invoer niet veranderen naar 'string'")
    return i.upper()

def ToInt(i = 0):
    incorrectInput = False
    while not incorrectInput:
        try:
            i = int(i)
            incorrectInput = True
        except ValueError:
            print("Fout: kan invoer niet veranderen naar 'int'")
            i = input("\nProbeer een andere waarde in te vullen: ")
            if (i == "exit"):
                return -1
    return i

inp = input("I wuvv testing: ")
print("Ingevoerde input: '" + ToLower(inp) + "' " + "\nType invoer: " + str(type(inp)))

