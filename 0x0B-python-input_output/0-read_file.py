#!/usr/bin/python3
""" contains read_file(...) finction """

def read_file(filename=""):
    """reads a text file (UTF-8) and print it to stdout"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line.rstrip())
