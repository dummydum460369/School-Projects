import math
ll = int(input('Lower Limit:'))
x = ll
while x >= ll:
    y = str(x)
    Sum = 0
    for i in y:
        num = int(i)
        f = math.factorial(num)
        Sum = Sum + f
    if Sum == x:
        print(x, 'is strong')
    else:
        pass
    x = x+1
else:
    print('Done')
