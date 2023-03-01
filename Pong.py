import time, os, sys, random, platform, getpass, pygame

global running
global gameTime
dis_hor = ' ╠════╬════╬════╣'
dis_hor_end = ' ╚════╩════╩════╝'
dis_hor_start = ' ╔════╦════╦════╗\n ║ 1. ║ 2. ║ 3. ║\n'
dis_ver = ' ║ '
gamedis_hor = '═════════════════════════════════════════════════════════════════════════════════'
gamedis_ver = '┊\n┊\n┊\n┊\n┊\n┊\n┊\n┊\n┊\n┊\n┊\n┊\n┊\n┊\n┊\n┊\n┊\n┊\n┊\n┊\n┊\n┊\n┊\n┊\n┊\n┊\n┊\n'

class Ball():
    wt = ""
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
    stick1 = ["██", "██", "██", "██", "██"]
    stick2 = ["╔╗", "║║", "║║", "║║", "╚╝"]
    stick3 = ["/\\","||", "||", "||", "\/"]
    SelectableSticks = [stick1[:], stick2[:], stick3[:]]
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
    print('\n')

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
            #time.sleep(0.25)
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



def SetupBoardDisplay():
    print(dis_hor_start + dis_hor)
    for i in range(5):
        #selSticks += str(i + 1) + '.\n'+ SelectableSticks[i] + '\n\n\n'
        #for j in range(len(SelectableSticks[i])):
        #temSelStick += str(i + 1) + '.\n' + SelectableSticks[i][j]
        print(str(dis_ver + SelectableSticks[0][i] + dis_ver + SelectableSticks[1][i] + dis_ver + SelectableSticks[2][i] + dis_ver))
    print(dis_hor_end)

    #for layer in range(5):
        #print(str(SelectableSticks[0][layer]))
    i = input('Kies een stick om te gebruiken:\n')
    while True:
        try:
            i = int(i)
            if (i > 0 and i <= len(SelectableSticks)):
                PlayerStick = SelectableSticks[i - 1]
                SelectableSticks.remove(SelectableSticks[i - 1])
                break
            else:
                i = input('Gekozen stick is niet geldig\nKies een stick om te gebruiken: ')
        except ValueError:
            i = input('Gekozen stick is niet geldig\nKies een stick om te gebruiken: ')
    temp = ''
    global PlayerSelectedStick
    for i in range(5):
        temp += PlayerStick[i] + '\n'
    print('Gekozen stick: \n' + temp)
    PlayerSelectedStick = temp
    temp = ''
    NewTimedText('PC kies een stick', 0.5)
    PCStick = random.choice(SelectableSticks[:])
    global PCSelectedStick
    for i in range(5):
        temp += PCStick[i] + '\n'
    input('PC heeft gekozen: \n' + temp)
    PCSelectedStick = temp

def UpdateBoardDisplay():
    SKEKE=""

def Update():
    print(PlayerSelectedStick)

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