#!/usr/bin/python3
def no_c(my_string):
    test_string = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            test_string += i
    return(test_string)
