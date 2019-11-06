from math import *
n = int(input('Enter accuracy:'))
e = 0
for i in range(n+1):
    e += 1/(factorial(i))
print(e)