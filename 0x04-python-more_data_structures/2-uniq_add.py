#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to add all unique integers in a list (only once
# for each integer)
#
# (C) 2022 Adiamah Isaiah, Kumasi, Ghana
# email isaiahadiamah20@gmail.com
# -----------------------------------------------------------


def uniq_add(my_list=[]):
    my_set = set(my_list)
    sum = 0
    for number in my_set:
        sum += number
    return sum
