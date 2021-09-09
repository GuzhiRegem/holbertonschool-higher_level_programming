#!/usr/bin/python3
import sys
if __name__ == "__main__" and sys.argv:
    args = sys.argv
    arguments = len(args) - 1
    word = "argument"
    if arguments != 1:
        word += "s"
    print("{} {}{}".format(arguments, word, ":" if arguments else "."))
    indx = 1
    while indx <= arguments:
        print("{}: {}".format(indx, args[indx]))
        indx += 1
