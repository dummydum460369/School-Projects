x = [str(x) for x in input('Type expression:\n').split(sep='+')]
product = 1
presence_of_multiply = 'No'
Result = 0
presence_of_divide = 'No'
for element_no in range(0, len(x)):             #Product initiate
    element = x[element_no]
    for letter in element:
        if letter == '*':
            multiply = element.split(sep='*')
            presence_of_multiply = 'Yes'
            for y in multiply:
                product = product * float(y)
        else:
            pass
    if presence_of_multiply == 'Yes':
        x[element_no] = product
        product = 1
        presence_of_multiply = 'No'
    else:
        pass
print(x)
for num in x:
    z = float(num)
    Result = Result + z

print(Result)