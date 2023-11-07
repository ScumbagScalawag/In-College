import json
from datetime import datetime
from typing import Optional
from common_utils.types.exceptions import MaximumNumberOfJobs
from common_utils.messages import (
    anyButtonToContinueMessage,
    invalidInput,
    returnToPreviousMenuMessage,
    underConstructionMessage,
)
from common_utils.types.job import Job
from common_utils.types.job_database import JobDatabase
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from common_utils.utils import (
    JSON_JOBS_FP,
    clearScreen,
    loadJobs,
    notLoggedIn,
    printOptionList,
    MAX_JOBS,
)
from pages.application import applyToJob, notAppliedList, personalApplicationList
from pages.savedJobs import createSavedJob, deletedSavedJob, printSavedJobs

jobOptionsList = [
    "*** Job Search ***",
    "1 - Search for Job/Internship",
    "2 - Post Job/Internship",
    "3 - View Saved Jobs",
    "4 - View Applications",
    "5 - View Open Jobs without Applications",
    "6 - Delete Job/Internship",
    returnToPreviousMenuMessage(),
]

jobListingChoices = [
    "*** Job Options ***",
    "1 - Apply for Job",
    "2 - Save Job",
    "3 - Unsave Job",
    returnToPreviousMenuMessage(),
]

jobApplicationDeleted = [
    "A job you applied for has been deleted",
]


# TODO check currentUser is not none
# user selected to do a job search
def printJobSearchScreen(currentUser: Optional[User] = None) -> Optional[User]:
    while True:
        clearScreen()
        # If the currentUser has had an application deleted they will be notified
        if currentUser != None:
            if currentUser.applicationDeleted != "UNDEFINED":
                printOptionList(jobApplicationDeleted)
                # print('The job you applied for "'+ currentUser.applicationDeleted+ '" has been deleted')
                # The applicationDeleted is the title of the job that was deleted, instructions state that only a notification about "A" job being deleted is required.
                currentUser.applicationDeleted = "UNDEFINED"  # reset applicationDeleted
        printOptionList(jobOptionsList)  # print job options
        userInput = input("")
        if userInput == "1":
            currentUser = jobSearch(currentUser)
        elif userInput == "2":
            currentUser = createJob(currentUser)
        elif userInput == "3":
            currentUser = printSavedJobs(currentUser)
        elif userInput == "4":
            clearScreen()
            print("*** Application List ***")
            applicationList = personalApplicationList(currentUser)
            for i in range(0, len(applicationList)):
                print(applicationList[i])
            print(anyButtonToContinueMessage())
            input("")
        elif userInput == "5":
            clearScreen()
            print("*** List of Jobs Not Applied To ***")
            notApplied = notAppliedList(currentUser)
            for i in range(0, len(notApplied)):
                print(notApplied[i])
            print(anyButtonToContinueMessage())
            input("")
        elif userInput == "6":
            print("*** Delete Job ***")
            currentUser = deleteJob(currentUser)
        elif userInput.upper() == "X":
            break
        else:
            print(invalidInput("Please select a valid option"))
            print(anyButtonToContinueMessage())
            input("")

    return currentUser


def jobSearch(currentUser: Optional[User] = None) -> Optional[User]:
    clearScreen()
    jobDB = JobDatabase()
    jobDB.loadJobs()
    jobs = jobDB.getJobListDict()
    totalJobs = len(jobs)
    # Printing all current positions
    print("Current Open Positions:")

    # checking to see if currentUser is logged in
    if notLoggedIn(currentUser):
        print(anyButtonToContinueMessage())
        input("")
        return currentUser

    if totalJobs == 0:
        print("There are currently no open positions")
        print(anyButtonToContinueMessage())
        input("")
        return currentUser
    else:
        # Determining if currentUser already applied to job and printing out job list
        for i in range(0, totalJobs):
            flag = False
            applicationNum = len(jobs[i]["applicants"])
            for j in range(0, applicationNum):
                if jobs[i]["applicants"][j]["username"] == currentUser.username:
                    print(i + 1, "-", jobs[i]["title"], "** Applied **")
                    flag = True
                # j += 1 # DELETE ME ?
            if flag == False:
                print(i + 1, "-", jobs[i]["title"])
            # i += 1 # DELETE ME ?
        returnToPreviousMenuMessage()

        print("Input a number for more details")
        # Printing details of jobs by request
        while True:
            userInput = input("")
            if userInput.upper() == "X":
                break

            try:
                userInputInt = int(userInput)
            except ValueError:  # If the user inputs a non-integer
                print(invalidInput("a number"))
                print(anyButtonToContinueMessage())
                input("")
                return currentUser
            # temp = int(userInput)

            if userInputInt in range(1, totalJobs + 1):
                clearScreen()
                print(
                    "Title: ",
                    jobs[userInputInt - 1]["title"],
                    "\nDescription: ",
                    jobs[userInputInt - 1]["description"],
                    "\nEmployer: ",
                    jobs[userInputInt - 1]["employer"],
                    "\nLocation: ",
                    jobs[userInputInt - 1]["location"],
                    "\nSalary: ",
                    jobs[userInputInt - 1]["salary"],
                    "\n",
                )
                print(anyButtonToContinueMessage())
                input("")

                printJobOptionScreen(userInputInt - 1, currentUser)
                break
            else:
                print(
                    invalidInput("Please choose a valid option")
                )  # TODO Format valid input options, spent way too long trying to to it
                print(anyButtonToContinueMessage())
                input("")

    return currentUser


