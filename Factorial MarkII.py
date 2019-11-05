x = int(input('Enter a number:\n'))
fact = 1
for a in range(1, x + 1):
    fact = fact * a
print('Factorial of', x, 'is', fact)
