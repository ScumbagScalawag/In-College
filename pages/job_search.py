import json
from typing import Optional

from common_utils.messages import (
    anyButtonToContinueMessage,
    invalidInput,
    returnToPreviousMenuMessage,
    underConstructionMessage,
)
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from common_utils.utils import JSON_JOBS_FP, clearScreen, loadJobs, printOptionList

MAXJOBS = 10


def saveJob(jobs, title, description, employer, location, salary, firstname, lastname):
    newJob = {
        "title": title,
        "description": description,
        "employer": employer,
        "location": location,
        "salary": salary,
        "firstname": firstname,
        "lastname": lastname,
    }

    jobs.append(newJob)
    saveJobDatabase(JSON_JOBS_FP, jobs)
    return


def saveJobDatabase(jsonFilePath, jobs):
    jobDB = {"joblist": jobs}
    with open(jsonFilePath, "w") as outfile:
        json.dump(jobDB, outfile, indent=4)

    return


jobOptionsList = [
    "*** Job Search ***",
    "1 - Search for Job/Internship",
    "2 - Post Job/Internship",
    returnToPreviousMenuMessage(),
]


# TODO check currentUser is not none
# user selected to do a job search
def printJobSearchScreen(currentUser: Optional[User] = None) -> Optional[User]:
    while True:
        clearScreen()
        printOptionList(jobOptionsList)
        userInput = input("")

        if userInput == "1":
            currentUser = jobSearch(currentUser)
        elif userInput == "2":
            currentUser = createJob(currentUser)
        elif userInput.upper() == "X":
            break
        else:
            print(invalidInput("1, 2, or X"))
            print(anyButtonToContinueMessage())
            input("")

    return currentUser


def jobSearch(currentUser: Optional[User] = None) -> Optional[User]:
    # under construction, not needed in EPIC2
    clearScreen()
    print("*** Job Search ***")
    currentPositions()
    # print(anyButtonToContinueMessage())
    # input("")
    return currentUser


# TODO check validity of inputs
def createJob(currentUser: Optional[User] = None) -> Optional[User]:
    # Must be logged in to create job
    if not isinstance(currentUser, User):
        print("You must be logged in to create a Job.")
        print(anyButtonToContinueMessage())
        input("")
        return currentUser

    jobs = loadJobs()
    print(jobs)
    # users = loadUsers()
    userDB = UserDatabase([])
    userDB.loadUsers()

    if len(jobs) < MAXJOBS:  # Requirement for 5 job postings
        while True:
            clearScreen()
            print("*** Create a new job posting ***")
            title = input("Job Title: ")
            description = input("Brief Description of the Job: ")
            employer = input("Employer: ")
            location = input("Location: ")
            salary = input("Salary: ")

            try:
                saveJob(
                    jobs,
                    title,
                    description,
                    employer,
                    location,
                    salary,
                    currentUser.firstname,
                    currentUser.lastname,
                )
            except:
                print("Error: There was an error saving the job. Please try again")
                pass
            # clearScreen()  # TODO I don't think this is needed

            print("\nJob Created!")
            break
    else:
        print(
            "All permitted jobs have been posted, please try again later"
        )  # Requirement for 5 accounts response
    print(anyButtonToContinueMessage())
    input("")
    return currentUser


def currentPositions():
    jobs = loadJobs()
    totalJobs = len(jobs)
    i = 0
    print("Current Open Positions:")
    print("Please input a number for more details or choose the last option to return")
    for i in range(0, totalJobs):
        print(i + 1, "-", jobs[i]["title"])
        i += 1
    print(i + 1, "-", "Return to Previous Menu")

    while True:
        userInput = input("")
        if userInput == userInput.upper() == "X":
            break
        temp = int(userInput)
        if temp in range(0, totalJobs + 1):
            print(
                "Title: ",
                jobs[temp]["title"],
                "\nDescription: ",
                jobs[temp]["description"],
                "\nEmployer: ",
                jobs[temp]["employer"],
                "\nLocation: ",
                jobs[temp]["location"],
                "\nSalary: ",
                jobs[temp]["salary"],
            )
            print(anyButtonToContinueMessage())
            input("")
            break
        elif temp == totalJobs + 1:
            break
        else:
            print(invalidInput("Please choose a valid option"))
            print(anyButtonToContinueMessage())
            input("")

    return
