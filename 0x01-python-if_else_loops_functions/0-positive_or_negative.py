#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number < 0:
    print("{} is negetive".format(number))
elif number == 0:
    print("{} is zero".format(number))
else:
    print("{} is positive".format(number))
