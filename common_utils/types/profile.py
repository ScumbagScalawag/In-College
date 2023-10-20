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
        experiences=[],
        education=[],
    ):
        self.username = username
        self.title = title
        self.major = self.formatTextCapital(major)
        self.university = self.formatTextCapital(university)
        self.about = about
        self.experiences = experiences
        self.education = education

    # WARNING: This method only copies VALUES from otherProfile: profile2.copyValues(profile1)
    def copyValues(self, otherProfile):
        self.username = otherProfile.username
        self.username = otherProfile.username
        self.title = otherProfile.title
        self.major = otherProfile.major
        self.university = otherProfile.university
        self.about = otherProfile.about
        self.experiences = otherProfile.experiences
        self.education = otherProfile.education

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
            "experience": self.experiences,
            "education": self.education,
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
            experiences=userProfile.get("experience", "UNDEFINED"),
            education=userProfile.get("education", "UNDEFINED"),
        )

    # Convert word that starts with uppercase letter and the rest is lower case.
    def formatTextCapital(text):
        new_text = " ".join(word.capitalize() for word in text.split())
        return new_major

    def add_experience(self, title, employer, date_started, date_ended, location, description):
        experience = Experience(title, employer, date_started, date_ended, location, description)
        self.experiences.append(experience)
        
    def add_experience(self, experience):
        self.experiences.append(experience)


    def add_education(self, school_name, degree, years_attended):
        
        print("AAA")

    def update_title(self, new_title):
        self.title = new_title
    
    def update_major(self, new_major):
        self.major = new_major
    
    def update_university(self, new_university):
        self.university = new_university
    
    def update_about(self, new_about):
        self.about = new_about
    

    major: str = "UNDEFINED",
        university: str = "UNDEFINED",
        about: str = "UNDEFINED",
        experiences=[],
        education=[],
    