#!/usr/bin/python3
import sys
if __name__ == "__main__" and sys.argv:
    args = sys.argv[1:]
    arguments = len(args)
    word = "argument"
    if arguments != 1:
        word += "s"
    print("{} {}{}".format(arguments, word, ":" if arguments else "."))
    for indx in range(len(args)):
        print("{}: {}".format(indx + 1, args[indx]))