lower = int(input('Lower limit;\n'))
upper = int(input('Upper limit;\n'))
for x in range(lower, upper+1):
    mid = x//2 + 1
    Sum = 0
    for i in range(1, mid):
        if x % i == 0:
            Sum += i
        else:
            pass
    if Sum == x:
        print(x, 'is a perfect number')
    else:
        pass
