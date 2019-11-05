x = int(input('Enter a Number:\n'))
r = 9
if x == 1:
    print('1 is not prime')
for a in range(2, x):
    r = x % a
    if r == 0:
        print(x, 'is not prime as', a, 'divides', x)
        break
else:
    print(x, 'is prime')
