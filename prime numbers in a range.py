x = int(input('Enter lower limit:\n'))
y = int(input('Enter upper limit:\n'))
for i in range(x, y + 1):
    if i == 1:
        print('1 is not prime. It is unique')
        continue
    for a in range(2, i):
        r = i % a
        if r == 0:
            print(i, 'is not prime as', a, 'divides', i)
            break
    else:
        print(i, 'is prime')
