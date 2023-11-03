import pytest
from pages.application import applyToJob, checkDate, personalApplicationList, notAppliedList
from common_utils.messages import anyButtonToContinueMessage, invalidInput, underConstructionMessage
from tests.shared import (
    JSON_JOBS_FP,
    singleUser,
    fourJobs,
    fiveJobs,
    fourAccounts,
    threeAccounts,
    twoJobs,
)
from common_utils.types.user_database import UserDatabase
from common_utils.types.user import User
from common_utils.types.job_database import JobDatabase
from common_utils.types.job import Job


@pytest.mark.parametrize(
    "mock_input,jobIndex,startingUser,startingUserDB,startingJobDB,responses",
    [
        (
            ["01/01/2022", "02/01/2022", "I am fit", ""],  # mock input
            1,  # job index
            singleUser,  # test user
            fourAccounts,  # starting userDB
            fourJobs,  # starting jobDB
            [
                "*** Job Application ***",
                "Application sucessfully submitted",
                anyButtonToContinueMessage(),
            ],  # responses
        ),
        (
            [""],  # mock input
            3,  # job index
            singleUser,  # test user
            fourAccounts,  # starting userDB
            fourJobs,  # starting jobDB
            [
                "You cannot apply for a job you posted.",
                anyButtonToContinueMessage(),
            ],  # responses
        ),
        (
            [""],  # mock input
            0,  # job index
            singleUser,  # test user
            fourAccounts,  # starting userDB
            fourJobs,  # starting jobDB
            [
                "You cannot apply for a job you have already applied to.",
                anyButtonToContinueMessage(),
            ],  # responses
        ),
    ],
    ids=[
        "Valid input apply to job",
        "User has created a job",
        "User has already applied",
    ],
)
def testApplyToJob(
    mock_input, jobIndex, startingUser, startingUserDB, startingJobDB, responses, monkeypatch, capfd
):
    testUser = User.dictToUser(startingUser)
    userDB = UserDatabase([])
    userDB.addUserDictList(startingUserDB)
    jobDB = JobDatabase([])
    jobDB.addJobDictList(startingJobDB)
    jobDB.saveDatabase()
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert applyToJob(jobIndex, testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        if r == "Application sucessfully submitted":
            jobDB.loadJobs()
            assert (
                jobDB.getJobListDict()[jobIndex]["applicants"][0]["username"] == testUser.username
            )
        assert r in captured.out


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("01/01/2022", True),
        ("01/01/22", False),
        ("13/01/2022", False),
        ("01/32/2022", False),
        ("2022/01/01", False),
    ],
    ids=[
        "Valid date",
        "Invalid year",
        "Invalid month",
        "Invalid day",
        "Invalid format",
    ],
)
def test_checkDate(input_string, expected_output):
    assert checkDate(input_string) == expected_output


@pytest.mark.parametrize(
    "user,jobs,expected_output",
    [
        (
            singleUser,  # test user
            fourJobs,  # starting jobDB
            [
                "Software Engineer",
            ],  # responses
        ),
        (
            None,  # test user
            twoJobs,  # starting jobDB
            [],  # responses
        ),
    ],
    ids=[
        "User has applied to some jobs",
        "User not logged in",
    ],
)
def test_PersonalApplicationList(user, jobs, expected_output, monkeypatch, capfd):
    if user is not None:
        testUser = User.dictToUser(user)
    else:
        testUser = user
    jobDB = JobDatabase([])
    jobDB.addJobDictList(jobs)
    jobDB.saveDatabase()
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert personalApplicationList(testUser) == expected_output
    except StopIteration:
        pass


@pytest.mark.parametrize(
    "user,jobs,expected_output",
    [
        (
            singleUser,  # test user
            fourJobs,  # starting jobDB
            [
                "Data Analyst",
                "Potato Masher",
                "Magician",
            ],  # responses
        ),
        (
            None,  # test user
            twoJobs,  # starting jobDB
            [],  # responses
        ),
    ],
    ids=[
        "User has not applied to some jobs",
        "User not logged in",
    ],
)
def test_notAppliedList(user, jobs, expected_output, monkeypatch, capfd):
    if user is not None:
        testUser = User.dictToUser(user)
    else:
        testUser = user
    jobDB = JobDatabase([])
    jobDB.addJobDictList(jobs)
    jobDB.saveDatabase()
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert notAppliedList(testUser) == expected_output
    except StopIteration:
        pass


# TODO test personalApplicationList
# @pytest.mark.parametrize(
#     "user, jobs, expected_output",
#     [
#         (
#             User("test_user", "password"),
#             [
#                 {"title": "Software Engineer", "applicants": [{"username": "test_user"}]},
#                 {"title": "Data Analyst", "applicants": [{"username": "another_user"}]},
#                 {"title": "Product Manager", "applicants": [{"username": "test_user"}]},
#             ],
#             ["Software Engineer", "Product Manager"],
#         ),
#         (
#             User("another_user", "password"),
#             [
#                 {"title": "Software Engineer", "applicants": [{"username": "test_user"}]},
#                 {"title": "Data Analyst", "applicants": [{"username": "another_user"}]},
#                 {"title": "Product Manager", "applicants": [{"username": "test_user"}]},
#             ],
#             ["Data Analyst"],
#         ),
#         (
#             User("not_applied_user", "password"),
#             [
#                 {"title": "Software Engineer", "applicants": [{"username": "test_user"}]},
#                 {"title": "Data Analyst", "applicants": [{"username": "another_user"}]},
#                 {"title": "Product Manager", "applicants": [{"username": "test_user"}]},
#             ],
#             [],
#         ),
#     ],
#     ids=[
#         "User has applied to some jobs",
#         "User has applied to one job",
#         "User has not applied to any jobs",
#     ],
# )
# def test_personalApplicationList(user, jobs, expected_output):
#     class JobDatabase:
#         def __init__(self):
#             self.jobs = jobs

#         def getJobListDict(self):
#             return self.jobs

#     assert personalApplicationList(user, JobDatabase()) == expected_output
