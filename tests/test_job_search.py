import pytest
from pages.new_user_account import saveDatabase
from pages.job_search import printJobSearchScreen, saveJobDatabase, jobOptionsList
from common_utils.messages import anyButtonToContinueMessage, underConstructionMessage
from tests.shared import JSON_USERS_FP, JSON_JOBS_FP, singleUser, fourJobs, fiveJobs


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
                # "Some message about job being created"
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
            singleUser["username"],
        ),
        (
            ["3", "anything"],
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
                'Invalid selection please input "1" or "2" or "3"',
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
    saveDatabase(JSON_USERS_FP, singleUser)
    saveJobDatabase(JSON_JOBS_FP, startingJobDB)
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printJobSearchScreen(singleUser["username"]) == expectedReturn  # Successful search
    except StopIteration:
        pass
    captured = capfd.readouterr()  # assert captured
    for r in responses:
        assert r in captured.out  # Friend successfully added
