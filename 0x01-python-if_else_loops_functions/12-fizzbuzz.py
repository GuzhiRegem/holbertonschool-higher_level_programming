#!/usr/bin/python3


def fizzbuzz():
    for num in range(100):
        num += 1
        out = ""
        if (num % 3) == 0:
            out += "Fizz"
        if (num % 5) == 0:
            out += "Buzz"
        if out == "":
            out = str(num)
        print("{} ".format(out), end="")
