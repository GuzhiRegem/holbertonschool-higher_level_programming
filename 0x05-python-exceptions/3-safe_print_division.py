#!/usr/bin/python3
def safe_print_division(a, b):
    num = 0
    try:
        num = a / b
    except:
        num = None
    finally:
        print("Inside result: {}".format(num))
    return num
