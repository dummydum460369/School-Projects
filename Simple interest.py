p = float(input('Borrowed amount:'))
r = float(input('At what rate(annual):'))
t = float(input('How long(in years):'))
Interest = (p * t * r) / 100
Amount = p + Interest
print('Amount of', Amount, 'must be paid.\nInterest =', Interest)

