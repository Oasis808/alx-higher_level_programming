#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to return a list with all values multiplied by a number
# without using any loops
#
# (C) 2022 Adiamah Isaiah, Kumasi, Ghana
# email isaiahadiamah20@gmail.com
# -----------------------------------------------------------


def multiply_list_map(my_list=[], number=0):
    return list(map(lambda i: number * i, my_list))
