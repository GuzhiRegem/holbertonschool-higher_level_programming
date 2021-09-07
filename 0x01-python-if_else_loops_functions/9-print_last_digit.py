#!/usr/bin/python3


def print_last_digit(number):
    num = number
    if number < 0:
        num = number * -1
    num = num % 10
    print(num)
    return num
