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
    li = txt1.split("\n")
    for a in range(len(li)):
        print(li[a].lstrip(), end="\n" if a + 1< len(li) else "")
