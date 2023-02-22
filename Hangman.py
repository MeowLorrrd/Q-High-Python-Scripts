import time, getpass, platform, webbrowser, os

print("\nRunning on Python version", str(platform.python_version()), "\n")
time.sleep(0.1)#debugging shenn
if not ((platform.python_version().__contains__("3.10")) or (platform.python_version().__contains__("3.11"))):
    print("\nJe hebt Python 3.10 of hoger nodig!\n")
    getpass.getpass("Druk op [Enter] om naar de Python website te gaan\n")
    webbrowser.open("https://www.python.org/downloads/")
    getpass.getpass("Druk op [Enter] om de app af te sluiten\n")
    quit()
#print("Python 10 installed: ", hasPythonTen, "\nPython 11 installed: ", hasPythonEleven, "\nCan run app: ", hasIncorrectPyVer)

def Clear():
    os.system('cls')

def GetHangman(type: int):
    match type:
        case 0:
            return "         \n         \n      \n      \n      \n      \n"
        case 1:
            return "         \n         \n      \n      \n      \n __|__\n"
        case 2:
            return "    _____\n   |/   |\n   |  \n   |  \n   |  \n __|__\n"
        case 3:
            return "    _____\n   |/   |\n   |   [\"]\n   |  \n   |  \n __|__\n"
        case 4:
            return "    _____\n   |/   |\n   |   [\"]\n   |   /|\\\n   |  \n __|__\n"
        case 5:
            return "    _____\n   |/   |\n   |   [\"]\n   |   /|\\\n   |   _|_\n __|__\n"
        case 6:
            return "\n       |\n       |\n   _________\n  |         |\n  | \/   \/ |\n  | /\   /\ |\n  |   ___   |   <- doodgemaakt :(\n  |_________|\n      \|/    \n     __|__   \n    /     \ \n"
        case _:
            return "    _\n   /\"\\\n  \\\\_//\n   \\|/\n    |\n   / \\\n  /   \\"

def GetTextBubble(frame: int):
    match frame:
        case 0:
            String = ''
            for i in range(GetWordLength()):
                String += '_'
            return "     _" + String + "_ "
        case 1:
            String = ''
            for i in range(GetWordLength()):
                String += ' '
            return "    /" + String + "  \\"
        case 2:
            String = ''
            for i in range(max(int(GetWordLength() * 0.1), 2)):
                String += ' '
            String += SelectedWord + '!'
            for i in range(max(int(GetWordLength() * 0.1), 1)):
                String += ' '
            return "   (" + String + ")"
        case 3:
            String = ''
            for i in range(GetWordLength()):
                String += '_'
            return "    \\  " + String + "/"
        case _:
            String = ''
            for i in range(GetWordLength()):
                String += '_'
            return "     \/"
   
def SetInputWord():
   global SelectedWord
   SelectedWord = ""
   if SelectedWord != "":
       return
   print("")
   tempSelectedWord = getpass.getpass("Voer een woord in: ")
   tempSelectedWord = tempSelectedWord.lower()
   while not (IsValidWord(tempSelectedWord)):
       print("Dit woord is ongeldig!")
       tempSelectedWord = getpass.getpass("Voer een nieuw, geldig woord in: ")
       tempSelectedWord = tempSelectedWord.lower()
   showWord = input("\nWil je het woord laten zien?\n[Y/N]: ")
   idkforaname = showWord.lower().__contains__("y")
   while idkforaname:
       print("Gekozen woord: ", tempSelectedWord)
       changeWord = input("Wil je het woord aanpassen?\n[Y/N]: ")
       if changeWord.lower().__contains__("y"):
           Clear()
           tempSelectedWord = getpass.getpass("Voer een woord in: ")
           tempSelectedWord = tempSelectedWord.lower()
           while not (IsValidWord(tempSelectedWord)):
               Clear()
               print("Dit woord is ongeldig!")
               tempSelectedWord = getpass.getpass("Voer een nieuw, geldig woord in: ")
               tempSelectedWord = tempSelectedWord.lower()
           else:
               Clear()
               showWord = input("\nWil je het woord laten zien?\n[Y/N]: ")
               idkforaname = showWord.lower().__contains__("y")
       else:
           idkforaname = False;
   else:
       SelectedWord = tempSelectedWord.lower()
       Clear()
       PlayGame()

def GetWordLength():
    return int(len(SelectedWord))

def SetDefaultWord():
    line = ""
    if line != "":
        return
    for _ in range(GetWordLength()):
        line += '_'
    return line

def IsValidLetter(string):
    string = str(string.lower())
    for i in range(97, 123):#All smol
        try:
            i = chr(i)
            if (string.__contains__(i)):
                return True
        except:
            return False
    for j in range (65, 91):#All cap
        try:
            string = chr(j)
            if (string.__contains__(j)):
                return True
        except:
            return False
    return False

def ContainsValidLetterOnly(string):
    string = str(string)
    for i in range(len(string)):
        if not IsValidLetter(string[i]):
            return False
    return True

