#!/usr/bin/python3
import random
number = random.randint(-10, 10)
sig = "zero"
if number > 0:
    sig = "positive"
if number < 0:
    sig = "negative"
print("{:d} is {}".format(number, sig))
