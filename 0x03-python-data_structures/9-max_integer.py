#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    lenn = len(my_list)
    for i in range(lenn):
        if my_list[i] > my_list[i + 1]:
            return my_list[i]
