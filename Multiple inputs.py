x = [float(x) for x in input('Type multiple numbers separated by commas:\n').split(sep=', ')]
operation = input('Which operation:\n')
Sum = 0
Product = 1
if operation == '+' or operation == 'Sum' or operation == 'Add' or operation == 'Addition' or operation == 'sum' \
        or operation == 'add' or operation == 'summation' or operation == 'Summation' or operation == 'addition':
    for a in x:
        Sum += a
    print('Sum is', Sum)
elif operation == '*' or operation == 'Product' or operation == 'Multiply' or operation == 'Multiplication' or\
         operation == 'product' or operation == 'multiply' or operation == 'Multiplication':
    for a in x:
        Product *= a
    print('Product is', Product)

