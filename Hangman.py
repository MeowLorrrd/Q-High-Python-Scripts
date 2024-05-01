import time, getpass, platform, webbrowser, os, random
replayGame = False

print(f"\n\tRunning on Python version {platform.python_version()}\n")
os.system('color');
if not ((platform.python_version().__contains__("3.10")) or (platform.python_version().__contains__("3.11")) or (platform.python_version().__contains__("3.12"))):
    print("\nJe hebt Python 3.10 of hoger nodig!\n")
    getpass.getpass("Druk op [Enter] om naar de Python website te gaan\n")
    webbrowser.open("https://www.python.org/downloads/")
    getpass.getpass("Druk op [Enter] om de app af te sluiten\n")
    quit()

def Col(r, g, b):
    return f'\033[38;2;{r};{g};{b}m';

def Clear():
    os.system('cls')

def GetTitle():
    defsplash = [
        '\n',
        '\t\t\t\t ╔═══════════════════════════════════════════════════════════════╗ \n',
        '\t\t\t\t╔╝░░░░░██╗░░░░░██╗███████╗██╗░░░░░██╗░░██╗░█████╗░░░██╗░██═╗░░░░░╚╗\n',
        '\t\t\t\t║░░░░░░██║░░░░░██║██╔════╝██║░░░░░██║░██╔╝██╔══██╗░████████║░░░░░░║\n',
        '\t\t\t\t║░░░░░░███╗██╗███║█████╗░░██║░░░░░█████═╝░██║░░██║░██╔██╗██╚╗░░░░░║\n',
        '\t\t\t\t║░░░░░░░████████╔╝██╔══╝░░██║░░░░░██╔═██╗░██║░░██║███║░╚╝███║░░░░░║\n',
        '\t\t\t\t║░░░░░░░░██║░██╔╝░███████╗███████╗██║░╚██╗╚█████╔╝██╔╝░░░░██║░░░░░║\n',
        '\t\t\t\t║░░░░░░░░░╚╝░░╚╝░░╚══════╝╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝░░░░░║\n',
        '\t\t\t\t╚╗░░░░░░░░░░░░░░░░░░░░██████╗░████████╗░░░░░██╗░░░░░░░░░░░░░░░░░░╔╝\n',
        '\t\t\t\t ║░░░░░░░░░░░░░░░░░░░░██╔══██╗░░░██╔══╝░░░░░██║░░░░░░░░░░░░░░░░░░║ \n',
        '\t\t\t\t ║░░░░░░░░░░░░░░░░░░░░██████╦╝░░░██║░░░░░░░░██║░░░░░░░░░░░░░░░░░░║ \n',
        '\t\t\t\t ║░░░░░░░░░░░░░░░░░░░░██╔══██╗░░░██║░░░░░░░██╔╝░░░░░░░░░░░░░░░░░░║ \n',
        '\t\t\t\t ║░░░░░░░░░░░░░░░░░░░░██████╦╝████████╗█████╔╝░░░░░░░░░░░░░░░░░░░║ \n',
        '\t\t\t\t╔╝░░░░░░░░░░░░░░░░░░░░╚═════╝░╚═══════╝╚════╝░░░░░░░░░░░░░░░░░░░░╚╗\n',
        '\t\t\t\t║░░░░██████╗░░░█████╗░░██╗░░░░░░░██████╗░░░░░░░██╗░███████╗░███╗░░║\n',
        '\t\t\t\t║░░░██╔════╝░░██╔══██╗░██║░░░░░░██╔════╝░░░░░░░██║░██╔════╝░███║░░║\n',
        '\t\t\t\t║░░░██║░███╗░░███████║░██║░░░░░░██║░███╗░░░░░░░██║░█████╗░░░░█╔╝░░║\n',
        '\t\t\t\t║░░░██║░░╚██╗░██╔══██║░██║░░░░░░██║░░╚██╗░░░░░██╔╝░██╔══╝░░░░╚╝░░░║\n',
        '\t\t\t\t║░░░░██████╔╝░██║░░██║░███████╗░░██████╔╝░█████╔╝░░███████╗░░█╗░░░║\n',
        '\t\t\t\t╚╗░░░╚═════╝░░╚═╝░░╚═╝░╚══════╝░░╚═════╝░░╚════╝░░░╚══════╝░░╚╝░░╔╝\n',
        '\t\t\t\t ╚════════════╦═════════════════════════════════╦════════════════╝ \n',
        '\t\t\t\t              ║ Drunk op [enter] om te starten! ║                  \n',
        '\t\t\t\t              ╚═════════════════════════════════╝                  \n'
        ]
    time.sleep(.75)
    border = ['╔', '╗', '╝', '╚', '═', '║', '╦']
    for i in range(len(defsplash)):
        for j in range(len(defsplash[i])):
            if ((any(x == defsplash[i][j] for x in border))):
                print(Col(155, 0, 155), end='');
                print(defsplash[i][j], end='');
            
            elif (defsplash[i][j] == '░'):
                print(Col(95, 0, 95), end='');
                print(defsplash[i][j], end='');
            else:
                print(Col(190, 0, 190), end='');
                print(defsplash[i][j], end='');
        time.sleep(0.025)
    getpass.getpass('')
    Clear()
    
