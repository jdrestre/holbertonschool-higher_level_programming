#!/usr/bin/python3
''' Class Square '''


class Square:
    '''Represent Square'''

    def __init__(self, size=0):
        '''Initializes the data with error handling'''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
