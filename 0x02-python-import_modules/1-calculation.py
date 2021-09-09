#!/usr/bin/python3
import calculator_1 as calc
a = 10
b = 5
if __name__ == "__main__":
    print("{} + {} = {}".(a, b, calc.add(a, b)))
    print("{} - {} = {}".(a, b, calc.sub(a, b)))
    print("{} * {} = {}".(a, b, calc.mul(a, b)))
    print("{} / {} = {}".(a, b, calc.div(a, b)))
