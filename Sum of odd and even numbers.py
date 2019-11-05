x = int(input('Enter a number:\n'))
Sum_even = 0
Sum_odd = 0
for a in range(2, x+1, 2):
    Sum_even += a
print('Sum of first', x, 'even numbers is', Sum_even)
for a in range(1, x+1, 2):
    Sum_odd += a
print('Sum of first', x, 'odd numbers is', Sum_odd)
