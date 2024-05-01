import random, sys, os, platform, time, getpass

def Clear():
    os.system('cls')

def GetCard(type:int, string: str = ''):
    card_hor_top = '╔═══════════╗'
    card_hor_bot = '╚═══════════╝'
    if type == 0:
        return ['             ','             ','             ','             ','             ','             ','             ','             ','             ','             ']
    elif type == 1:
        return [card_hor_top, '║ \       / ║', '║  \     /  ║','║   \   /   ║','║    \ /    ║','║    / \    ║','║   /   \   ║','║  /     \  ║','║ /       \ ║', card_hor_bot]
    elif type == 2:
        s_space = ''
        s_space_extra = ''
        if (len(string) % 2 == 0):
            s_space_extra = ' '
        if (len(string) == 3):
            s_space += '    '
        elif (len(string) == 4 or len(string) == 5):
            s_space += '   '
        elif (len(string) == 6 or len(string) == 7):
            s_space += '  '
        elif (len(string) == 8 or len(string) == 9):
            s_space += ' '
        return card_hor_top + '\n║           ║\n║           ║\n║           ║\n║' + s_space + string + s_space + s_space_extra + '║\n║           ║\n║           ║\n║           ║\n' + card_hor_bot
def BoringSetupCards(type: int):
    return

for i in range(10):
    print(GetCard(0)[i])
for i in range(10):
    print(GetCard(1)[i])
input()
def Game():
    FullCards = []
    CardEmpty = GetCard(0)
    CardSelected = GetCard(1)
    words = ['Fiets', 'Tafel' ,'Appel' ,'Gisteren']
    for i in range(len(words)):
        FullCards.append(GetCard(2, words[i]))
        print('Woord: '+words[i]+'\nKaart: '+'\n'+ FullCards[i])
    for i in range(10):
        print(CardSelected[i]);
    input('Press [enter] to continue...: ')
Game()