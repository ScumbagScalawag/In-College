import json

from common_utils.utils import clearScreen, loadJobs, loadUsers, JSON_JOBS_FP, printOptionList
from pages.under_construction import underConstructionMessage

MAXJOBS = 5


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
    "3 - Return to Main Menu",
]


# TODO check currentUser is not none
# user selected to do a job search
def printJobSearchScreen(currentUser=None):
    clearScreen()
    while True:
        printOptionList(jobOptionsList)
        userInput = input("")

        if userInput == "1":
            jobSearch()
        elif userInput == "2":
            createJob(currentUser)
            break
        elif userInput == "3":
            break
        else:
            print('Invalid selection please input "1" or "2" or "3"')
    return


def jobSearch():
    # under construction, not needed in EPIC2
    clearScreen()
    print("*** Job Search ***")
    print(underConstructionMessage())
    userInput = input("")
    return 0


# TODO check validity of inputs
def createJob(currentUser):
    jobs = loadJobs()
    users = loadUsers()

    if len(jobs) < MAXJOBS:  # Requirement for 5 job postings
        while True:
            clearScreen()
            print("*** Create a new job posting ***")
            title = input("Job Title: ")  # get job title
            description = input("Brief Description of the Job: ")  # get description of job
            employer = input("Employer: ")  # get employer
            location = input("Location: ")  # get location
            salary = input("Salary: ")  # get salary

            # setting currentUserIndex = 0
            currentUserIndex = None
            # get index of current user
            for i, user in enumerate(users):
                print(user)
                if user["username"] == currentUser:
                    currentUserIndex = i
                    break

            # retrieving first and last name from current user
            firstname = users[currentUserIndex]["firstname"]
            lastname = users[currentUserIndex]["lastname"]
            saveJob(jobs, title, description, employer, location, salary, firstname, lastname)
            clearScreen()  # TODO I don't think this is needed
            return

    print(
        "All permitted jobs have been posted, please try again later"
    )  # Requirement for 5 accounts response
    print("Please press any button to continue")
    tempInput = input("")
    return -1
