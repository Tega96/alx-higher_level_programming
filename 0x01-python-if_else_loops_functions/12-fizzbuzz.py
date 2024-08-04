#!/usr/bin/python3
# 12-fizzbuzz.py
# Otega Otite <Tega96@github.com

def fizzbuzz():
    """print fizz for multiples of 3, buzz for multiples of 5 and fizzbuzz for multiples of 3 and 5 on range of numbers 0 - 100"""
    for x in range(0, 101):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 5 == 0:
            print("Buzz")
        elif x % 3 == 0:
            print("Fizz")
        else:
            print("{}".format(x), end=" ")
