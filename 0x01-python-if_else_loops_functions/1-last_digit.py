#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_number = number % 10
else:
    last_number = number % -10
print('Last digit of {:d} is {:d} and is'.format(number, last_number), end=' ')
if last_number > 5:
    print('greater than 5')
elif last_number == 0:
    print('0')
else:
    print('less than 6 and not 0')
