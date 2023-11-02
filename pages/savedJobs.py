from common_utils.messages import (
    anyButtonToContinueMessage,
)
from common_utils.utils import (
    JSON_JOBS_FP,
    clearScreen,
)
from common_utils.types.job_database import JobDatabase


def createSavedJob(jobIndex, currentUser):
    clearScreen()
    jobDB = JobDatabase()
    jobDB.loadJobs()
    jobs = jobDB.joblist
    # jobs = loadJobs() #Delete me
    jobs[jobIndex]["saved"].append(currentUser.username)
    saveJobDatabase(JSON_JOBS_FP, jobs)
    print("Sucessfully saved job")
    print(anyButtonToContinueMessage())
    input("")

    return currentUser


def deletedSavedJob(jobIndex, currentUser):
    clearScreen()
    jobDB = JobDatabase()
    jobDB.loadJobs()
    jobs = jobDB.joblist
    # jobs = loadJobs() #Delete me
    jobs[jobIndex]["saved"].remove(currentUser.username)
    jobDB.saveDatabase()
    # saveJobDatabase(JSON_JOBS_FP, jobs)
    print("Sucessfully removed job")
    print(anyButtonToContinueMessage())
    input("")

    return currentUser


def printSavedJobs(currentUser):
    clearScreen()
    print("*** Saved Jobs ***")
    jobDB = JobDatabase()
    jobDB.loadJobs()
    jobs = jobDB.joblist
    # jobs = loadJobs() #Delete me
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
        print(k + 1, "-", savedList[k])
        k += 1
    print(anyButtonToContinueMessage())
    input("")
    return currentUser
