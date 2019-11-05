import math
radius = float(input('Enter Radius:\n'))
choice = int(input('What do you need:\n1)Area\n2)Perimeter:\n'))
if choice == 1:
    area = math.pi * radius * radius
    print('Area =', area)
elif choice == 2:
    perimeter = 2 * math.pi * radius
    print('Perimeter =', perimeter)
