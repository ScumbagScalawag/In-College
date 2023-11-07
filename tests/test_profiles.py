import pytest
from pages.profiles import (
    inputWithExit,
    addEducationToProfile,
    addExperiencesToProfile,
    createProfile,
    printProfileScreen,
    printEditProfile,
    addNewExperience,
)
from common_utils.types.profile import Profile
from common_utils.types.user import User
from common_utils.types.user_database import UserDatabase
from tests.shared import fourAccounts, sampleProfile, emptyProfile
import pytest
from pages.profiles import addEducationToProfile
from common_utils.types.profile import Profile


@pytest.mark.parametrize(
    "mock_input,expectedReturn",
    [
        (
            ["Foam Earplugs"],
            "Foam Earplugs",
        ),
        (
            ["X"],
            None,
        ),
    ],
    ids=["Foam Earplugs", "X"],
)
def testInputWithExit(mock_input, expectedReturn, monkeypatch, capfd):
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert inputWithExit(mock_input) == expectedReturn
    except StopIteration:
        pass


@pytest.mark.parametrize(
    "school_name, degree, years_attended",
    [
        (
            "University of South Florida",
            "Bachelor of Science",
            "2020-2023",
        ),
        (
            "Cloud University",
            "X",
            "2006-2067",
        ),
        (
            "FIU",
            "PhD",
            "X",
        ),
        ("X", "AS", "2222-2223"),
        (
            "X",
            "X",
            "X",
        ),
    ],
    ids=["Valid Education", "No Degree", "No Years Attended", "No School Name", "XXX"],
)
def testAddEducationToProfile(school_name, degree, years_attended, monkeypatch, capfd):
    profile = Profile()
    mock_input = [
        school_name,
        degree,
        years_attended,
    ]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        testProfile = addEducationToProfile(profile)
        if school_name == "X":
            assert testProfile.education.school_name == None
        else:
            assert testProfile.education.school_name == school_name
        if degree == "X":
            assert testProfile.education.degree == None
        else:
            assert testProfile.education.degree == degree
        if years_attended == "X":
            assert testProfile.education.years_attended == None
        else:
            assert testProfile.education.years_attended == years_attended
    except StopIteration:
        pass


@pytest.mark.parametrize(
    "job_title,employer,date_started,date_ended,location,description",
    [
        (
            "job title",
            "employer",
            "start date",
            "end date",
            "location",
            "description",
        ),
        (
            "X",
            "employer",
            "start date",
            "end date",
            "location",
            "description",
        ),
        (
            "job title",
            "X",
            "start date",
            "end date",
            "location",
            "description",
        ),
        (
            "job title",
            "employer",
            "X",
            "end date",
            "location",
            "description",
        ),
        (
            "job title",
            "employer",
            "start date",
            "X",
            "location",
            "description",
        ),
        (
            "job title",
            "employer",
            "start date",
            "end date",
            "X",
            "description",
        ),
        (
            "job title",
            "employer",
            "start date",
            "end date",
            "location",
            "X",
        ),
        (
            "X",
            "X",
            "X",
            "X",
            "X",
            "X",
        ),
    ],
    ids=[
        "1-Add",
        "No Title",
        "No Employer",
        "No Start Date",
        "No End Date",
        "No Location",
        "No Description",
        "All X",
    ],
)
def testAddExperiencesToProfile(
    job_title, employer, date_started, date_ended, location, description, monkeypatch, capfd
):
    profile = Profile()
    mock_input = [
        job_title,
        employer,
        date_started,
        date_ended,
        location,
        description,
        "n",
    ]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        testProfile = addExperiencesToProfile(profile)
    except StopIteration:
        pass
    for experience in testProfile.experiences:
        if job_title == "X":
            assert experience.job_title == None
        else:
            assert experience.job_title == job_title
        if employer == "X":
            assert experience.employer == None
        else:
            assert experience.employer == employer
        if date_started == "X":
            assert experience.date_started == None
        else:
            assert experience.date_started == date_started
        if date_ended == "X":
            assert experience.date_ended == None
        else:
            assert experience.date_ended == date_ended
        if location == "X":
            assert experience.location == None
        else:
            assert experience.location == location
        if description == "X":
            assert experience.description == None
        else:
            assert experience.description == description


# TODO Fix this test after fixing addNewExperience or addExperiencesToProfile as they both do the same thing
# TODO 2-Add, 3-Add, Max Reached
# def testAddNewExperience(monkeypatch, capfd):
#     profile = Profile()
#     mock_input = [
#         "job title 1",
#         "employer 1",
#         "start date 1",
#         "end date 1",
#         "location 1",
#         "description 1",
#         "y",
#         "job title 2",
#         "employer 2",
#         "start date 2",
#         "end date 2",
#         "location 2",
#         "description 2",
#         "n",
#     ]
#     input_generator = iter(mock_input)
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
#     try:
#         testProfile = addNewExperience(profile)
#     except StopIteration:
#         pass
#     assert len(testProfile.experiences) == 2
#     for experience in testProfile.experiences:
#         assert experience.job_title == "job title"
#         assert experience.employer == "employer"
#         assert experience.date_started == "start date"
#         assert experience.date_ended == "end date"
#         assert experience.location == "location"
#         assert experience.description == "description"
