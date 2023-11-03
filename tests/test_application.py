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



# TODO test notAppliedList
@pytest.fixture
def user():
    return User("test_user", "password")

@pytest.fixture
def jobs():
    return [
        {"title": "Job 1", "applicants": [{"username": "test_user"}]},
        {"title": "Job 2", "applicants": []},
        {"title": "Job 3", "applicants": [{"username": "other_user"}]},
    ]

@pytest.mark.parametrize(
    "user, jobs, expected_output",
    [
        (User("test_user", "password"), [
            {"title": "Job 1", "applicants": [{"username": "test_user"}]},
            {"title": "Job 2", "applicants": []},
            {"title": "Job 3", "applicants": [{"username": "other_user"}]},
        ], ["Job 2"]),
        (User("other_user", "password"), [
            {"title": "Job 1", "applicants": [{"username": "test_user"}]},
            {"title": "Job 2", "applicants": []},
            {"title": "Job 3", "applicants": [{"username": "other_user"}]},
        ], ["Job 1", "Job 2"]),
        (User("nonexistent_user", "password"), [
            {"title": "Job 1", "applicants": [{"username": "test_user"}]},
            {"title": "Job 2", "applicants": []},
            {"title": "Job 3", "applicants": [{"username": "other_user"}]},
        ], ["Job 1", "Job 2", "Job 3"]),
    ],
    ids=[
        "User has not applied to any jobs",
        "User has applied to some jobs",
        "User does not exist",
    ]
)
def test_notAppliedList(user, jobs, expected_output):
    assert notAppliedList(user) == expected_output




# TODO test personalApplicationList
@pytest.mark.parametrize(
    "user, jobs, expected_output",
    [
        (
            User("test_user", "password"), 
            [
                {"title": "Software Engineer", "applicants": [{"username": "test_user"}]},
                {"title": "Data Analyst", "applicants": [{"username": "another_user"}]},
                {"title": "Product Manager", "applicants": [{"username": "test_user"}]},
            ],
            ["Software Engineer", "Product Manager"]
        ),
        (
            User("another_user", "password"), 
            [
                {"title": "Software Engineer", "applicants": [{"username": "test_user"}]},
                {"title": "Data Analyst", "applicants": [{"username": "another_user"}]},
                {"title": "Product Manager", "applicants": [{"username": "test_user"}]},
            ],
            ["Data Analyst"]
        ),
        (
            User("not_applied_user", "password"), 
            [
                {"title": "Software Engineer", "applicants": [{"username": "test_user"}]},
                {"title": "Data Analyst", "applicants": [{"username": "another_user"}]},
                {"title": "Product Manager", "applicants": [{"username": "test_user"}]},
            ],
            []
        ),
    ],
    ids=[
        "User has applied to some jobs",
        "User has applied to one job",
        "User has not applied to any jobs"
    ]
)
def test_personalApplicationList(user, jobs, expected_output):
    class JobDatabase:
        def __init__(self):
            self.jobs = jobs
        def getJobListDict(self):
            return self.jobs
    
    assert personalApplicationList(user, JobDatabase()) == expected_output