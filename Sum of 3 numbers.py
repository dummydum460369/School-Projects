x = float(input('Type number 1:\n'))
y = float(input('Type number 2:\n'))
z = float(input('Type number 3:\n'))
Sum1 = x + y + z
if x == y:
    if x == z:
        Sum2 = 0
    else:
        Sum2 = z
elif y == z:
    Sum2 = x
elif x == z:
    Sum2 = y
else:
    Sum2 = Sum1
print('Numbers are', x, ',', y, ',', z)
print('Sum of all numbers =', Sum1)
print('Sum of all non-duplicate numbers =', Sum2)




