#!/usr/bin/python3
def roman_to_int(roman_string):
        if isinstance(roman_string, str):
                return None
        out = 0
        lis = []
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in roman_string:
                lis.append(val[i])
        rm = []
        for i in range(len(lis)):
                if lis[i] > lis[i - 1 if i > 0 else 0]:
                        lis[i] = lis[i] - lis[i-1]
                        rm.append(i - 1)
        for i in range(len(rm)):
                del lis[rm[i] - i]
        return sum(lis)
