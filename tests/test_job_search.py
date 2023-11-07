import pytest
from pages.job_search import (
    printJobSearchScreen,
    jobOptionsList,
    printJobOptionScreen,
    jobListingChoices,
)
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
            ["3", "anything"],
            [
                *jobOptionsList,
                "*** Saved Jobs ***",
                anyButtonToContinueMessage(),
            ],
            [],
            singleUser,
        ),
        (
            ["4", "3"],
            [
                *jobOptionsList,
                "*** Application List ***",
                "Software Engineer",
                anyButtonToContinueMessage(),
            ],
            fourJobs,
            singleUser,
        ),
        (
            ["5", "anything"],
            [
                *jobOptionsList,
                "*** List of Jobs Not Applied To ***",
                "Data Analyst",
                "Potato Masher",
                "Magician",
                anyButtonToContinueMessage(),
            ],
            fourJobs,
            singleUser,
        ),
        (
            ["6", "X"],
            [
                *jobOptionsList,
                "*** Delete Job ***",
                "Job does not exist",
            ],
            fourJobs,
            singleUser,
        ),
        (
            ["Foam Earplugs", "X"],
            [
                *jobOptionsList,
                invalidInput("Please select a valid option"),
                anyButtonToContinueMessage(),
            ],
            fourJobs,
            singleUser,
        ),
        (
            ["X"],
            [
                *jobOptionsList,
            ],
            fourJobs,
            singleUser,
        ),
    ],
    ids=[
        "1-JobSearch",
        "2-CreateJob",
        "2-MaxJobsReached",
        "3-PrintSavedJobs",
        "4-ViewApplications",
        "5-NotAppliedList",
        "6-DeleteJob",
        "InvalidInput",
        "X-ReturnToMainMenu",
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


# temp test to test jobSearch
def testJobSearch(monkeypatch, capfd):
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


def testDeleteJob(monkeypatch, capfd):
    # in system
    userDB = UserDatabase([])
    jobDB = JobDatabase()
    jobDB.addJobDictList(fiveJobs)
    userDB.addUserDictList(fourAccounts)
    # Must create User object from singleUser Dict. See @classmethod dictToUser
    testUser = User.dictToUser(singleUser)

    input_generator = iter(
        [
            "6",
            "Pokemon Trainer",
        ]
    )  # Make it choose to remove friend here
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert (
            printJobSearchScreen(testUser) == testUser
        )  # assert printFriendsScreen returns user context correctly
        assert jobDB.getJobListDict() == fourJobs
    except StopIteration:
        pass
    captured = capfd.readouterr()  # assert captured
    responses = [
        *jobOptionsList,
        "*** Delete Job ***",
        "Title: Pokemon Trainer",
        "Description: Capture, train, and battle with a team of Pokemon",
        "-------------------------",
        "Job deleted successfully",
        anyButtonToContinueMessage(),
    ]
    for r in responses:
        assert r in captured.out


def testPrintJobOptionScreen_ApplyToJob(monkeypatch, capfd):
    # in system
    userDB = UserDatabase([])
    jobDB = JobDatabase()
    jobsToEdit = fiveJobs[:]
    jobsToEdit[0]["firstname"] = "Bojangle"
    jobsToEdit[0]["lastname"] = "McGee"
    # Give us something to apply to
    jobDB.addJobDictList(jobsToEdit)
    userDB.addUserDictList(fourAccounts)
    # Must create User object from singleUser Dict. See @classmethod dictToUser
    testUser = User.dictToUser(singleUser)

    input_generator = iter(
        [
            "1",
            "01/01/2020",
            "02/01/2020",
            "I am fit",
            "Foam Earplugs",
            "X",
        ]
    )  # Make it choose to remove friend here
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert (
            printJobOptionScreen(0, testUser) == testUser
        )  # assert printFriendsScreen returns user context correctly
        jobDB.loadJobs()
        assert jobDB.getJobListDict()[0]["applicants"][0]["username"] == singleUser["username"]
    except StopIteration:
        pass

    captured = capfd.readouterr()  # assert captured
    responses = [
        *jobListingChoices,
        "*** Job Application ***",
        "Application sucessfully submitted",
    ]

    for r in responses:
        assert r in captured.out


def testPrintJobOptionScreen_CreateSavedJob(monkeypatch, capfd):
    # in system
    userDB = UserDatabase([])
    jobDB = JobDatabase()
    jobDB.addJobDictList(fourJobs)
    userDB.addUserDictList(fourAccounts)
    # Must create User object from singleUser Dict. See @classmethod dictToUser
    testUser = User.dictToUser(singleUser)

    input_generator = iter(
        [
            "1",
            "X",
        ]
    )  # Make it choose to remove friend here
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert (
            printJobOptionScreen(testUser) == testUser
        )  # assert printFriendsScreen returns user context correctly
    except StopIteration:
        pass

    captured = capfd.readouterr()  # assert captured
    responses = [
        *jobListingChoices,
        "Current Open Positions:",
    ]

    for r in responses:
        assert r in captured.out


def testPrintJobOptionScreen_CreateDeleteSavedJob(monkeypatch, capfd):
    # in system
    userDB = UserDatabase([])
    jobDB = JobDatabase()
    jobDB.addJobDictList(fourJobs)
    userDB.addUserDictList(fourAccounts)
    # Must create User object from singleUser Dict. See @classmethod dictToUser
    testUser = User.dictToUser(singleUser)

    input_generator = iter(
        [
            "1",
            "X",
        ]
    )  # Make it choose to remove friend here
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert (
            printJobOptionScreen(testUser) == testUser
        )  # assert printFriendsScreen returns user context correctly
    except StopIteration:
        pass

    captured = capfd.readouterr()  # assert captured
    responses = [
        *jobListingChoices,
        "Current Open Positions:",
    ]

    for r in responses:
        assert r in captured.out
