#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to convert a Roman numeral to an integer
#
# (C) 2024 Adiamah Isaiah, Accra, Ghana
# email isaiahadiamah20@gmail.com
# -----------------------------------------------------------

def roman_to_int(roman_string):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    p = 0

    if type(roman_string) is str and roman_string:
        for c in range(len(roman_string) - 1, -1, -1):
            if val[roman_string[c]] >= p:
                res += val[roman_string[c]]
            else:
                res -= val[roman_string[c]]
            p = val[roman_string[c]]
    return res
