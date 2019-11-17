from math import *
from functools import lru_cache
from time import *

prime_cache = {}


@lru_cache(maxsize=1000000000)
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        prime_cache[n] = True
        return True
    for i in prime_cache:
        if n % i == 0:
            return False

    for i in range(3, floor(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    prime_cache[n] = True
    return True


start = time()
for a in range(1, 100000):
    is_prime(a)
end = time()
print(f'Time taken:{end - start}s')
