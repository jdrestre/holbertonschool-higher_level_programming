#!/usr/bin/python3


def print_last_digit(number):
    if number < 0:
        number = abs(number)
    print('{}'.format(number % 10), end='')
    return number % 10
