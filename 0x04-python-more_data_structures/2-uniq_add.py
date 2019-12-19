#!/usr/bin/python3
def uniq_add(my_list=[]):
    setlist = set(my_list)
    x = 0
    for i in setlist:
        x += i
    return x

'''
    new_list = my_list[:]
    for i range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return (new_list)
'''
