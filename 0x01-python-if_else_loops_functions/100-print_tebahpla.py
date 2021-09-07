#!/usr/bin/python3
dif = ord('A') - ord('a')
for letter in range(ord('a'), ord('z') + 1):
    inv = ord('z') + ord('a') - letter
    out = chr(inv)
    if (letter % 2 == 0):
        out = chr(inv + dif)
    print("{}".format(out), end='')
