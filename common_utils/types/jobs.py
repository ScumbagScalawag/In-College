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

    if len(jobs) < MAXJOBS:  # Requirement for 10 job postings
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

def removeJob(currentUser: Optional[User] = None) -> Optional[User]:
    # Must be logged in to delete job
    jobs = loadJobs()
    # If user is not logged in
    if not isinstance(currentUser, User):
        print("You must be logged in to create a Job.")
        print(anyButtonToContinueMessage())
        input("")
        return currentUser
    
    #TODO Get the job index
    jobIndex = 0

    # If user created the job posting
    if (
        jobs[jobIndex]["firstname"] == currentUser.firstname
        and jobs[jobIndex]["lastname"] == currentUser.lastname
    ):
        print("Job Removed")
        job = jobs[jobIndex]
        #TODO Notifiy Applicants
        for people in job["applicants"]:
            #TODO Notify people
            pass
        jobs.remove(job)
        #jobs.pop(jobIndex)
        saveJobDatabase(JSON_JOBS_FP, jobs)
        print(anyButtonToContinueMessage())
        input("")
        return currentUser
    else:
        print("You cannot remove a job posting that you did not create")
        print(anyButtonToContinueMessage())
        input("")
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
    }

    jobs.append(newJob)
    saveJobDatabase(JSON_JOBS_FP, jobs)
    return


def saveJobDatabase(jsonFilePath, jobs):
    jobDB = {"joblist": jobs}
    with open(jsonFilePath, "w") as outfile:
        json.dump(jobDB, outfile, indent=4)
    return
