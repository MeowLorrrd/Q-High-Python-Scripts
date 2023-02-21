import random, time, sys, random, os


def ToLower(i):
    try:
        i = str(i)
        return i.lower()
    except ValueError:
        print("Fout: kan invoer niet veranderen naar 'string'")

def ToUpper(i):
    try:
        i = str(i)
        return i.upper()
    except ValueError:
        print("Fout: kan invoer niet veranderen naar 'string'")

def ToInt(i = 0):
    correctInput = False
    while not correctInput:
        try:
            i = int(i)
            correctInput = True
        except ValueError:
            print("Fout: kan invoer niet veranderen naar 'int'")
            i = input("\nProbeer een andere waarde in te vullen: ")
            if (i == "exit"):
                return -1
    return i

inp = input("I wuvv testing: ")
print("Ingevoerde input: '" + ToLower(inp) + "' " + "\nType invoer: " + str(type(inp)))

