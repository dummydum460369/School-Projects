print('Enter 5 numbers followed by 1 divisor')
a = float(input('Enter number:\n'))
b = float(input('Enter number:\n'))
c = float(input('Enter number:\n'))
d = float(input('Enter number:\n'))
e = float(input('Enter number:\n'))
f = float(input('Enter  divisor number:\n'))
count = 0
print('The Multiples are:')
if a % f == 0:
    print(a)
    count += 1
if b % f == 0:
    print(b)
    count += 1
if c % f == 0:
    print(c)
    count += 1
if d % f == 0:
    print(d)
    count += 1
if e % f == 0:
    print(e)
    count += 1
print(count, 'multiples found of', f)
