import time, os;
def isPrime(n):
    for i in range(2, n // 2 + 1):
        if (not (n % i)):
            return 0;
    return 1;

def Col(r, g, b):
    return f'\033[38;2;{r};{g};{b}m';

def toInt(n):
    while True:
        try:
            n = int(n);
            return n if (n != 0) else (250001);
        except ValueError:
            if (n == ''):
                print('\n Returned default: 250001\n');
                return 250001;
            else:
                n = input(' Please enter a valid number (empty defaults to 250001): ');
'''
for i in range(40):
    print(f'{Col((255)if((100/20*i)<50)else(385-(int(255/100*(100/20*i)))),((int(255/100*(100/20*i)))*2)if((100/20*i)<50)else(255),0)}███',end='');
print('\n\n');
'''
def main():
    os.system('cls');
    os.system('color');
    print('\n\033[38;2;0;255;255m', end = '\r', flush = True);
    inp = input(f'{Col(0, 255, 255)} Program started...\n\n\n Enter number (empty defaults to 250001): ');
    intInp = toInt(inp);
    start = time.time();
    numPrimes = 0;
    numCount = 0;
    m = [];
    _time = time.time();
    for i in range(0, max(intInp, 3)):
        numCount += 1;
        numPrimes += isPrime(i);
        _time = round(time.time() - start);
        m = [
                ' second  (' if (_time >= 1) & (_time < 2) else (' seconds ('),
                (' minute)  ' if ((_time > 60) & (_time < 119)) else ( ' minutes) ')),
                Col((255) if ((100 / intInp * numCount) < 51) else (385 - (int(255/ 100 * (100 / intInp * numCount )))),
                ((int(255 / 100 * (100 / intInp * numCount))) * 2) if ((100 / intInp * numCount) < 50) else (255), 0)
            ]
        print(f'\tTime elapsed: {_time}{m[0]}{(_time // 60)}{m[1]}on loop {numCount}/{intInp}{m[2]} ({(100 / intInp * numCount):.1f}%){Col(0, 255, 255)}', end = '\r', flush = True);
    input(f'{Col(0, 255, 255)}\n\n Finished (returned: {numPrimes})!\n\n Total time to finish: {_time}{m[0]}{(_time // 60):.0f}{m[1]}\n Press [enter] to exit');

def main_simple():
    inp = input(' Program started...\n\n\n Enter number (empty defaults to 250001): ');
    intInp = toInt(inp);
    numPrimes = 0;
    timerStart = time.time();
    for i in range(0, max(intInp, 3)):
        numPrimes += isPrime(i);
    input(f' Finished (returned {numPrimes}) in {(time.time() - timerStart):.0f} seconds!\n Press [enter] to exit')

if __name__ == '__main__':

    Type = input(' What type of program do you want to run?\n\n [1] for Fancy\n [2] or empty for Basic\n\n ');
    if (Type == '1'):
        print('\n Running Fancy Mode!')
        main();
    else:
        print('\n Running Simple Mode!')
        main_simple();
