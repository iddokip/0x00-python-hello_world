#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    number_keys = list(a_dictionary.keys())

    for i in number_keys:
        num += 1

    return (num)
