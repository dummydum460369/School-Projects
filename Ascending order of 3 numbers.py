x = float(input('Type number 1:\n'))
y = float(input('Type number 2:\n'))
z = float(input('Type number 3:\n'))
if x > y and x > z:
    if y > z:
        print(x, ">", y, '>', z)
    elif y < z:
        print(x, ">", z, '>', y)
    elif y == z:
        print(x, ">", z, '=', y)
elif y > x and y > z:
    if x > z:
        print(y, ">", x, '>', z)
    elif x < z:
        print(y, ">", z, '>', x)
    elif x == z:
        print(y, ">", z, '=', x)
elif z > x and z > y:
    if x > y:
        print(z, ">", x, '>', y)
    elif y < x:
        print(z, ">", y, '>', x)
    elif y == x:
        print(z, ">", y, '=', x)
elif x == y and y == z:
    print(z, "=", y, '=', x)
