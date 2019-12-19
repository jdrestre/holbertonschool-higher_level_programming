#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    new_list = [x if x != search else replace for x in my_list]
    return(new_list)

'''
    new_list = []
    for x in my_list:
        if val == search:
            new_list.append(replace)
        else:
            new_list.append(x)
    return new_list
'''
