import pytest  # needed for pytest
from tests.shared import fourAccounts, emptyProfile, sampleProfile  # needed for testWithDatabaseSet
from common_utils.types.user_database import UserDatabase
from common_utils.types.user import User
from common_utils.types.profile import Profile
from pages.friends import printFriendsScreen, friendScreenOptions


def test_toDict():
    profile = Profile()
    profileDict = profile.toDict()
    assert profileDict == emptyProfile

def test_dictToProfile():
    profile = Profile.dictToProfile(sampleProfile)
    profileDict = profile.toDict()
    assert profileDict == sampleProfile

def test_addExperience():
    experienceList = sampleProfile["experiences"]
    experienceDict = experienceList[0]
    profile = Profile()
    profile.add_experience(experienceDict["job_title"], experienceDict["employer"], experienceDict["date_started"], experienceDict["date_ended"], experienceDict["location"], experienceDict["description"])
    profileExperienceList = profile.toDict()["experiences"]
    assert profileExperienceList == experienceList

def test_addEducation():
    educationDict = sampleProfile["education"]
    profile = Profile()
    profile.add_education(educationDict["school_name"], educationDict["degree"], educationDict["years_attended"])
    profileExperienceDict = profile.toDict()["education"]
    assert profileExperienceDict == educationDict

def test_copyValues():
    profile1 = Profile()
    profile2 = Profile.dictToProfile(sampleProfile)
    profile1.copyValues(profile2)
    profile1Dict = profile1.toDict()
    profile2Dict = profile2.toDict()
    assert profile1Dict == profile2Dict

def testViewFriendProfile(monkeypatch, capfd):
    # in system
    userDB = UserDatabase([])

    # Add mutual friends to dict
    fourAccountsWithFriendsProfiles = fourAccounts[:]
    currentUsername = fourAccountsWithFriendsProfiles[1]["username"]
    friendUsername = fourAccountsWithFriendsProfiles[0]["username"]
    fourAccountsWithFriendsProfiles[1]["friends"] = [friendUsername]
    fourAccountsWithFriendsProfiles[0]["friends"] = [currentUsername]
    fourAccountsWithFriendsProfiles[0]["profile"] = sampleProfile

    userDB.addUserDictList(fourAccountsWithFriendsProfiles)

    # Must create User object from singleUser Dict. See @classmethod dictToUser
    testUser = User.dictToUser(fourAccountsWithFriendsProfiles[1])

    input_generator = iter(
        [
            "1",
            "2",
        ]
    )  # Make it choose to remove friend here
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert (
            printFriendsScreen(testUser) == testUser
        )  # assert printFriendsScreen returns user context correctly
    except StopIteration:
        pass

    captured = capfd.readouterr()  # assert captured
    responses = [
        *friendScreenOptions,
        "1 - {} - Profile".format(friendUsername),
        "X - Return to previous menu",
        "1. Remove Friend",  
        "2. View Friend Profile",
        "X. Exit",
        "*** Profile of {} {} ***".format(fourAccountsWithFriendsProfiles[0]["firstname"], fourAccountsWithFriendsProfiles[0]["lastname"]),
        "Title: {}".format(sampleProfile["title"]),
        "Major: {}".format(sampleProfile["major"]),
        "University: {}".format(sampleProfile["university"]),
        "About: {}".format(sampleProfile["about"]),
        "Education:",
        "School Name: {}".format(sampleProfile["education"]["school_name"]),
        "Degree: {}".format(sampleProfile["education"]["degree"]),
        "Years Attended: {}".format(sampleProfile["education"]["years_attended"]),
        "Experiences:",
        #Experiences would go here but they seem to be missing
    ]
    for experience in sampleProfile["experiences"]:
        for key, value in experience.items():
            if key == "job_title":
                responses.append("Job Title: {}".format(value))
            elif key == "employer":
                responses.append("Employer: {}".format(value))
            elif key == "date_started":
                responses.append("Start Date: {}".format(value))
            elif key == "date_ended":
                responses.append("End Date: {}".format(value))
            elif key == "location":
                responses.append("Location: {}".format(value))
            elif key == "description":
                responses.append("Description: {}".format(value))

    for r in responses:
        assert r in captured.out