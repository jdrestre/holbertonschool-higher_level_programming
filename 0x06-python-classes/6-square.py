#!/usr/bin/python3
'''class Square'''


class Square:
    '''Represents a Square with size and a coordinate position'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initializes the data with error handling.'''
        self.size = size
        self.position = position

    def area(self):
        '''Returns the current square area.'''
        return (self.__size * self.__size)

    @property
    def position(self):
        '''Returns the current square's position'''
        return self.__position

    @property
    def size(self):
        '''Returns size of Square instance'''
        return self.__size

    @position.setter
    def position(self, value):
        '''Sets position attribute'''
        if len(value) < 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[0], int) or value[0] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[1], int) or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    @size.setter
    def size(self, value):
        '''Sets size attribute'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        '''Prints stdout square with character #'''
        if self.__size > 0:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for blanks in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
