"""
Module for the class User for the Life Simulator
"""


class User:
    """
    Class for user in the Life Simulator
    """

    def __init__(self, job):
        self.name = job.name
        self.age = job.age
        self.money = 0

        self.job = job

    def set_name(self, new_name):
        """
        Function to set the name of the user
        """

        self.name = new_name

        self.job.set_name(new_name)

    def set_age(self, new_age):
        """
        Function to set the age of the user
        """

        self.age = new_age

        self.job.set_age(new_age)
