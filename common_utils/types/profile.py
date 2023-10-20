import json


# Copy from user class
class Profile:
    # Constructor (w/ default values)
    def __init__(
        self,
        username: str = "UNDEFINED",
        title: str = "UNDEFINED",
        major: str = "UNDEFINED",
        university: str = "UNDEFINED",
        about: str = "UNDEFINED",
        experience_paragraph: str = "UNDEFINED",
        education_paragraph: str = "UNDEFINED",
    ):
        self.username = username
        self.title = title
        self.major = self.formatTextCapital(major)
        self.university = self.formatTextCapital(university)
        self.about = about
        self.experience_paragraph = experience_paragraph
        self.education_paragraph = education_paragraph

    # WARNING: This method only copies VALUES from otherProfile: profile2.copyValues(profile1)
    def copyValues(self, otherProfile):
        self.username = otherProfile.username
        self.username = otherProfile.username
        self.title = otherProfile.title
        self.major = otherProfile.major
        self.university = otherProfile.university
        self.about = otherProfile.about
        self.experience_paragraph = otherProfile.experience_paragraph
        self.education_paragraph = otherProfile.education_paragraph

    # define what print(userObject) does
    # print(user), where user: User
    def __str__(self):
        return json.dumps(self.toDict(), indent=4)

    # for user1 == user2 expression, where otherUser is of type User
    def __eq__(self, otherProfile) -> bool:
        # in case otherUser is None
        if not isinstance(otherProfile, Profile):
            return False
        else:
            return self.username == otherProfile.username

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
