import pytest  # needed for pytest
from tests.shared import emptyProfile, sampleProfile  # needed for testWithDatabaseSet
from common_utils.types.user_database import UserDatabase
from common_utils.types.user import User
from common_utils.types.profile import Profile


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