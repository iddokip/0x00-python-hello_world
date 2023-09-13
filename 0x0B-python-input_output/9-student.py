#!/usr/bin/python3
"""Contains a Student class"""


class Student:
    """defines a student object"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary repres """
        return self.__dict__
