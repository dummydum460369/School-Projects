x = int(input('Type number 1:\n'))
y = int(input('Type number 2:\n'))
z = int(input('Type number 3:\n'))
Max = x
if y > Max:
    Max = y
if z > Max:
    Max = z
print('Max Value is:', Max)
