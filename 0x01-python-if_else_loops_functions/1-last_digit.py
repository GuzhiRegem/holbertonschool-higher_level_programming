#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    digit = number % 10
else:
    digit = ((number * -1) % 10) * -1
sig = "0"
if digit != 0:
    sig = "less than 6 and not 0"
    if digit > 5:
        sig = "greater than 5"
print("Last digit of {:d} is {:d} and is {}".format(number, digit, sig))
