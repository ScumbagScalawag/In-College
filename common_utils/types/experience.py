import json


# Copy from user class
class Experience:
    # Constructor (w/ default values)
    def __init__(
        self,
        job_title: str = "UNDEFINED",
        employer: str = "UNDEFINED",
        date_started: str = "UNDEFINED",
        date_ended: str = "UNDEFINED",
        location: str = "UNDEFINED",
        description: str = "UNDEFINED",
    ):
        self.job_title = job_title
        self.employer = employer
        self.date_started = date_started
        self.date_ended = date_ended
        self.location = location
        self.description = description

    # WARNING: This method only copies VALUES from otherExperience: experience2.copyValues(experience1)
    def copyValues(self, otherExperience):
        self.job_title = otherExperience.job_title
        self.employer = otherExperience.employer
        self.date_started = otherExperience.date_started
        self.date_ended = otherExperience.date_ended
        self.location = otherExperience.location
        self.description = otherExperience.description

    # define what print(userObject) does
    # print(user), where user: User
    def __str__(self):
        return json.dumps(self.toDict(), indent=4)

    # for user1 == user2 expression, where otherUser is of type User
    def __eq__(self, otherExperience) -> bool:
        # in case otherUser is None
        if not isinstance(otherExperience, Experience):
            return False
        else:
            return self.username == otherExperience.username

    # GETTERS

    # return the Dict translation
    def toDict(self):
        return {
            "job_title": self.job_title,
            "employer": self.employer,
            "date_started": self.date_started,
            "date_ended": self.date_ended,
            "location": self.location,
            "description": self.description
        }

    # The attributes can be retrieved manually. like this: userObject.firstname

    # SETTERS

    ## Return a User into userObject with: userObject = User.dictToUser(singleUserDict)
    # singleUserDict: For example, see singleUser in tests.shared
    @classmethod
    def dictToProfile(cls, userProfile):
        return cls(
            username=userProfile.get("username", "UNDEFINED"),
            job_title=userProfile.get("job_title", "UNDEFINED"),
            employer=userProfile.get("employer", "UNDEFINED"),
            date_started=userProfile.get("date_started", "UNDEFINED"),
            date_ended=userProfile.get("date_ended", "UNDEFINED"),
            location=userProfile.get("location", "UNDEFINED"),
            description=userProfile.get("description", "UNDEFINED")
        )
    # Convert word that starts with uppercase letter and the rest is lower case.
    # or return " ".join(word.capitalize() for word in text.split())
    def formatTextCapital(text):
        new_text = " ".join(word.capitalize() for word in text.split())
        return new_text

    # updates ; not really used for anything
    def update_job_title(self, new_job_title):
        self.job_title = new_job_title

    def update_employer(self, new_employer):
        self.employer = new_employer

    def update_date_started(self, new_date):
        self.date_started = new_date

    def update_date_ended(self, new_date):
        self.date_ended = new_date

    def update_location(self, new_location):
        self.location = new_location

    def update_description(self, new_description):
        self.description = new_description

