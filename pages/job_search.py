import json
import os

from common_utils.utils import clearScreen, loadJobs, loadUsers
from pages.main_menu import printMainMenu

MAXJOBS = 5
JSONFP = os.path.join(os.path.dirname(__file__), "..")


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
            # Search function under construction
            print("under construction, input anything to return")
            tempInput = input()
            printJobSearchScreen()
        elif userInput == "2":
            createJob(currentUser)
        elif userInput == "3":
            printMainMenu()
        else:
            print('Invalid selection please input "1" or "2" or "3"')


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

            # get index of current user
            for i, user in enumerate(users):
                if user["username"] == currentUser:
                    currentUserIndex = i
                    break
            # retrieving first and last name from current user
            firstname = users[currentUserIndex]["firstname"]
            lastname = users[currentUserIndex]["lastname"]
            saveJob(title, description, employer, location, salary, firstname, lastname)

    print("All permitted jobs have been posted, please try again later")  # Requirement for 5 accounts response
    print("Please press any button to continue")
    tempInput = input()
    return -1


def saveJob(title, description, employer, location, salary, firstname, lastname):
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
    jobs = {"joblist": jobs}
    os.chdir(JSONFP)
    with open("jobs.json", "w") as outfile:
        json.dump(jobs, outfile, indent=4)
