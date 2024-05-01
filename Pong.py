import time, os, sys, random, platform, getpass, keyboard

global running
global gameTime

class Ball():
    wt = ""
class Utils():
    def Clear(preCls=0,postCls=0):
        time.sleep(preCls);
        os.system('cls');
        time.sleep(postCls);
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
    def TryNum(i):
        while True:
            try:
                i = int(i)
                return i;
            except ValueError:
                i = input('Kan niet naar type \'int\' veranderen\nVoer een geldig getal in: ')
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
        Utils.Clear(0,0);
    splashArray = [
                "\n",
                "\n",
                "\t\t\t\t███████╗░░░█████╗░███╗░░██╗░░█████╗░░░░███╗\n",
                "\t\t\t\t██╔═══██░░██╔══██╗████╗░██║░██╔══╝╚╗░░░███║\n",
                "\t\t\t\t███████║░░██║░░██║██╔██╗██║░██║░░██╚╗░░░█╔╝\n",
                "\t\t\t\t██╔════╝░░██║░░██║██║╚████║░██╝░░░██║░░░╚╝░\n",
                "\t\t\t\t██║░░░░░░░╚█████╔╝██║░╚███║░╚██████╔╝░░░█╗░\n",
                "\t\t\t\t╚═╝░░░░░░░░╚════╝░╚═╝░░╚══╝░░╚═════╝░░░░╚╝░\n"
                    ]
    splash = ''
    for i in range(len(splashArray)):
        splash += splashArray[i] + '\n'
        for j in range(len(splashArray[i])): 
            print(splashArray[i][j], end='',flush=True)
            time.sleep(0.025)
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
    print(' ╔════╦════╦════╗\n ║ 1. ║ 2. ║ 3. ║\n ╠════╬════╬════╣')
    for i in range(5):
        print(f' ║ {SelectableSticks[0][i]} ║ {SelectableSticks[1][i]} ║ {SelectableSticks[2][i]} ║ ')
    print(' ╚════╩════╩════╝')

    #for layer in range(5):
        #print(str(SelectableSticks[0][layer]))
    while True:
        i = input('Kies een stick om te gebruiken: ')
        i=Utils.TryNum(i);
        if (i>=1) and (i<=3):
            break
        print(f'Getal is te {"groot" if (i > 3) else "klein"}')
    PlayerStick=SelectableSticks[i-1];
    SelectableSticks.remove(SelectableSticks[i-1]);
    temp = ''
    global PlayerSelectedStick
    for i in range(5):
        temp += PlayerStick[i] + '\n'
    print('Gekozen stick: \n' + temp)
    PlayerSelectedStick = temp
    temp = ''
    Utils.NewTimedText('PC kies een stick', 0.5)
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
        GetSplash()
        getpass.getpass("\n\t\t\t\t\tDruk op [ENTER] om te starten!\n")
        Utils.Clear(0,0)
        BoringSetup()
        SetupBoardDisplay()
        gameTime = 0
        doneSetup = True
    while running:
        time.sleep(1/12)#24 fps i think?
        gameTime += 1
        #print(str(gameTime))
        Utils.Clear()
        Update()
        global PCSelectedStick
        print(PCSelectedStick)

if __name__ == '__main__':
    Main()