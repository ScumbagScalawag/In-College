import json


# Copy from user class
class Education:
    # Constructor (w/ default values)
    def __init__(
        self,
        school_name: str = "UNDEFINED",
        degree: str = "UNDEFINED",
        years_attended: str = "UNDEFINED",
    ):
        self.school_name = school_name
        self.degree = degree
        self.years_attended = years_attended

    # WARNING: This method only copies VALUES from otherEducation: experience2.copyValues(experience1)
    def copyValues(self, otherEducation):
        self.school_name = otherEducation.job_title
        self.degree = otherEducation.degree
        self.years_attended = otherEducation.years_attended

    # define what print(userObject) does
    # print(user), where user: User
    def __str__(self):
        return json.dumps(self.toDict(), indent=4)

    # for user1 == user2 expression, where otherUser is of type User
    def __eq__(self, otherEducation) -> bool:
        # in case otherUser is None
        if not isinstance(otherEducation, Education):
            return False
        else:
            return self.degree == otherEducation.degree

    # GETTERS
    # return the Dict translation
    def toDict(self):
        return {
            "school_name": self.school_name,
            "degree": self.degree,
            "years_attended": self.years_attended,
        }

    # The attributes can be retrieved manually. like this: userObject.firstname

    # SETTERS

    ## Return a User into userObject with: userObject = User.dictToUser(singleUserDict)
    # singleUserDict: For example, see singleUser in tests.shared
    @classmethod
    def dictToProfile(cls, userEducation):
        return cls(
            username=userEducation.get("school_name", "UNDEFINED"),
            degree=userEducation.get("degree", "UNDEFINED"),
            years_attended=userEducation.get("years_attended", "UNDEFINED"),
        )

    # updates ; not really used for anything
    def update_job_title(self, new_job_title):
        self.job_title = new_job_title

    def update_school_name(self, new_school_name):
        self.school_name = new_school_name

    def update_degree(self, new_degree):
        self.degree = new_degree

    def update_years_attended(self, new_years_attended):
        self.years_attended = new_years_attended