def GetFancyOptions(sType: int):
    PreGame = [
        '\n',
        '\t  ╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮\n',
        '\t ╭╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╮\n',
        '\t╭╯\t╭───────────────────╮    ╔═══════════════════╗\t    ╰╮\n',
        '\t╰╮\t│     ╔════╗        │    ║    ╭─────────╮    ║\t    ╭╯\n',
        '\t╭╯\t│     ╚══╗ ║        │    ║    ╰───────╮ │    ║\t    ╰╮\n',
        '\t╰╮\t│        ║ ║        │    ║    ╭───────╯ │    ║\t    ╭╯\n',
        '\t╭╯\t│        ║ ║        │    ║    │ ╭───────╯    ║\t    ╰╮\n',
        '\t╰╮\t│    ╔═══╝ ╚═══╗    │    ║    │ ╰───────╮    ║\t    ╭╯\n',
        '\t╭╯\t│    ╚═════════╝    │    ║    ╰─────────╯    ║\t    ╰╮\n',
        '\t╰╮\t│                   │    ║                   ║\t    ╭╯\n',
        '\t╭╯\t│      Random       │    ║    Eigen Woord    ║\t    ╰╮\n',
        '\t╰╮\t╰───────────────────╯    ╚═══════════════════╝\t    ╭╯\n',
        '\t ╰╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╮╭╯\n',
        '\t  ╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯╰╯\n',
        '\n'
        ]
    specialChars = ['╭', '╮', '╰', '╯', '─', '│', '╔', '╗', '╝', '╚', '═', '║']
    if (sType == 1):
        for i in range(len(PreGame)):
            for j in range(len(PreGame[i])):
                if (any(x == PreGame[i][j] for x in specialChars)):
                    print(Col(155, 0, 155), end='');
                    print(PreGame[i][j], end='')
                else:
                    print(Col(190, 0, 190), end='');
                    print(PreGame[i][j], end='')
            #print(PreGame[i])
            time.sleep(0.05)
    
    pass

def GetHangman(type: int):
    match type:
        case 0:
            return "         \n         \n      \n      \n      \n      \n"
        case 1:
            return "         \n         \n      \n      \n      \n\t __|__\n"
        case 2:
            return "\t    _____\n\t   |/   |\n\t   |  \n\t   |  \n\t   |  \n\t __|__\n"
        case 3:
            return "\t    _____\n\t   |/   |\n\t   |   [\"]\n\t   |  \n\t   |  \n\t __|__\n"
        case 4:
            return "\t    _____\n\t   |/   |\n\t   |   [\"]\n\t   |   /|\\\n\t   |  \n\t __|__\n"
        case 5:
            return "\t    _____\n\t   |/   |\n\t   |   [\"]\n\t   |   /|\\\n\t   |   _|_\n\t __|__\n"
        case 6:
            return "\t       |\n\t       |\n\t   _________\n\t  |         |\n\t  | \/   \/ |\n\t  | /\   /\ |\n\t  |   ___   |   <- doodgemaakt :(\n\t  |_________|\n\t      \|/    \n\t     __|__   \n\t    /     \ \n"
        case _:
            return "\t    _\n\t   /\"\\\n\t  \\\\_//\n\t   \\|/\n\t    |\n\t   / \\\n\t  /   \\"

