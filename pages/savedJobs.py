from common_utils.messages import anyButtonToContinueMessage
from common_utils.types.job_database import JobDatabase
from common_utils.utils import JSON_JOBS_FP, clearScreen


def createSavedJob(jobIndex, currentUser):
    clearScreen()
    jobDB = JobDatabase()
    jobDB.loadJobs()
    jobs = jobDB.getJobListDict()
    # jobs = loadJobs() #Delete me
    jobs[jobIndex]["saved"].append(
        {
            "username": currentUser.username,
        }
    )
    # jobDB.joblist = jobs
    jobDB.saveDatabase()
    # saveJobDatabase(JSON_JOBS_FP, jobs) #Delete me
    print("Sucessfully saved job")
    print(anyButtonToContinueMessage())
    input("")

    return currentUser


def deletedSavedJob(jobIndex, currentUser):
    clearScreen()
    jobDB = JobDatabase()
    jobDB.loadJobs()
    jobs = jobDB.getJobListDict()
    # jobs = loadJobs() #Delete me
    flag = False
    for savedJob in jobs[jobIndex]["saved"]:
        if savedJob["username"] == currentUser.username:
            jobs[jobIndex]["saved"].remove(savedJob)
            jobDB.saveDatabase()
            print("Sucessfully removed job")
            print(anyButtonToContinueMessage())
            input("")
            flag == True
            break

    if flag == False:
        print("Job not found in saved list")
        print(anyButtonToContinueMessage())
        input("")
    # jobs[jobIndex]["saved"].remove(currentUser.username)
    # jobDB.joblist = jobs
    # saveJobDatabase(JSON_JOBS_FP, jobs)

    return currentUser


def printSavedJobs(currentUser):
    clearScreen()
    print("*** Saved Jobs ***")
    jobDB = JobDatabase()
    jobDB.loadJobs()
    jobs = jobDB.getJobListDict()
    # jobs = loadJobs() #Delete me
    totalJobs = len(jobs)
    savedList = []
    for i in range(0, totalJobs):
        totalUsersSaved = len(jobs[i]["saved"])
        for j in range(0, totalUsersSaved):
            if currentUser.username == jobs[i]["saved"][j]["username"]:
                savedList.append(jobs[i]["title"])

    for k in range(0, len(savedList)):
        print(k + 1, "-", savedList[k])
    print(anyButtonToContinueMessage())
    input("")
    return currentUser
