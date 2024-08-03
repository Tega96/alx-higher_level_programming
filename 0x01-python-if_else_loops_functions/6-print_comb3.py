#!/usr/bin/python3
# 6-print_comb3.py
# Otite Otega <Tega96@gihub.com>

"""Print all possible different combination of two digits in ascnding order
The two digits must be different - 01 and 10 are considered identical
"""
for number1 in range(0, 10):
    for number2 in range(number1 + 1, 10):
        if number1 == 8 and number2 == 9:
            print("{}{}".format(number1, number2))
        else:
            print("{}{}".format(number1, number2), end=", ")
