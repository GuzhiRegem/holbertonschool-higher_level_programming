#!/usr/bin/python3
for dec in range(10):
    for uni in range(dec, 10):
        sep = "\n"
        if dec < 8:
            sep = ", "
        if uni != dec:
            print("{}{}{}".format(dec, uni, sep), end="")
