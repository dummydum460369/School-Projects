from tkinter import *
import math
master = Tk()
master.configure(bg='Black')
master.title('--Expression Calculator MARK-VI(by-Ayan)--')


def search_for_div_in_element(x):                   # Determines presence of division sign in element(x)
    for letter in x:
        if letter == '/':
            return 'Yes'
        else:
            pass
    else:
        return 'No'


def split(x, y):                                    # Splits x into a list using separator y
    return x.split(sep=y)


def divide_elements_in_list(x):                     # Divides items in a list(x) from left to right
    y = float(x[0])
    for z in range(1, len(x)):
        w = float(x[z])
        y = y / w
    return y


def search_for_multiply_in_element(x):              # Determines presence of multiplication sign in element(x)
    for letter in x:
        if letter == '*':
            return 'Yes'
        else:
            pass
    else:
        return 'No'


def multiply_elements_in_list(x):                     # Multiplies items in a list(x)
    y = 1
    for z in range(0, len(x)):
        w = float(x[z])
        y = y * w
    return y


def add_elements_in_list(x):                           # Adds items in a list(x)
    y = 0
    for w in x:
        y = y + float(w)
    return y


def search_for_brackets_in_element(x):              # Determines presence of open bracket in element(x)
    for letter in x:
        if letter == '(':
            return 'Yes'
        else:
            pass
    else:
        return 'No'


def scan_first_occurrence_and_return_index(x, y):
    for first_index in range(0, len(x)):
        if x[first_index] == y:
            return first_index
        else:
            pass
    else:
        return None


def return_index_of_first_and_last_occurrence(x, y, z=''):
    # Determines index values of first occurrence of y in x and last occurrence of z(default=y) in x.
    # REQUIRES 2 VARIABLES!
    # Edit 1: Takes total instances of starting index and limits second index accordingly(optimised for calculator)
    if z == '':
        z = y
    index = 0
    y_instances = 0
    z_instances = 0
    while index < len(x):
        print('Index:', index)
        if y_instances == z_instances and y_instances != 0:
            print('y:', y_instances, 'z:', z_instances)
            index = index-1
            print('Index:', index)
            break
        elif x[index] == y:
            print('Index:', index)
            print('y:', y_instances, 'z:', z_instances)
            if y_instances == z_instances and y_instances != 0:
                print('y:', y_instances, 'z:', z_instances)
                index = index-1
                print('Index:', index)
                break
            else:
                y_instances = y_instances + 1
                print('y:', y_instances, 'z:', z_instances)
        elif x[index] == z:
            print('y:', y_instances, 'z:', z_instances)
            z_instances = z_instances + 1
            if z_instances < y_instances:
                print('y:', y_instances, 'z:', z_instances)
            elif z_instances >= y_instances:
                print('y:', y_instances, 'z:', z_instances)
                break
        else:
            pass
        index = index + 1
    return scan_first_occurrence_and_return_index(x, y), index


def simplify(x):
    # Simplifies expression using the order of B.O.D.M.A.S.                 # 22(22)22
    # REQUIRES all functions from Calculator modules
    x = substitute_constant(x)
    print(x)

    while search_for_brackets_in_element(x) == 'Yes':
        print(x)
        y, z = return_index_of_first_and_last_occurrence(x, '(', ')')
        bracket_expression = ''
        for index in range(y+1, z):
            bracket_expression = bracket_expression + x[index]
        bracket_expression = simplify(bracket_expression)
        print(x)
        rest_expression_left_part = ''
        for index in range(0, y):
            rest_expression_left_part = rest_expression_left_part + x[index]
        rest_expression_right_part = ''
        for index in range(z+1, len(x)):
            rest_expression_right_part = rest_expression_right_part + x[index]
        x = rest_expression_left_part + str(bracket_expression) + rest_expression_right_part
        print(x)
    x = split(x, '+')
    print(x)
    for element_no_x in range(0, len(x)):
        if search_for_multiply_in_element(x[element_no_x]) == 'Yes':            # 2*2/4+5
            multiply = split(x[element_no_x], '*')
            print(multiply)
            for element_no_multiply in range(0, len(multiply)):
                if search_for_div_in_element(multiply[element_no_multiply]) == 'Yes':
                    divide = split(multiply[element_no_multiply], '/')
                    divide = simplify_exponents(divide)
                    multiply[element_no_multiply] = divide_elements_in_list(divide)
                else:
                    pass
            multiply = simplify_exponents(multiply)
            x[element_no_x] = multiply_elements_in_list(multiply)
        elif search_for_div_in_element(x[element_no_x]) == 'Yes':
            divide = split(x[element_no_x], '/')
            divide = simplify_exponents(divide)
            x[element_no_x] = divide_elements_in_list(divide)
    print(x)
    x = simplify_exponents(x)
    x = add_elements_in_list(x)
    return x


