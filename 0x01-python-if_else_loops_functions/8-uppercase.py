#!/usr/bin/python3


def uppercase(str):
    dif = ord('A') - ord('a')
    for letter in str:
        let = letter
        if ord(let) >= ord('a') and ord(let) <= ord('z'):
            let = chr(ord(let) + dif)
        print("{}".format(let), end="")
    print()
