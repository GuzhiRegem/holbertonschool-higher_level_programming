#!/usr/bin/python3
safe_print_list(my_list=[], x=0):
    num = 0
    try:
        for li in range(x):
            print("{}".format(my_list[li]))
            num += 1
    return (num)
