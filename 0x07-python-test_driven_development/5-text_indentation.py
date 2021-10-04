#!/usr/bin/python3
"""
    mamaaaaa
    uhhhhhuhhh
    i killed a man...
"""


def text_indentation(text):
    """ alalalala """
    if type(text) != str:
        raise TypeError("text must be a string")
        return
    txt1 = text[:]
    for i in [".", "?", ":"]:
        a = i + "\n\n"
        txt1 = txt1.replace(i, a)
    for a in txt1.split("\n"):
        print(a.lstrip())
