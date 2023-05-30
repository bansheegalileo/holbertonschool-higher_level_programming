#!/usr/bin/python3
"""
    student class that defines a student
"""


class Student():
    """
        student class
    """
    def __init__(self, first_name, last_name, age):
        """
            INIT
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            returns description for Student
        """
        return(self.__dict__)
