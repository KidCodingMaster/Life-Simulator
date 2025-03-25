"""
A small game where the player can be what ever they want
"""

from utils.get_info import get_age, get_job, get_name
from utils.jobs import UnEmployed
from utils.user import User


jobs = {"unemployed": UnEmployed}

name = get_name()
age = get_age()

job = get_job(name, age, jobs)

user = User(job)

# Main Loop
while True:
    command = input("What do you want to do (type 'help' to see commands)? ").lower()

    if command == "help":
        print("Type 'name' to change the name")
        print("Type 'age' to change the age")
        print("Type 'job' to change the job")
        print("Type 'work' to work")
    elif command == "name":
        new_name = get_name()
        job.set_name(new_name)

        print("Name set to " + new_name)
    elif command == "age":
        new_age = get_age()
        job.set_age(new_age)

        print("Age set to " + str(new_age))
    elif command == "job":
        job = get_job(name, age, jobs)

        print("Job set to " + str(job))
    elif command == "work":
        if isinstance(job, UnEmployed):
            print("You are unemployed!")
            continue
