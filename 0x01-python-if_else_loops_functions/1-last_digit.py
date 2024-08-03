#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
x = abs(number) % 10
if x < 0:
    x = -x
    print("Last digit of {} is {} and is ".format(number, x), end="")
if x > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, x))
elif x == 0:
    print("Last digit of {} is {} and is 0".format(number, x))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, x))