def GetTextBubbleFrame(frame: int):
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
            String += SelectedWord
            return "   (" + String + "! )"
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

def GetRandomWord():
    global SelectedWord
    SelectedWord = ""
    NewTimedText('Willekeurig woord aan het genereren', 0.334)
    with open('wordlist.txt', mode='r',encoding='utf-8') as file:
        lines = file.readlines();
        temp = random.choice(lines)
        SelectedWord = temp[0:len(temp)-1].lower()
        file.close()
    Clear()
    print('\nWoord gekozen!')
    time.sleep(0.334)
    #print(SelectedWord)
    PlayGame()
   
def SetInputWord():
   global SelectedWord
   SelectedWord = ""
   if SelectedWord != "":
       return
   tempSelectedWord = getpass.getpass(f"\n\tVoer een woord in\n\t{Col(0,255,0)}> {Col(190,0,190)}")
   tempSelectedWord = tempSelectedWord.lower()
   while not (IsValidWord(tempSelectedWord)):
       print("\tDit woord is ongeldig!")
       tempSelectedWord = getpass.getpass(f"\n\tVoer een nieuw, geldig woord in\n\t{Col(0,255,0)}> {Col(190,0,190)}")
       tempSelectedWord = tempSelectedWord.lower()
   showWord = input(f"\n\tWil je het woord laten zien?\n\t[Y/N]\n\t{Col(0,255,0)}> {Col(190,0,190)}")
   idkforaname = showWord.lower().__contains__("y")
   while idkforaname:
       print(f"\n\tGekozen woord: {Col(255,0,255)}{tempSelectedWord}{Col(190,0,190)}")
       changeWord = input(f"\tWil je het woord aanpassen?\n\t[Y/N]\n\t{Col(0,255,0)}> {Col(190,0,190)}")
       if changeWord.lower().__contains__("y"):
           Clear()
           tempSelectedWord = getpass.getpass(f"\n\tVoer een woord in\n\t{Col(0,255,0)}> {Col(190,0,190)}")
           tempSelectedWord = tempSelectedWord.lower()
           while not (IsValidWord(tempSelectedWord)):
               Clear()
               print(f"\n\tDit woord is ongeldig!")
               tempSelectedWord = getpass.getpass(f"Voer een nieuw, geldig woord in\n\t{Col(0,255,0)}> {Col(190,0,190)}")
               tempSelectedWord = tempSelectedWord.lower()
           else:
               Clear()
               showWord = input(f"\n\tWil je het woord laten zien?\n\t[Y/N]\n\t{Col(0,255,0)}> {Col(190,0,190)}")
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
    Clear()
    global replayGame
    replayGame = True
    Pre_Game()

def NewTimedText(message: str, secs: float, loopCount: int = 3):
    dots = []
    dot = ''
    for i in range(loopCount):
        dot += '.'
        dots.append(dot)
    if secs > 0:
        for i in range(loopCount):
            print(f"\t{message}{dots[i]}", end='\r', flush=True)
            time.sleep(secs)

