from time import *


def is_prime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


start = time()
for a in range(1, 100000):
    is_prime(a)
end = time()
print(f'Time taken:{end - start}s')