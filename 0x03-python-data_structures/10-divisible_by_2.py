#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None or len(my_list) is 0:
        return(None)
    table_tr = []
    for i in my_list:
        if 1 % 2:
            table_tr.append(False)
        else:
            table_tr.append(True)
    return(table_tr)