def search_for_constant(x):
    for index in range(0, len(x)):
        if x[index] == 'p' and x[index + 1] == 'i':
            return 'Yes'
        elif x[index] == 'e':
            return 'Yes'
        elif x[index] == 'c':
            return 'Yes'
        elif x[index] == 'h':
            return 'Yes'
        elif x[index] == 'G':
            return 'Yes'
        if x[index] == 'N' and x[index + 1] == 'A':
            return 'Yes'
    else:
        return 'No'


def substitute_constant(x):
    while search_for_constant(x) == 'Yes':
        for index in range(0, len(x)):
            if x[index] == 'p' and x[index + 1] == 'i':
                substitute = str(math.pi)
                left_index = index - 1
                right_index = index + 2
                break
            elif x[index] == 'e':
                substitute = str(math.e)
                left_index = index - 1
                right_index = index + 1
                break
            elif x[index] == 'c':
                substitute = '299792458'
                left_index = index - 1
                right_index = index + 1
                break
            elif x[index] == 'h':
                substitute = '0.0000000000000000000000000000000006626176'
                left_index = index - 1
                right_index = index + 1
                break
            elif x[index] == 'G':
                substitute = '0.0000000000667408'
                left_index = index - 1
                right_index = index + 1
                break
            elif x[index] == 'N' and x[index + 1] == 'A':
                substitute = '602214086000000000000000'
                left_index = index - 1
                right_index = index + 2
                break
        else:
            return x
        left_part = ''
        for i in range(0, left_index + 1):
            left_part += x[i]
        right_part = ''
        for j in range(right_index, len(x)):
            right_part += x[j]
        result = left_part + substitute + right_part
        x = result
    return x


def search_for_exponents_in_element(x):
    x = str(x)
    for index in range(len(x)):
        if x[index] == '^':
            return 'Yes(^)'
        else:
            pass
    else:
        return 'No'


def simplify_exponents(x):
    for index in range(0, len(x)):
        if search_for_exponents_in_element(x[index]) == 'Yes(^)':
            y = split(x[index], '^')
            y.reverse()
            result = 1
            for element in y:
                result = float(element) ** result
            x[index] = result
        else:
            pass
    return x


def return_entry(self):
    x = entry.get()
    if x == self:
        pass
    result = simplify(x)
    Label(master, text='Result=', font=('Futura-Bold', 30), fg='Dark Green', bg='Black').grid(row=2, column=0)
    Label(master, text=result, font=('Futura-Bold', 30), fg='Dark Green', bg='Black')\
        .grid(row=2, column=1, sticky=W+E+N+S)


Label(master, text='Expression Calculator', font=('COCOGOOSE LETTERPRESS', 50),
      fg='Dark Green', bg='Black').grid(row=0, columnspan=2, sticky=W+E+N+S)
Label(master, text="Input: ", font=('Futura-Bold', 30), fg='Dark Green', bg='Black').grid(row=1, sticky=W+E+N+S)
entry = Entry(master, font=('Futura-Bold', 30), fg='Dark Green', bg='Black')
entry.grid(row=1, column=1, sticky=N+S)
entry.bind('<Return>', return_entry)

mainloop()
