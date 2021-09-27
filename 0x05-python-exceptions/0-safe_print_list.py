#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        for li in range(x):
            print("{}".format(my_list[li]), end="")
            num += 1
    except:
        pass
    print()
    return num
