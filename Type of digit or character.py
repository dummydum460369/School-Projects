x = str(input('Type a single character string:\n'))
if 'A' <= x <= 'Z':
    print(x, 'is a Upper case')
elif 'a' <= x <= 'z':
    print(x, 'is a Lower case')
elif '0' <= x <= '9':
    print(x, 'is a digit')
else:
    print(x, 'is a special character')