mapping = {}


def fibonacci(n):
    global mapping
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        if n in mapping:
            return mapping[n]
        else:
            mapping[n] = fibonacci(n - 2) + fibonacci(n - 1)
            return fibonacci(n - 2) + fibonacci(n - 1)


for i in range(1, 1001):
    print(i, ':', fibonacci(i))
