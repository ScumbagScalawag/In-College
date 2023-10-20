import json


# Copy from user class
class Experience:
    # Constructor (w/ default values)
    def __init__(
        self,
        title: str = "UNDEFINED",
        employer: str = "UNDEFINED",
        date_started: str = "UNDEFINED",
        date_ended: str = "UNDEFINED",
        location: str = "UNDEFINED",
        description: str = "UNDEFINED",
    ):
        self.username = username
        self.title = title
        self.employer = employer
        self.date_started = date_started
        self.date_ended = date_ended
        self.location = location
        self.description = description

    # WARNING: This method only copies VALUES from otherExperience: experience2.copyValues(experience1)
    def copyValues(self, otherExperience):
        self.username = otherExperience.username
        self.username = otherExperience.username
        self.title = otherExperience.title
        self.major = otherExperience.major
        self.university = otherExperience.university
        self.about = otherExperience.about
        self.experience_paragraph = otherExperience.experience_paragraph
        self.education_paragraph = otherExperience.education_paragraph

    # define what print(userObject) does
    # print(user), where user: User
    def __str__(self):
        return json.dumps(self.toDict(), indent=4)

    # for user1 == user2 expression, where otherUser is of type User
    def __eq__(self, otherExperience) -> bool:
        # in case otherUser is None
        if not isinstance(otherExperience, Profile):
            return False
        else:
            return self.username == otherExperience.username

    # GETTERS

    # return the Dict translation
    def toDict(self):
        return {
            "username": self.username,
            "title": self.title,
            "major": self.major,
            "university": self.university,
            "about": self.about,
            "experience": self.experience_paragraph,
            "education": self.education_paragraph,
        }

    # The attributes can be retrieved manually. like this: userObject.firstname

    # SETTERS

    ## Return a User into userObject with: userObject = User.dictToUser(singleUserDict)
    # singleUserDict: For example, see singleUser in tests.shared
    @classmethod
    def dictToProfile(cls, userProfile):
        return cls(
            username=userProfile.get("username", "UNDEFINED"),
            title=userProfile.get("title", "UNDEFINED"),
            major=userProfile.get("major", "UNDEFINED"),
            university=userProfile.get("university", "UNDEFINED"),
            about=userProfile.get("about", "UNDEFINED"),
            experience_paragraph=userProfile.get("experience", "UNDEFINED"),
            education_paragraph=userProfile.get("education", "UNDEFINED"),
        )

    # Convert word that starts with uppercase letter and the rest is lower case.
    def formatTextCapital(text):
        new_text = " ".join(word.capitalize() for word in text.split())
        return new_major
