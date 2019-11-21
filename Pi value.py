n = int(input('Enter accuracy:'))
pi = 0
for i in range(n + 1):
    pi += ((2 * ((-1) ** i)) * (3 ** ((1 / 2) - i))) / ((2 * i) + 1)
print(pi)
