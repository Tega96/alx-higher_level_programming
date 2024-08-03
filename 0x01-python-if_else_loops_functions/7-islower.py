#!/usr/bin/python3
# 7-islower.py
# Otite Otega <Tega96@github.com>

"""This code checks if an alphabet is lower case"""
def islower(c):
    """check for lower character"""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
