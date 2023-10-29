import json
from datetime import datetime
from typing import Optional
from pages.application import applyToJob, personalApplicationList, notAppliedList

from common_utils.messages import (
    anyButtonToContinueMessage,
    invalidInput,
    returnToPreviousMenuMessage,
    underConstructionMessage,
)
from common_utils.types.jobs import createJob, saveJob, saveJobDatabase
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from common_utils.utils import JSON_JOBS_FP, clearScreen, loadJobs, printOptionList

jobOptionsList = [
    "*** Job Search ***",
    "1 - Search for Job/Internship",
    "2 - Post Job/Internship",
    "3 - View Saved Jobs",
    "4 - View Applications",
    "5 - View Open Jobs without Applications",
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
        elif userInput == "3":
            print(underConstructionMessage())  # haven't gotten there yet
        elif userInput == "4":
            clearScreen()
            print("*** Application List ***")
            applications = personalApplicationList(currentUser)
            for i in range(0, len(applications)):
                print(applications[i])
            print(anyButtonToContinueMessage())
            input("")
        elif userInput == "5":
            clearScreen()
            print("*** List of Jobs Not Applied To ***")
            notApplied = notAppliedList(currentUser)
            for i in range(0, len(notApplied)):
                print(notApplied[i])
            print(anyButtonToContinueMessage())
            input("")  # haven't gotten there yet
        elif userInput.upper() == "X":
            break
        else:
            print(invalidInput("Please select a valid option"))
            print(anyButtonToContinueMessage())
            input("")

    return currentUser



def jobSearch(currentUser: Optional[User] = None) -> Optional[User]:
    clearScreen()
    jobs = loadJobs()
    totalJobs = len(jobs)
    # Printing all current positions
    print("Current Open Positions:")
    
    # Determining if currentUser already applied to job and printing out job list
    for i in range(0, totalJobs):
        flag = False
        applicationNum = len(jobs[i]["applicants"])
        for j in range(0, applicationNum):
            if jobs[i]["applicants"][j]["username"] == currentUser.username:
                print(i + 1, "-", jobs[i]["title"], "** Applied **")
                flag = True
            j += 1
        if (flag == False):
            print(i + 1, "-", jobs[i]["title"])
        i += 1
    returnToPreviousMenuMessage()

    print("Input a number for more details")
    # Printing details of jobs by request
    while True:
        userInput = input("")
        if userInput.upper() == "X":
            break
        temp = int(userInput)
        if temp in range(1, totalJobs + 1):
            clearScreen()
            print(
                "Title: ",
                jobs[temp - 1]["title"],
                "\nDescription: ",
                jobs[temp - 1]["description"],
                "\nEmployer: ",
                jobs[temp - 1]["employer"],
                "\nLocation: ",
                jobs[temp - 1]["location"],
                "\nSalary: ",
                jobs[temp - 1]["salary"],
                "\n",
            )
            print(anyButtonToContinueMessage())
            input("")

            printJobOptionScreen(temp - 1, currentUser)
            break
        else:
            print(invalidInput("Please choose a valid option"))
            print(anyButtonToContinueMessage())
            input("")

    return currentUser


jobListingChoices = [
    "*** Job Options ***",
    "1 - Apply for Job",
    "2 - Save Job",
    returnToPreviousMenuMessage(),
]


def printJobOptionScreen(jobIndex, currentUser: Optional[User] = None) -> Optional[User]:
    while True:
        clearScreen()
        printOptionList(jobListingChoices)
        userInput = input("")

        if userInput == "1":
            currentUser = applyToJob(jobIndex, currentUser)
        elif userInput == "2":
            currentUser = userSaveJob(jobIndex, currentUser)
        elif userInput.upper() == "X":
            break
        else:
            print(invalidInput("1, 2, or X"))
            print(anyButtonToContinueMessage())
            input("")

    return


def userSaveJob(jobIndex, currentUser):
    print("SAVE")
    return currentUser
