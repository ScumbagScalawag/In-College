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
from common_utils.utils import (
    JSON_JOBS_FP,
    clearScreen,
    loadJobs,
    notLoggedIn,
    printOptionList,
)


def createSavedJob(jobIndex, currentUser):
    clearScreen()
    jobs = loadJobs()

    jobs[jobIndex]["saved"].append(currentUser.username)
    saveJobDatabase(JSON_JOBS_FP, jobs)
    print("Sucessfully saved job")
    print(anyButtonToContinueMessage())
    input("")

    return currentUser


def deletedSavedJob(jobIndex, currentUser):
    jobs = loadJobs()
    jobs[jobIndex]["saved"].remove(currentUser.username)
    saveJobDatabase(JSON_JOBS_FP, jobs)
    print("Sucessfully removed job")
    print(anyButtonToContinueMessage())
    input("")

    return currentUser


def printSavedJobs(currentUser):
    clearScreen()
    print("*** Saved Jobs ***")
    jobs = loadJobs()
    totalJobs = len(jobs)
    savedList = []
    for i in range(0, totalJobs):
        totalUsersSaved = len(jobs[i]["saved"])
        for j in range(0, totalUsersSaved):
            if currentUser.username == jobs[i]["saved"][j]:
                savedList.append(jobs[i]["title"])
            j += 1
        i += 1

    for k in range(0, len(savedList)):
        print(savedList[k])
        k += 1
    print(anyButtonToContinueMessage())
    input("")
    return currentUser
