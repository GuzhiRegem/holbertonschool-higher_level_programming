#!/usr/bin/python3
import dis
MagicClass = __import__('103-magic_class').MagicClass
mc = MagicClass(10) 
print("{:.2f}".format(mc.circumference()))
print("{:.2f}".format(mc.area()))
