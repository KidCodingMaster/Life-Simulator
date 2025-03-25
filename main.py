"""
A small game where the player can be what ever they want
"""

import sys
from utils.get_info import get_age, get_job, get_name
from utils.jobs import UnEmployed, Engineer
from utils.user import User


jobs = {"unemployed": UnEmployed, "engineer": Engineer}

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
        print("Type 'money' to see how much money you have")
        print("Type 'exit' to exit")
    elif command == "name":
        new_name = get_name()
        user.set_name(new_name)

        print("Name set to " + new_name)
    elif command == "age":
        new_age = get_age()
        user.set_age(new_age)

        print("Age set to " + str(new_age))
    elif command == "job":
        job = get_job(user.name, user.age, jobs)
        user.set_job(job)

        print("Job set to " + str(job))
    elif command == "work":
        if isinstance(job, UnEmployed):
            print("You are unemployed!")
            continue

        try:
            time = int(input("How long do you want to work for? "))
        except ValueError:
            print("Please enter a numerical value")
            continue

        user.work(user.job.work(time))
    elif command == "money":
        print(f"You have ${user.money} money")
    elif command == "exit":
        print("Thanks for playing Life Simulator!")
        sys.exit()
