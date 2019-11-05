x = int(input('Type number:'))
y = x
r = 0
while y:
    d = y % 10
    r = r * 10 + d
    y = y//10
if y == r:
    print('It is a palindrome as reverse of', x, 'is', r)
else:
    print('It is not a palindrome as reverse of', x, 'is', r)
