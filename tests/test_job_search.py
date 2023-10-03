import pytest
from pages.job_search import printJobSearchScreen, saveJobDatabase, jobOptionsList
from common_utils.messages import anyButtonToContinueMessage, invalidInput, underConstructionMessage
from tests.shared import JSON_JOBS_FP, singleUser, fourJobs, fiveJobs, fourAccounts
from common_utils.types.user_database import UserDatabase
from common_utils.types.user import User

@pytest.mark.parametrize(
    "mock_input,responses,startingJobDB,expectedReturn",
    [
        (
            ["1", "anything"],
            [
                *jobOptionsList,
                underConstructionMessage(),
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
            fiveJobs,
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
                invalidInput("1, 2, or X")
            ],
            [],
            singleUser["username"],
        ),
    ],
    ids=[
        "1-JobSearchUnderConstruction",
        "2-CreateJob; Currently expected to fail until singleUser variable is fixed",
        "2-MaxJobsReached",
        "3-ReturnMain",
        "InvalidSelection",
    ],
)
def testJobSearch(mock_input, responses, startingJobDB, expectedReturn, monkeypatch, capfd):
    # saveDatabase(JSON_USERS_FP, singleUser)
    testUser = User.dictToUser(singleUser)
    userDB = UserDatabase([])
    userDB.addUserDictList(fourAccounts)

    saveJobDatabase(JSON_JOBS_FP, startingJobDB)
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printJobSearchScreen(testUser) == testUser  # Successful search
    except StopIteration:
        pass
    captured = capfd.readouterr()  # assert captured
    for r in responses:
        assert r in captured.out  # Friend successfully added
