#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    len1 = len(list_a)
    len2 = len(list_b)
    while len1 < 2:
        list_a.append(0)
        len1 += 1
    while len2 < 2:
        list_b.append(0)
        len2 += 1
    x = list_a[0] + list_b[0]
    y = list_a[1] + list_b[1]
    return(x, y)
