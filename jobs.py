"""
Module for jobs for the Life Simulator game
"""

from abc import ABC


class Job(ABC):
    """
    Base Class for Jobs
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, new_name):
        """
        Function to set the name of the user
        """
        self.name = new_name

    def set_age(self, new_age):
        """
        Function to set the age of the user
        """

        self.age = new_age

    def __str__(self):
        return self.__class__.__name__


# UnEmployed Person
class UnEmployed(Job):
    """
    Job for unemployed people
    """
