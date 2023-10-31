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
from common_utils.utils import (
    JSON_JOBS_FP,
    clearScreen,
    loadJobs,
    notLoggedIn,
    printOptionList,
)

MAXJOBS = 10


# TODO check validity of inputs
def createJob(currentUser):
    clearScreen()
    print("*** Post a Job/Internship ***")
    # Must be logged in to create job
    if notLoggedIn(currentUser) == True:
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


def deleteJob(currentUser):
    jobs = loadJobs()
    # Print jobs that have same first name and last name as current user
    for i in range(0, len(jobs)):
        if (
            jobs[i]["firstname"] == currentUser.firstname
            and jobs[i]["lastname"] == currentUser.lastname
        ):
            # Select the job that matches the index
            print("Title: " + jobs[i]["title"])
            print("Description: " + jobs[i]["description"])
            print("-------------------------")
    # Get user input for which job to delete
    jobToDelete = input("Which job would you like to delete? ")
    # Check if the job exists
    for i in range(0, len(jobs)):
        if jobs[i]["title"] == jobToDelete:
            # Check if the current user is the poster of the job
            if (
                jobs[i]["firstname"] == currentUser.firstname
                and jobs[i]["lastname"] == currentUser.lastname
            ):
                # Notify applicants that the job has been deleted
                for j in range(0, len(jobs[i]["applicants"])):
                    # TODO Notify the applicant
                    jobs[i]["applicants"][j]["username"]

                # Remove the job
                del jobs[i]
                print("Job deleted successfully")
                break
            else:
                print("You are not the poster of this job.")
                return currentUser
        else:
            print("Job does not exist")
            return currentUser

    # Save the job database
    saveJobDatabase(JSON_JOBS_FP, jobs)

    return currentUser


def saveJob(jobs, title, description, employer, location, salary, firstname, lastname):
    newJob = {
        "title": title,
        "description": description,
        "employer": employer,
        "location": location,
        "salary": salary,
        "firstname": firstname,
        "lastname": lastname,
        "applicants": [],
        "saved": [],
    }

    jobs.append(newJob)
    saveJobDatabase(JSON_JOBS_FP, jobs)
    return


def saveJobDatabase(jsonFilePath, jobs):
    jobDB = {"joblist": jobs}
    with open(jsonFilePath, "w") as outfile:
        json.dump(jobDB, outfile, indent=4)
    return