def GameEnd(won: bool = False):
    Clear()
    if not (won):
        print(GetHangman(6))
        replay = getpass.getpass(f"\n\tJe hebt het galgje opgehangen D:\n\tZijn laatste woorden waren: \"{SelectedWord}\"\n\n\tWil je het spel opnieuw spelen?\n\t[Y/N]\n\t{Col(0,255,0)}> {Col(190,0,190)}")
    else:
        for i in range(0, 5):
            print(f"\t{GetTextBubbleFrame(i)}")
        print(GetHangman(7))
        replay = getpass.getpass(f"\n\tJe hebt het galgje gered! :D\n\n\tWil je het spel opnieuw spelen?\n\t[Y/N]\n\t{Col(0,255,0)}> {Col(190,0,190)}")
    if replay.lower().__contains__('y'):
        NewTimedText("Bord leegmaken", 0.334)
        time.sleep(0.5)
        Replay()
    else:
        Clear()
        print("\n\tBedankt voor het spelen!\n")
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
    print("\n\tGame is gestart!\n")
    time.sleep(1.5)
    Clear()
    print(f"{GetHangman(0)}\n\t{sober}\n\n\tGebruikte letters: geen. Fouten: (0/6)")
    while not gameWon and not (mistakes >= 6):
        NoLetters = AddedLettersString == ''
        lastChanceWarn = ''
        inputletter = input(f"\n\tVoer een letter in\n\t{Col(0,255,0)}> {Col(190,0,190)}")
        inputletter = inputletter.lower()
        incorrectInput = ((len(inputletter) != 1) or (not IsValidLetter(inputletter)) or (AddedLetters.__contains__(inputletter)))
        while incorrectInput:
            Clear()
            if (mistakes >= 5):
                lastChanceWarn = ' *Laatste zet!*'
            if (NoLetters):
                print(f"{GetHangman(mistakes)}\n\t{sober}\n\n\tGebruikte letters: geen. Fouten: ({mistakes}/6) {lastChanceWarn}")
            else:
                print(f"{GetHangman(mistakes)}\n\t{sober}\n\n\tGebruikte letters: {AddedLettersString}. Fouten: ({mistakes}/6) {lastChanceWarn}")
            print(f"\n\n\tDe invoer \"{Col(255,0,255)}{inputletter}{Col(190,0,190)}\" is onjuist")
            ErrorMessage = "\tReden: "
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
            inputletter = input(f"\n\tVoer een letter in\n\t{Col(0,255,0)}> {Col(190,0,190)}").lower()
            incorrectInput = ((len(inputletter) != 1) or (not IsValidLetter(inputletter)) or (AddedLetters.__contains__(inputletter)))
        else:
            AddedLetters.append(str(inputletter))
            if not (SelectedWord.__contains__(inputletter)):
                if not (mistakes >= 5):
                    Clear()
                    mistakes += 1
                    if (mistakes >= 5):
                        lastChanceWarn = ' *Laatste zet!*'
                    AddedLettersString = ''
                    for i in range(len(AddedLetters)):
                        if (len(AddedLetters) > 1 and not (i == 0)):
                            AddedLettersString = AddedLettersString + ', '
                        if not (AddedLettersString.__contains__(AddedLetters[i])):
                            AddedLettersString += AddedLetters[i]
                    print(f"{GetHangman(mistakes)}\n\t{sober}\n\n\tGebruikte letters: {AddedLettersString}. Fouten: ({mistakes}/6) {lastChanceWarn}")
                else:
                    GameEnd(False)
                    break
            else:
                for j in range(GetWordLength()):
                    if (SelectedWord[j].__contains__(inputletter)):
                        checkerBoard[j] = inputletter
                sober = ""
                for k in range(len(checkerBoard)):
                    sober += checkerBoard[k]
                if not (checkerBoard.__contains__('_')):
                    GameEnd(True)
                    break
                else:
                    Clear()
                    if (mistakes >= 5):
                        lastChanceWarn = ' *Laatste zet!*'
                    AddedLettersString = ''
                    for i in range(len(AddedLetters)):
                        if (len(AddedLetters) > 1 and not (i == 0 or i == 0 )):
                            AddedLettersString = AddedLettersString + ', '
                        AddedLettersString += AddedLetters[i]
                    print(f"{GetHangman(mistakes)}\n\t{sober}\n\n\tGebruikte letters: {AddedLettersString}. Fouten: ({mistakes}/6) {lastChanceWarn}")

def Pre_Game():
    global replayGame;
    if (not replayGame):
        GetTitle()
    GetFancyOptions(1)
    n = input(f'\n\tWil je een random woord krijgen [1] of zelf een woord invullen [2]?\n\t{Col(0,255,0)}> {Col(190,0,190)}')
    if (n == '2' or n.lower().__contains__('zelf')):
        Clear();
        SetInputWord();
    else:
        Clear()
        GetRandomWord();

if __name__ == '__main__':
    time.sleep(0.5)
    Clear()
    Pre_Game();
