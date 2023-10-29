import json
from datetime import datetime
from typing import Optional

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
            print(underConstructionMessage())  # haven't gotten there yet
        elif userInput == "5":
            print(underConstructionMessage())  # haven't gotten there yet
        elif userInput.upper() == "X":
            break
        else:
            print(invalidInput("1, 2, or X"))
            print(anyButtonToContinueMessage())
            input("")

    return currentUser


def jobSearch(currentUser: Optional[User] = None) -> Optional[User]:
    clearScreen()
    jobs = loadJobs()
    totalJobs = len(jobs)
    i = 0
    # Printing all current positions
    print("Current Open Positions:")
    for i in range(0, totalJobs):
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


def applyToJob(jobIndex, currentUser):
    jobs = loadJobs()
    applicationNum = len(jobs[jobIndex]["applicants"])
    flag = False
    # checking to see if currentUser has already applied
    for i in range(0, applicationNum):
        if jobs[jobIndex]["applicants"][i]["username"] == currentUser.username:
            flag = True
        else:
            i += 1
    # If user is not logged in
    if not isinstance(currentUser, User):
        print("You must be logged in to create a Job.")
        print(anyButtonToContinueMessage())
        input("")
        return currentUser
    # If user created the job posting
    elif (
        jobs[jobIndex]["firstname"] == currentUser.firstname
        and jobs[jobIndex]["lastname"] == currentUser.lastname
    ):
        print("You cannot apply for a job you posted.")
        print(anyButtonToContinueMessage())
        input("")
        return currentUser
    elif flag == True:
        print("You cannot apply for a job you have already applied to.")
        print(anyButtonToContinueMessage())
        input("")
        return currentUser
    else:
        clearScreen()
        while True:
            print("*** Job Application ***")
            gradDate = input("Enter graduation date in the form mm/dd/yyy: ")
            if checkDate(gradDate) == False:
                print("Invalid input please try again")
                print(anyButtonToContinueMessage())
                input("")
                break
            startDate = input("Enter your desired start date in the form mm/dd/yyy: ")
            if checkDate(startDate) == False:
                print("Invalid input please try again")
                print(anyButtonToContinueMessage())
                input("")
                break
            explanation = input("Explain why you would be a good fit for this position: ")

            jobs[jobIndex]["applicants"] = [
                {
                    "username": currentUser.username,
                    "graduation": gradDate,
                    "start": startDate,
                    "reason": explanation,
                }
            ]
            saveJobDatabase(JSON_JOBS_FP, jobs)
            print("Application sucessfully submitted")
            print(anyButtonToContinueMessage())
            input("")
            break

    return currentUser


def checkDate(input_string):
    try:
        datetime.strptime(input_string, "%m/%d/%Y")
        return True
    except ValueError:
        return False


def userSaveJob(jobIndex, currentUser):
    print("SAVE")
    return currentUser
