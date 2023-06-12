#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    max_len = max(len_a, len_b)
    paddedA = tuple_a + (0,) * (max_len - len_a)
    paddedB = tuple_b + (0,) * (max_len - len_b)
    result = tuple(paddedA[i] + paddedB[i] for i in range(len(paddedA)))
    return result
