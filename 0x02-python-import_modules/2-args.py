#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    arguments = len(args)
    print("{} argument{}{}".format(arguments, "s" if arguments != 1 else "", ":" if arguments else "."))
    for indx in range(len(args)):
        print("{}: {}".format(indx, args[indx]))
