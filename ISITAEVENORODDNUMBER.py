#i see no flaws in this
def IsEven(num: int):
	return IsOdd(num + 1)
def IsOdd(num: int):
	return IsEven(num + 1)
Input = input('nummer: ')
validInput = False
while not validInput:
    try:
        Input = int(Input)
        validInput = True
        break
    except ValueError:
        print('Can\'t convert to type \'int\'')
        Input = input('nummer (pt2): ')
print('Is it even?: ' + str(bool(IsEven(Input))))