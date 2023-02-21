import random
import time

def GetRandomNum():
    i = random.randint(0, 101)
    return i

def StringToInt(inputString):
    incorrectInput = False
    while not incorrectInput:
        try:
            inputString = int(inputString)
            incorrectInput = True
        except ValueError:
            print("Fout: kan invoer niet veranderen naar 'int'")
            inputString = input("\nProbeer een andere waarde in te vullen: ")
    return inputString

def PlayGame():
    chosenNum = GetRandomNum()
    playerNum = input("Probeer het juiste nummer te raden: ")
    playerNum = StringToInt(playerNum)
    while playerNum != chosenNum:
        if playerNum > chosenNum:
            print("Je moet lager!")
            playerNum = input("Probeer het juiste nummer te raden: ")
            playerNum = StringToInt(playerNum)
        else:
            print("Je moet hoger!")
            playerNum = input("Probeer het juiste nummer te raden: ")
            playerNum = StringToInt(playerNum)
    print(str(namePlayerOne) + ", je hebt gewonnen!\n")
    time.sleep(.5)
    ReplayGame()

def ReplayGame():
    replayString = input("Wil je opnieuw spelen?\n[Y/N]: ")
    if replayString.lower().__contains__("n"):
        print("Bedankt voor het spelen!\n")
        time.sleep(.3)
        periods = [" ",".","..","..."]
        for i in range(len(periods)):
            time.sleep(0.3334)
            print("Spel verlaten" + periods[i], end='\r', flush=True)
        quit()
    else:
        PlayGame()

def DoGamerule():
    Rules = ["\nHet spel genereert een getal van 0 tot en met 100", 
             "\nJij probeert het getal te raden",
             "\nHet spel geeft aan of je hoger of lager moet raden",
             "\nAls je het getal hebt geraden, win je!",
             "\nHet spel gaat nu starten!\n"]
    shouldRule = input("Wil je een uitleg?\n[Y/N]: ")
    shouldRule = shouldRule.lower()
    if shouldRule.__contains__("n"):
        return
    else:
        for i in range(len(Rules)):
            print(Rules[i])
            time.sleep(0.6667)

def GetName():
    global namePlayerOne
    namePlayerOne = str(input("Wat is je naam?: "))
    while len(namePlayerOne) < 1 or namePlayerOne == " ":
        print("\nTe korte naam...\n")
        namePlayerOne = str(input("Geef een GOEDE naam door: "))
        if len(namePlayerOne) > 1 and namePlayerOne != " ":
           break
    print("Welkom " + namePlayerOne+ "!\n")
    return namePlayerOne

GetName()
DoGamerule()
PlayGame()