def printJobOptionScreen(jobIndex, currentUser: Optional[User] = None) -> Optional[User]:
    while True:
        clearScreen()
        printOptionList(jobListingChoices)
        userInput = input("")

        if userInput == "1":
            currentUser = applyToJob(jobIndex, currentUser)
        elif userInput == "2":
            currentUser = createSavedJob(jobIndex, currentUser)
        elif userInput == "3":
            currentUser = deletedSavedJob(jobIndex, currentUser)
        elif userInput.upper() == "X":
            break
        else:
            print(invalidInput("1, 2, 3, or X"))
            print(anyButtonToContinueMessage())
            input("")

    return currentUser


def createJob(currentUser: Optional[User] = None) -> Optional[User]:
    clearScreen()
    print("*** Post a Job/Internship ***")
    # Must be logged in to create job
    if notLoggedIn(currentUser):
        print(anyButtonToContinueMessage())
        input("")
        return currentUser
    jobDB = JobDatabase()
    jobDB.loadJobs()
    jobs = jobDB.getJobListDict()
    # jobs = loadJobs()
    # print(jobs) # DELETE ME ?
    # users = loadUsers()
    userDB = UserDatabase([])
    userDB.loadUsers()

    if len(jobs) < MAX_JOBS:  # Requirement for 10 job postings
        while True:
            clearScreen()
            print("*** Create a new job posting ***")
            title = input("Job Title: ")
            description = input("Brief Description of the Job: ")
            employer = input("Employer: ")
            location = input("Location: ")
            salary = input("Salary: ")

            newJob = Job(
                title,
                description,
                employer,
                location,
                salary,
                currentUser.firstname,
                currentUser.lastname,
            )
            try:
                jobDB.addJob(newJob)
            except MaximumNumberOfJobs as e:
                print(f"Error: {e}")
                print(anyButtonToContinueMessage())
                input("")
                break

            # try:
            #     saveJob(
            #         jobs,
            #         title,
            #         description,
            #         employer,
            #         location,
            #         salary,
            #         currentUser.firstname,
            #         currentUser.lastname,
            #     )
            # except:
            #     print("Error: There was an error saving the job. Please try again")
            #     pass
            # clearScreen()  # TODO I don't think this is needed

            print("\nJob Created!")
            break
    else:
        print(
            "All permitted jobs have been posted, please try again later"
        )  # Requirement for 10 accounts response
    print(anyButtonToContinueMessage())
    input("")
    return currentUser


def deleteJob(currentUser):
    jobDB = JobDatabase()
    jobDB.loadJobs()
    jobs = jobDB.getJobListDict()
    if len(jobs) == 0:
        print("There are no jobs to delete")
        print(anyButtonToContinueMessage())
        input("")
        return currentUser
    # jobs = loadJobs() #Delete me
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
    jobFoundFlag = False
    for i in range(0, len(jobs)):
        if jobs[i]["title"] == jobToDelete:
            jobFoundFlag = True
            # Check if the current user is the poster of the job
            if (
                jobs[i]["firstname"] == currentUser.firstname
                and jobs[i]["lastname"] == currentUser.lastname
            ):
                # Notify applicants that the job has been deleted
                userDB = UserDatabase([])
                userDB.loadUsers()
                for j in range(0, len(jobs[i]["applicants"])):
                    # The next time that the student visits the jobs section, they will be notified that a job that they applied for has been deleted.
                    userDB.getUser(jobs[i]["applicants"][j]["username"]).applicationDeleted = jobs[
                        i
                    ]["title"]
                    userDB.updateUser(userDB.getUser(jobs[i]["applicants"][j]["username"]))
                    # jobs[i]["applicants"][j]["username"] = "username of applicant"
                # Remove the job
                del jobs[i]

                jobDB.joblist = jobs
                #jobDB.saveDatabase()

                print("Job deleted successfully")
                print(anyButtonToContinueMessage())
                input("")
                break
            else:
                print("You are not the poster of this job.")
                print(anyButtonToContinueMessage())
                input("")
                return currentUser
        else:
            continue
    if jobFoundFlag == False:
        print("Job does not exist")
        print(anyButtonToContinueMessage())
        input("")
        return currentUser
    # Save the job database
    jobDB.saveDatabase()  # TODO This is not needed
    # saveJobDatabase(JSON_JOBS_FP, jobs)

    return currentUser


def removeJob(currentUser: Optional[User] = None) -> Optional[User]:
    # Must be logged in to delete job
    jobs = loadJobs()
    # If user is not logged in
    if not isinstance(currentUser, User):
        print("You must be logged in to remove a Job.")
        print(anyButtonToContinueMessage())
        input("")
        return currentUser

    # TODO Get the job index
    jobIndex = 0

    # If user created the job posting
    if (
        jobs[jobIndex]["firstname"] == currentUser.firstname
        and jobs[jobIndex]["lastname"] == currentUser.lastname
    ):
        print("Job Removed")
        job = jobs[jobIndex]
        # TODO Notifiy Applicants
        for people in job["applicants"]:
            # TODO Notify people
            pass
        jobs.remove(job)
        # jobs.pop(jobIndex)
        saveJobDatabase(JSON_JOBS_FP, jobs)
        print(anyButtonToContinueMessage())
        input("")
        return currentUser
    else:
        print("You cannot remove a job posting that you did not create")
        print(anyButtonToContinueMessage())
        input("")
        return currentUser
