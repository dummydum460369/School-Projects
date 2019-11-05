cmd = 'a'
repeat = 'Yes'
while cmd == 'a':
    while repeat == 'Yes':
        x = float(input('Type number 1:\n'))
        y = float(input('Type number 2:\n'))
        z = input(str('Which Operation? :\n'))
        if z == '+':
            print(x, '+', y, '=', x + y)
            print("You're welcome :)")
        elif z == '-':
            print(x, '-', y, '=', x - y)
            print(y, '-', x, '=', y - x)
        elif z == '*':
            print(x, '*', y, '=', x * y)
            repeat = str(input('Anything else(say Yes or No):\n'))
        elif z == '/':
            print('Quotient(', x, '/', y, ') =', x / y)
            print('Remainder(', x, '/', y, ') =', x % y)
            print('Quotient(', y, '/', x, ') =', y / x)
            print('Remainder(', y, '/', x, ') =', y % x)
            repeat = str(input('Anything else(say Yes or No):\n'))
        elif z == 'power':
            print(x, '^', y, '=', x ** y)
            print(x, '^', y, '=', y ** x)
            repeat = str(input('Anything else(say Yes or No):\n'))
        else:
            print("Sorry, I can't do that, ......yet :  (\n")
            repeat = str(input('Anything else(say Yes or No):\n'))
    print("You're welcome :)")
    print('＼(＾▽＾*)')
