import json
from datetime import datetime
from typing import Optional

from common_utils.messages import (
    anyButtonToContinueMessage,
    invalidInputPressToContinue,
    returnToPreviousMenuMessage,
    underConstructionMessage,
)
from common_utils.types.jobs import createJob, saveJob, saveJobDatabase  # saveJob is not used
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from common_utils.types.job_database import JobDatabase
from common_utils.utils import (
    JSON_JOBS_FP,
    clearScreen,
    loadJobs,
    notLoggedIn,
    printOptionList,
)


def applyToJob(jobIndex, currentUser):
    # jobs = loadJobs() # Delete me
    jobDB = JobDatabase()
    jobDB.loadJobs()
    jobs = jobDB.joblist
    applicationNum = len(jobs[jobIndex]["applicants"])
    flag = False
    # If user is not logged in
    if not isinstance(currentUser, User):
        print("You must be logged in to create a Job.")
        print(anyButtonToContinueMessage())
        input("")
        return currentUser

        # checking to see if currentUser has already applied
    for i in range(0, applicationNum):
        if jobs[jobIndex]["applicants"][i]["username"] == currentUser.username:
            flag = True
        else:
            i += 1

    # If user created the job posting
    if (
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
                invalidInputPressToContinue("in the valid date format")
                break
            startDate = input("Enter your desired start date in the form mm/dd/yyy: ")
            if checkDate(startDate) == False:
                invalidInputPressToContinue("in the valid date format")
                break
            explanation = input("Explain why you would be a good fit for this position: ")
            jobs[jobIndex]["applicants"].append(
                {
                    "username": currentUser.username,
                    "graduation": gradDate,
                    "start": startDate,
                    "reason": explanation,
                }
            )
            jobDB.saveDatabase()
            # saveJobDatabase(JSON_JOBS_FP, jobs)
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


def personalApplicationList(currentUser):
    applications = []
    jobDB = JobDatabase()
    jobDB.loadJobs()
    jobs = jobDB.joblist
    # jobs = loadJobs() #Delete me
    totalJobs = len(jobs)
    # checking to see if currentUser is logged in
    if notLoggedIn(currentUser):
        return applications

    # creating a list of all applied jobs
    for i in range(0, totalJobs):
        applicationNum = len(jobs[i]["applicants"])
        for j in range(0, applicationNum):
            if jobs[i]["applicants"][j]["username"] == currentUser.username:
                applications.append(jobs[i]["title"])
            j += 1
        i += 1
    return applications


def notAppliedList(currentUser):
    applications = []
    jobDB = JobDatabase()
    jobDB.loadJobs()
    jobs = jobDB.joblist
    # jobs = loadJobs() #Delete me
    totalJobs = len(jobs)
    # checking to see if currentUser is logged in
    if notLoggedIn(currentUser):
        return applications

    # creating a list of all jobs not applied to
    for i in range(0, totalJobs):
        flag = False
        applicationNum = len(jobs[i]["applicants"])
        for j in range(0, applicationNum):
            if jobs[i]["applicants"][j]["username"] == currentUser.username:
                flag = True
            j += 1
        if flag == False:
            applications.append(jobs[i]["title"])
        i += 1
    return applications
