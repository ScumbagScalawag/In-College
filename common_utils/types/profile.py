import json
from typing import Optional, List
from common_utils.types.education import Education
from common_utils.types.experience import Experience


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
        education: Optional[Education] = None,
        experiences: Optional[List[Experience]] = None
    ):
        self.username = username
        self.title = title
        self.major = self.formatTextCapital(major)
        self.university = self.formatTextCapital(university)
        self.about = about
        self.education = education if education else Education()
        self.experiences = experiences if experiences else []
    # WARNING: This method only copies VALUES from otherProfile: profile2.copyValues(profile1)
    def copyValues(self, otherProfile):
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
            "education": self.education.toDict() if self.education else None,
            "experiences": [exp.toDict() for exp in self.experiences]
        }

    # The attributes can be retrieved manually. like this: userObject.firstname

    # SETTERS

    ## Return a User into userObject with: userObject = User.dictToUser(singleUserDict)
    # singleUserDict: For example, see singleUser in tests.shared
    @classmethod
    def dictToProfile(cls, userProfile):
        # Convert experience dictionaries into Experience objects
        experiences_list = userProfile.get("experiences", [])
        experiences_obj_list = [Experience.dictToExperience(exp_dict) for exp_dict in experiences_list]

        # Convert education dictionary into an Education object
        education_data = userProfile.get("education", {})
        education_obj = Education(
            school_name=education_data.get("school_name", "UNDEFINED"),
            degree=education_data.get("degree", "UNDEFINED"),
            years_attended=education_data.get("years_attended", "UNDEFINED")
        )

        return cls(
            username=userProfile.get("username", "UNDEFINED"),
            title=userProfile.get("title", "UNDEFINED"),
            major=userProfile.get("major", "UNDEFINED"),
            university=userProfile.get("university", "UNDEFINED"),
            about=userProfile.get("about", "UNDEFINED"),
            experiences=experiences_obj_list,
            education=education_obj
        )

    # Convert word that starts with uppercase letter and the rest is lower case.
    def formatTextCapital(self, text):
        new_text = " ".join(word.capitalize() for word in text.split())
        return new_text

    # Pick a way of doing it and comment out the other.
    def add_experience(self, title, employer, date_started, date_ended, location, description):
        experience = Experience(title, employer, date_started, date_ended, location, description)
        self.experiences.append(experience)

    #def add_experience(self, experience):
    #    self.experiences.append(experience)

  #  def add_education(self, education):
   #     self.education.append(education)

    def add_education(self, school_name, degree, years_attended):
        new_education = Education(school_name, degree, years_attended)
        self.education.append(new_education)

    # updates
    def update_title(self, new_title):
        self.title = new_title

    def update_major(self, new_major):
        self.major = new_major

    def update_university(self, new_university):
        self.university = new_university

    def update_about(self, new_about):
        self.about = new_about

    def __str__(self):
        return json.dumps(self.toDict(), indent=4)