def IsValidWord(string):
    string = str(string)
    if ((len(string) < 2) or (len(string) > 20)):
        return False
    if not (ContainsValidLetterOnly(string)):
        return False
    return True

def Replay():
    SelectedWord = ""
    Clear()
    SetInputWord()

def NewTimedText(message: str, secs: float, loopCount: int = 3):
    dots = []
    dot = ''
    for i in range(loopCount):
        dot += '.'
        dots.append(dot)
    if secs > 0:
        for i in range(loopCount):
            print(message + dots[i], end='\r', flush=True)
            time.sleep(secs)

def GameEnd(won: bool = False):
    Clear()
    if not (won):
        print(GetHangman(6))
        replay = getpass.getpass("\nJe hebt het galgje opgehangen D:\nZijn laatste woorden waren: \"" + SelectedWord + "\"\n\nWil je het spel opnieuw spelen? [Y/N]: ")
    else:
        for i in range(0, 5):
            print(GetTextBubble(i))
        print(GetHangman(7))
        replay = getpass.getpass("\nJe hebt het galgje gered! :D\n\nWil je het spel opnieuw spelen? [Y/N]: ")
    if replay.__contains__('y'):
        print("Bord leegmaken...")
        time.sleep(0.5)
        Replay()
    else:
        Clear()
        print("\nBedankt voor het spelen!\n")
        time.sleep(1.5)
        NewTimedText("Spel verlaten", 0.9, 3)

def PlayGame():
    mistakes = 0
    gameWon = False
    AddedLetters = []
    checkerBoard = []
    AddedLettersString = ''
    for i in range (GetWordLength()):
        checkerBoard.append('_')
    sober = ""
    for x in range(len(checkerBoard)):
        sober += '_'
    print("\nGame is gestart!\n\n " + sober + "\n")
    while not gameWon and not (mistakes >= 6):
        NoLetters = AddedLettersString == ''
        inputletter = input("\nLetter: ")
        inputletter = inputletter.lower()
        incorrectInput = ((len(inputletter) != 1) or (not IsValidLetter(inputletter)) or (AddedLetters.__contains__(inputletter)))
        while incorrectInput:
            Clear()
            if (NoLetters):
                print(GetHangman(mistakes), "\n ", sober, "\n\nGebruikte letters: geen. (" + str(mistakes) + "/6)")
            else:
                print(GetHangman(mistakes), "\n ", sober, "\n\nGebruikte letters: ", str(AddedLettersString) + ". (" + str(mistakes) + "/6)")
            print("\n\nDe invoer \"" + inputletter + "\" is onjuist")
            ErrorMessage = "Reden: "
            if (len(inputletter) != 1):
                ErrorMessage += "onjuist aantal karakters"
            if not (IsValidLetter(inputletter)):
                if (ErrorMessage.__contains__("onjuist")):
                    ErrorMessage += ", "
                ErrorMessage += "ongeldig karakter"
            if (AddedLetters.__contains__(inputletter)):
                if (ErrorMessage.__contains__("ongeldig") or ErrorMessage.__contains__("onjuist")):
                    ErrorMessage += ", "
                ErrorMessage += "letter is al toegevoegd"
            print(ErrorMessage + "\n")
            inputletter = input("Voer een letter in: ")
            inputletter = inputletter.lower()
            incorrectInput = ((len(inputletter) != 1) or (not IsValidLetter(inputletter)) or (AddedLetters.__contains__(inputletter)))
        else:
            AddedLetters.append(str(inputletter))
            if not (SelectedWord.__contains__(inputletter)):
                if not (mistakes >= 5):
                    Clear()
                    mistakes += 1
                    AddedLettersString = ''
                    for i in range(len(AddedLetters)):
                        if (len(AddedLetters) > 1 and not (i == 0)):
                            AddedLettersString = AddedLettersString + ', '
                        if not (AddedLettersString.__contains__(AddedLetters[i])):
                            AddedLettersString += AddedLetters[i]
                    print(GetHangman(mistakes), "\n ", sober, "\n\nGebruikte letters: ", str(AddedLettersString) + ". (" + str(mistakes) + "/6)")
                else:
                    GameEnd(False)
                    break
            else:
                for j in range(GetWordLength()):
                    if (SelectedWord[j].__contains__(inputletter)):
                        checkerBoard[j] = inputletter
                #print("Word length: ", GetWordLength(), "\nSelected word: ", SelectedWord, "\nInput Letter: ", inputletter, "\nChecker board: ", checkerBoard)
                sober = ""
                for k in range(len(checkerBoard)):
                    sober += checkerBoard[k]
                if not (checkerBoard.__contains__('_')):
                    GameEnd(True)
                    break
                else:
                    Clear()
                    AddedLettersString = ''
                    for i in range(len(AddedLetters)):
                        if (len(AddedLetters) > 1 and not (i == 0 or i == 0 )):
                            AddedLettersString = AddedLettersString + ', '
                        AddedLettersString += AddedLetters[i]
                    print(GetHangman(mistakes), "\n ", sober, "\n\nGebruikte letters: ", str(AddedLettersString) + ". (" + str(mistakes) + "/6)")

SetInputWord()
