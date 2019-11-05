from tkinter import *
master = Tk()
master.configure(bg='Black')


def return_entry(en):

    x = entry.get()
    x = [str(x) for x in x.split(sep='+')]
    product = 1
    division = 1
    divide = [1]
    presence_of_multiply = 'No'
    Result = 0
    presence_of_divide = 'No'
    for element_no in range(0, len(x)):  # Product initiate
        element = x[element_no]
        for letter in element:
            if letter == '*':
                multiply = element.split(sep='*')
                presence_of_multiply = 'Yes'
                for search_div_element_no in range(0, len(multiply)):  # divide initiate
                    search_div_element = multiply[search_div_element_no]
                    for search_div_letter in search_div_element:
                        if search_div_letter == '/':
                            divide = search_div_element.split(sep='/')
                            presence_of_divide = 'Yes'
                            division = float(divide[0])
                    if presence_of_divide == 'Yes':
                        for h in range(1, len(divide)):
                            division = division / float(divide[h])
                        multiply[search_div_element_no] = division
                        division = 1
                        divide = [1]
                        presence_of_divide = 'No'
                for y in multiply:
                    product = product * float(y)
                break
            if letter == '/':  # divide initiate
                divide = element.split(sep='/')
                presence_of_divide = 'Yes'
                division = divide[0]
                for i in range(1, len(divide)):
                    divisor = divide[i]
                    division = float(division) / float(divisor)
            else:
                pass
        if presence_of_multiply == 'Yes':
            x[element_no] = product
            product = 1
            presence_of_multiply = 'No'
        elif presence_of_divide == 'Yes':
            x[element_no] = division
            division = 1
            divide = [1]
            presence_of_divide = 'No'
        else:
            pass
    print('=Sum of', x)
    for num in x:
        z = float(num)
        Result = Result + z
    print('=', Result)
    Label(master, text='Result=', font=('Futura-Bold', 30), fg='Dark Green', bg='Black').grid(row=2, column=0)
    Label(master, text=Result, font=('Futura-Bold', 30), fg='Dark Green', bg='Black').grid(row=2, column=1)


Label(master, text='Expression Calculator', font=('Futura', 50), fg='Dark Green', bg='Black').grid(row=0, columnspan=2,
                                                                                                   sticky=W+E+N+S)
Label(master, text="Input: ", font=('Futura-Bold', 30), fg='Dark Green', bg='Black').grid(row=1, sticky=W+E+N+S)

entry = Entry(master, font=('Futura-Bold', 30), fg='Dark Green', bg='Black')
entry.grid(row=1, column=1)

# Connect the entry with the return button
entry.bind('<Return>', return_entry)

mainloop()
