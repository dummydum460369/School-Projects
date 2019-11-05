count = Sum = 0
repeat = 'y'
error = 0
while repeat == 'y':
    x = str(input('Enter a number(Type abort to stop adding):\n'))
    if x == 'abort':
        break
    for a in x:
        if '1' <= a <= '9' or a == '.':
            pass
        else:
            print("Don't enter a string or a negative number")
            break
    else:
        if x[0] == '.':
            x = '0' + x
        x = float(x)
        Sum += x
        count += 1
print('You added', count, 'numbers whose sum is', Sum)




