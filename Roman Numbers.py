x = int(input('Type your number:'))
while x < 1:
    x = int(input('Only Natural Numbers\nType again:'))
roman_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
value_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
count = 0
roman_no = ''
while x > 0:
    for i in range(x // value_list[count]):
        roman_no += roman_list[count]
        x += -value_list[count]
    count += 1
print('roman form:', roman_no)
