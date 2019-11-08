from math import *

n = int(input('Enter accuracy:'))
x = float(input('Enter power of e'))
e = 0
for i in range(n + 1):
    e += (x ** i) / (factorial(i))
print(e)
