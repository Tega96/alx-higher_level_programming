#!/usr/bin/python3
# 8-uppercase.py
# Otite Otega <Tega96@github.com>

"""Prints a string in uppercase followed by a new line"""
def uppercase(str):
    for s in str:
        tmp = ord(s)
        if tmp >= 97 and tmp <= 122:
            pr = chr(tmp -32)
        else:
            pr = s
        print('{}'.format(pr), end="")
    print()
