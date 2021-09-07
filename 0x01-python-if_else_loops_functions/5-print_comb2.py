#!/usr/bin/python3
for number in range(100):
    sep = '\n'
    if (number < 99):
        sep = ", "
    print("{}{}".format(number, sep), end="")
