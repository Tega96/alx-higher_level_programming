#!/usr/bin/python3
# 12-fizzbuzz.py
# Otega Otite <Tega96@github.com

def fizzbuzz():
    """print fizz for multiples of 3, buzz for multiples of 5 and fizzbuzz for multiples of 3 and 5 on range of numbers 0 - 100"""
    for x in range(1, 101):
        if x % (3 * 5) == 0:
            print('FizzBuzz ')
        elif x % 3 == 0:
            print('Fizz ')
        elif x % 5 == 0:
            print('buzz ')
        else:
            print('{} '.format(x), end="")
