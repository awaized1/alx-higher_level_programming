#!/usr/bin/python3
"""Code defines class Student."""


class Student:
    """Class reps a student."""

    def __init__(self, first_name, last_name, age):
        """Function initialize new Student.

        Args:
            first_name (str): First name of student.
            last_name (str): Student last name.
            age (int): Age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function gets dictionary representation of Student.

        If attrs is list of strings, reps only those attributes
        in the list.

        Args:
            attrs (list): The attributes to be represented.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
