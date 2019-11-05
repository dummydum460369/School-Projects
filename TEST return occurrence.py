
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


ll = input()
print(return_index_of_first_and_last_occurrence(ll, '(', ')'))
