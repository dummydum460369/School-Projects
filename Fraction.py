x = input('Fraction1')
y = input('Fraction2')
if '/' not in x:
    x = x + '/1'
if '/' not in y:
    y = y + '/1'


def decimal_to_fraction(fraction):
    lst = fraction.split('/')
    for i in range(len(lst)):
        x = lst[i]
        if '.' in x:
            num_of_zero = len(x[x.find('.') + 1:])
            numerator = x[:x.find('.')] + x[x.find('.') + 1:] if i == 0 else lst[0] + '0' * num_of_zero
            denominator = lst[1] + '0' * num_of_zero if i == 0 else x[:x.find('.')] + x[x.find('.') + 1:]
            return numerator + '/' + denominator
        else:
            return fraction


print(decimal_to_fraction(x))
