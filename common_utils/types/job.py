import json


class Job:
    def __init__(
        self,
        title: str = "UNDEFINED",
        description: str = "UNDEFINED",
        employer: str = "UNDEFINED",
        location: str = "UNDEFINED",
        salary: str = "UNDEFINED",
        firstname: str = "UNDEFINED",
        lastname: str = "UNDEFINED",
        applicants=[],
        saved=[],
    ):
        self.title = title
        self.description = description
        self.employer = employer
        self.location = location
        self.salary = salary
        self.firstname = firstname
        self.lastname = lastname
        self.applicants = applicants
        self.saved = saved

    def copyValues(self, otherJob):
        self.title = otherJob.title
        self.description = otherJob.description
        self.employer = otherJob.employer
        self.location = otherJob.location
        self.salary = otherJob.salary
        self.firstname = otherJob.firstname
        self.lastname = otherJob.lastname
        self.applicants = otherJob.applicants.copy()
        self.saved = otherJob.saved.copy()

    def __str__(self):
        return json.dumps(self.toDict(), indent=4)

    def __eq__(self, otherJob) -> bool:
        if not isinstance(otherJob, Job):
            return False
        else:
            return self.title == otherJob.title

    def toDict(self):
        return {
            "title": self.title,
            "description": self.description,
            "employer": self.employer,
            "location": self.location,
            "salary": self.salary,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "applicants": self.applicants,
            "saved": self.saved,
        }

    @classmethod
    def dictToJob(cls, jobDict):
        return cls(
            title=jobDict.get("title", "UNDEFINED"),
            description=jobDict.get("description", "UNDEFINED"),
            employer=jobDict.get("employer", "UNDEFINED"),
            location=jobDict.get("location", "UNDEFINED"),
            salary=jobDict.get("salary", "UNDEFINED"),
            firstname=jobDict.get("firstname", "UNDEFINED"),
            lastname=jobDict.get("lastname", "UNDEFINED"),
            applicants=jobDict.get("applicants", []),
            saved=jobDict.get("saved", []),
        )


# TODO check validity of inputs


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
