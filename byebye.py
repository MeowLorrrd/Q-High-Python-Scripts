
anyNum = ['1','2','3','4','5','6','7','8','9','0']
file = open('C:/Users/jayol/OneDrive/Documents/School/Informatica/P3P3P3/Oy/wordlist.txt', mode='r', encoding='utf-8');
print(f'\nBestand gevonden!\n\n{file}\n');

with open('C:/Users/jayol/OneDrive/Documents/School/Informatica/P3P3P3/Oy/a.txt', encoding='utf-8', mode='r') as file:
    contents = file.read();
    input(f'{contents}\n\n\t^Alle huidige woorden^');
    wordlist = []
    wordlist.append(contents.split());
    #wordlist = wordlist[0];
    input(f'{wordlist[0]}\n\n\t^Alle huidige woorden in een list^');
    """
    for i in range(len(wordlist[0])):
        if (wordlist[0][i].__contains__('a')):
            input('Illegale karakter gevonden!\nVerwijderen...');
            wordlist[0].remove(i);
    """
    l2 = wordlist[0];
    print(f'Oud: {wordlist}\n\nNieuw: {l2}');
    """
    for i in range(len(l2)):
        if l2[i].__contains__('a'):
            l2.pop(i);
            print('\nLijn verwijderd!')
    """
    while l2[:].__contains__('a'):
        if l2 == []:
            break;
        l2.clear();
        print(f'Over: {l2}', end='\r', flush=True);
        
    input(f'\n{l2}\n\n\t^Alle nieuwe, huidige woorden^');
input('\n\n\n\tDruk op [enter] om af te sluiten\n')