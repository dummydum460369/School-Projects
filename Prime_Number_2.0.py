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
        if i > floor(sqrt(n))+1:
            break
        if n % i == 0:
            return False

    prime_cache[n] = True
    return True


start = time()
for a in range(1, 1000000):
    if is_prime(a):
        print(a)
end = time()
print(f'Time taken:{end - start}s')
