import pytest
from pages.job_search import printJobSearchScreen, jobOptionsList
from common_utils.messages import anyButtonToContinueMessage, invalidInput, underConstructionMessage
from tests.shared import JSON_JOBS_FP, singleUser, fourJobs, fiveJobs, fourAccounts, tenJobs
from common_utils.types.user_database import UserDatabase
from common_utils.types.job_database import JobDatabase
from common_utils.types.user import User


@pytest.mark.parametrize(
    "mock_input,responses,startingJobDB,expectedReturn",
    [
        (
            ["1", "X"],
            [
                *jobOptionsList,
                "Current Open Positions:",
            ],
            [],
            [0],
        ),
        (
            ["2", "Code Tester", "Test Code for hours", "Mr. Roth", "Home", "100"],
            [
                *jobOptionsList,
                "*** Create a new job posting ***",
                "Job Created!",
            ],
            fourJobs,
            None,
        ),
        (
            ["2", "anything"],
            [
                *jobOptionsList,
                "All permitted jobs have been posted, please try again later",
                anyButtonToContinueMessage(),
            ],
            tenJobs,
            singleUser,
        ),
        (
            ["X", "anything"],
            [
                *jobOptionsList,
            ],
            [],
            singleUser["username"],
        ),
        (
            ["4", "3"],
            [
                *jobOptionsList,
                invalidInput("1, 2, or X"),
            ],
            [],
            singleUser["username"],
        ),
    ],
    ids=[
        "1-JobSearch",
        "2-CreateJob",
        "2-MaxJobsReached",
        "3-ReturnMain",
        "InvalidSelection",
    ],
)
def testJobSearch(mock_input, responses, startingJobDB, expectedReturn, monkeypatch, capfd):
    # saveDatabase(JSON_USERS_FP, singleUser)
    testUser = User.dictToUser(singleUser)
    userDB = UserDatabase([])
    userDB.addUserDictList(fourAccounts)  # users

    jobDB = JobDatabase()
    jobDB.addJobDictList(startingJobDB)  # jobs
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printJobSearchScreen(testUser) == testUser  # Successful search
    except StopIteration:
        pass
    captured = capfd.readouterr()  # assert captured
    for r in responses:
        assert r in captured.out  # Friend successfully added


# TODO: FIX TESTS FOR JOB SEARCH
# 2. CreateJob
# 2. MaxJobsReached
# 3. printSavedJobs
# 4. Application List
# 5. not applied list
# 6. delete job
# 7. invalid selection
# X. Return to Main Menu


# Application Deleted
# temp test to test jobSearch
def test_jobSearch(monkeypatch, capfd):
    userDB = UserDatabase([])
    jobDB = JobDatabase()
    jobDB.addJobDictList(fourJobs)
    userDB.addUserDictList(fourAccounts)
    # Must create User object from singleUser Dict. See @classmethod dictToUser
    testUser = userDB.getUser(singleUser["username"])

    input_generator = iter(
        [
            "1",
            "X",
        ]
    )  # Make it choose to remove friend here
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert (
            printJobSearchScreen(testUser) == testUser
        )  # assert printFriendsScreen returns user context correctly
    except StopIteration:
        pass

    captured = capfd.readouterr()  # assert captured
    responses = [
        *jobOptionsList,
        "Current Open Positions:",
    ]

    for r in responses:
        assert r in captured.out
