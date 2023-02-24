import time, os, sys, random, platform, getpass

global running
global gameTime

class Ball():
    wt = ""
#Utils
def Clear():
    os.system('cls')
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

def GetSplash(exitSplash: bool = False, shouldClear: bool = False):
    if (shouldClear):
        Clear()
    splashArray = [
                " ",
                " ",
                "               ███████═╗░░█████╗░███╗░░██╗░░█████╗░░░░███╗",
                "               ██╔═══██║░██╔══██╗████╗░██║░██╔══╝╚╗░░░███║",
                "               ███████╔╝░██║░░██║██╔██╗██║░██║░░██╚╗░░░█╔╝",
                "               ██╔════╝░░██║░░██║██║╚████║░██╝░░░██║░░░╚╝░",
                "               ██║░░░░░░░╚█████╔╝██║░╚███║░╚██████╔╝░░░█╗░",
                "               ╚═╝░░░░░░░░╚════╝░╚═╝░░╚══╝░░╚═════╝░░░░╚╝░"
                    ]
    splash = ''
    for i in range(len(splashArray)):
        splash += splashArray[i] + '\n'
        if not (exitSplash):#so at start
            print(splash)
            #time.sleep(0.35)
            Clear()
    if (exitSplash):
        splashArray2 = [
                #"           ------------------------------------------",
                "       ██████╗░███████╗██████╗░░█████╗░███╗░░██╗██╗░░██╗████████╗",
                "       ██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗░██║██║░██╔╝╚══██╔══╝",
                "       ██████╦╝█████╗░░██║░░██║███████║██╔██╗██║█████═╝░░░░██║░░░",
                "       ██╔══██╗██╔══╝░░██║░░██║██╔══██║██║╚████║██╔═██╗░░░░██║░░░",
                "       ██████╦╝███████╗██████╦╝██║░░██║██║░╚███║██║░╚██╗░░░██║░░░",
                "       ╚═════╝░╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═╝░░░",
                "   ██╗░░░░░██╗░█████╗░░░█████╗░██████╗░░░░██╗░░░██╗███████╗████████╗",
                "   ░██╗░░░██╔╝██╔══██╗░██╔══██╗██╔══██╗░░░██║░░░██║██╔════╝╚══██╔══╝",
                "   ░░██╗░██╔╝░██║░░██║░██║░░██║██████╔╝░░░████████║█████╗░░░░░██║░░░",
                "   ░░░████╔╝░░██║░░██║░██║░░██║██╔══██╗░░░██╔═══██║██╔══╝░░░░░██║░░░",
                "   ░░░░██╔╝░░░╚█████╔╝░╚█████╔╝██║░░██║░░░██║░░░██║███████╗░░░██║░░░",
                "   ░░░░╚═╝░░░░░╚════╝░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚══════╝░░░╚═╝░░░",
                "       ░██████╗███████═╗███████╗██╗░░░░░███████╗███╗░░██╗░░███╗",
                "       ██╔════╝██╔═══██║██╔════╝██║░░░░░██╔════╝████╗░██║░░███║",
                "       ╚█████╗░███████╔╝█████╗░░██║░░░░░█████╗░░██╔██╗██║░░░█╔╝",
                "       ░╚═══██╗██╔════╝░██╔══╝░░██║░░░░░██╔══╝░░██║╚████║░░░╚╝░",
                "       ██████╔╝██║░░░░░░███████╗███████╗███████╗██║░╚███║░░░█╗░",
                "       ╚═════╝░╚═╝░░░░░░╚══════╝╚══════╝╚══════╝╚═╝░░╚══╝░░░╚╝░"
                    ]
        for i in range(len(splashArray2)):
            splash += splashArray2[i] + '\n'
    return splash

def BoringSetup():
    global PlayerPos
    PlayerPos = [1, 15]
    global PlayerVel
    global BallPos
    BallPos = [26, 15]
    global BallVel
    global PCPos
    PCPos = [51, 15]
    global PCVel
    global PlayerStick
    global SelectableSticks
    global PCStick
    SelectableSticks =   ["██\n██\n██\n██\n██", "╔╗\n║║\n║║\n║║\n╚╝", "/\\\n||\n||\n||\n\\/"]
    PlayerStick = SelectableSticks[0]
    #PCStick = SelectableSticks[0]

def SetupBoardDisplay():
    selSticks = ''
    for i in range(len(SelectableSticks)):
        selSticks += str(i + 1) + '.\n'+ SelectableSticks[i] + '\n\n\n'
    i = input('Kies een stick om te gebruiken:\n' + selSticks)
    while True:
        try:
            i = int(i)
            if (i > 0 and i <= len(SelectableSticks)):
                PlayerStick = SelectableSticks[i - 1]
                SelectableSticks.remove(SelectableSticks[i -1])
                break
            else:
                i = input('Gekozen stick is niet geldig\nKies een stick om te gebruiken: ')
        except ValueError:
            i = input('Gekozen stick is niet geldig\nKies een stick om te gebruiken: ')
    NewTimedText('PC kies een stick', 0.5)
    PCStick = random.choice(SelectableSticks)
    input('\nPC heeft gekozen: \n' + PCStick)
def UpdateBoardDisplay():
    SKEKE=""

def Update():
    print(PCStick)
    sek=""

def Main():
    running = True
    doneSetup = False
    if not (doneSetup):
        print(GetSplash())
        getpass.getpass("                     Druk op [ENTER] om te starten!")
        Clear()
        BoringSetup()
        SetupBoardDisplay()
        gameTime = 0
        doneSetup = True
    while running:
        time.sleep(1/24)#24 fps i think?
        gameTime += 1
        #print(str(gameTime))
        Clear()
        Update()

Main()