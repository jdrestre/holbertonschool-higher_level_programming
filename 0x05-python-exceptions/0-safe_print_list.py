#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        len = 0
        for i in my_list:
            len += 1
        if x > len:
            x = len
        count = 0
        i = 0
        while (i < x):
            print("{}".format(my_list[i]), end='')
            count += 1
            i += 1
        print()
        return count
    except:
        print()
        return count
