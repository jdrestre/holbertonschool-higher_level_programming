#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for val in a_dictionary:
        new[val] = a_dictionary[val] * 2
    return new

'''
    new_dic = a_dictionary.copy()
    for k, v in new_dic.items():
        new_dic[k] = v * 2
    return(new_dic)


    return ({k: a_dictionary[k] * 2 for k in a_dictionary})
'''
