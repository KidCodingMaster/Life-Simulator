"""
Module to get info about the user
"""


def get_name():
    """
    Function to get the name of the user
    """

    name = input("What is your name? ")

    if not name:
        print("Please enter a valid name!")
        return get_name()

    return name


def get_age():
    """
    Function to get the age of the user
    """

    try:
        age = int(input("What is your age? "))
    except ValueError:
        print("Please Enter a numerical value. Please try again")
        return get_age()

    if age < 18:
        exit("You need to be at least 18 years old to have a job!")

    return age


def get_job(name, age, jobs):
    """
    Function to get the job of the user
    """

    job = input("What job do you want (type help to see all job)? ").lower()

    if job == "help":
        for job_name in jobs:
            print("You can become a " + job_name)

        return get_job(name, age, jobs)
    elif (job_class := jobs.get(job)) is not None:
        return job_class(name, age)
    else:
        print("Job not found, please try again")
        return get_job(name, age, jobs)
