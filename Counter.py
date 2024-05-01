import os

Counter = 0;
cInput = "";
os.system("color");
while True:
    #os.system("cls");
    print(f"\033[38;2;255;55;225mCurrent Count: \033[38;2;0;255;34m{Counter}\033[38;2;255;55;225m // Input: \033[38;2;25;255;34m", end = " ", flush = True);
    cInput = input();
    if (len(cInput) == 0):
        Counter += 1;
    elif cInput.isnumeric():
        Counter = int(cInput);
    elif (cInput.lower().__contains__("e")):
        break;
quit();