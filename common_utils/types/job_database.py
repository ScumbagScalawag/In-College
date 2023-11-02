from typing import List, Optional
from common_utils.types.exceptions import MaximumNumberOfJobs, JobNotFoundException
from common_utils.types.job import Job
from common_utils.utils import JSON_JOBS_FP, MAX_JOBS
import json


class JobDatabase:
    def __init__(self, joblist: Optional[List[Job]] = None):
        if joblist is None:
            joblist = []
        self.joblist = joblist

    def __str__(self):
        return json.dumps(self.toDict(), indent=4)

    def loadJobs(self):
        self.joblist = []
        try:
            with open(JSON_JOBS_FP, "r") as database:
                jobDBDict = json.load(database)
                for jobDict in jobDBDict.get("joblist", []):
                    job = Job.dictToJob(jobDict)
                    self.joblist.append(job)
        except (FileNotFoundError, json.JSONDecodeError):  # Handle file not found or invalid JSON
            print("WARNING: Cannot find JSON DataBase!")
            pass

    def getDatabaseDict(self):
        return {"joblist": self.getJobListDict()}

    def getJobListDict(self):
        jobDictList = []
        for job in self.joblist:
            jobDictList.append(job.toDict())
        return jobDictList

    def jobExists(self, title: str):
        for job in self.joblist:
            if job.title == title:
                return True
        return False

    def getJob(self, title: str) -> Optional[Job]:
        for job in self.joblist:
            if job.title == title:
                return job
        return None

    # TODO if needed def jobSearch
    def saveDatabase(self):
        if len(self.joblist) > MAX_JOBS:
            raise MaximumNumberOfJobs("Cannot Write to JobDatabase: Maximum number of jobs reached")
        with open(JSON_JOBS_FP, "w") as outfile:
            json.dump(self.getDatabaseDict(), outfile, indent=4)

    def updateJob(self, alteredJob: Optional[Job]) -> Optional[Job]:
        if isinstance(alteredJob, Job):
            for i, job in enumerate(self.joblist):
                if job.title == alteredJob.title:
                    self.joblist[i].copyValues(alteredJob)
                    self.saveDatabase()
                    return
        raise JobNotFoundException("Couldn't find match for user")

    def addJob(self, job: Job):
        if len(self.joblist) < MAX_JOBS:
            self.joblist.append(job)
            self.saveDatabase()
        else:
            raise MaximumNumberOfJobs("Cannot Write to JobDatabase: Maximum number of jobs reached")

    def addJobList(self, jobList: List[Job]):
        for user in jobList:
            self.addJob(job)

    def addJobDictList(self, jobDictList: List[dict]):
        for jobDict in jobDictList:
            self.addJobDict(jobDict)
