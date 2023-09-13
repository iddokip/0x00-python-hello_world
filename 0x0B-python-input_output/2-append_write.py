#!/usr/bin/python3
"""Contains the function append_write(...)"""


def append_write(filename="", text=""):
    """appends and returns the number of characters added"""
    with open(filename, "a", encoding="utf-8") as f:
        c = f.write(text)
    return c
