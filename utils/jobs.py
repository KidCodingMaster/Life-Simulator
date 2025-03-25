"""
Module for jobs for the Life Simulator game
"""

from abc import ABC
import random
from time import sleep


class Job(ABC):
    """
    Base Class for Jobs
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.salary = 0

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

    def work(self, time):
        """
        Method for the user to work for 'time' seconds
        """


# UnEmployed Person
class UnEmployed(Job):
    """
    Job for unemployed people
    """


class Engineer(Job):
    """
    Job for engineers
    """

    def __init__(self, name, age):
        super().__init__(name, age)

        self.salary = random.randint(20000, 30000)

    def work(self, time):
        sleep(time)

        return self.salary / (time * 5)
