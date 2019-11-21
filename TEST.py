x = 'abc'
while (n := len(x)) < 6:
    print(n)
    x = x[::] + 'a'
