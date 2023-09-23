import json
import os

from common_utils.utils import clearScreen, loadJobs, loadUsers

MAXJOBS = 5
JSONFP = os.path.join(os.path.dirname(__file__), "..")
JSONFP2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "jobs.json")


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
    saveJobDatabase(JSONFP2, jobs)
    return


def saveJobDatabase(jsonFilePath, jobs):
    jobDB = {"joblist": jobs}
    with open(jsonFilePath, "w") as outfile:
        json.dump(jobDB, outfile, indent=4)

    return


# user selected to do a job search
def printJobSearchScreen(currentUser):
    clearScreen()
    while True:
        print("*** Job Search ***")
        print("1 - Search for Job/Internship")
        print("2 - Post Job/Internship")
        print("3 - Return to Main Menu")
        userInput = input()

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
    print("under construction, input anything to return")
    userInput = input()
    return 0
