import pytest
from common_utils.utils import saveUserDatabase
from pages.job_search import printJobSearchScreen, saveJobDatabase
from pages.under_construction import underConstructionMessage
from tests.shared import JSON_USERS_FP, JSON_JOBS_FP, singleUser, fourJobs, fiveJobs


@pytest.mark.parametrize(
    "mock_input,responses,startingJobDB,expectedReturn",
    [
        (
            ["1", "anything"],
            [
                "*** Job Search ***",
                "1 - Search for Job/Internship",
                "2 - Post Job/Internship",
                "3 - Return to Main Menu",
                underConstructionMessage(),
            ],
            [],
            [0],
        ),
        (
            ["2", "Code Tester", "Test Code for hours", "Mr. Roth", "Home", "100"],
            [
                "*** Job Search ***",
                "1 - Search for Job/Internship",
                "2 - Post Job/Internship",
                "3 - Return to Main Menu",
                "*** Create a new job posting ***",
                # "Some message about job being created"
            ],
            fourJobs,
            [0],
        ),
        (
            ["2", "anything"],
            [
                "*** Job Search ***",
                "1 - Search for Job/Internship",
                "2 - Post Job/Internship",
                "3 - Return to Main Menu",
                "All permitted jobs have been posted, please try again later",
                "Please press any button to continue",
            ],
            fiveJobs,
            None,
        ),
        (
            ["3", "anything"],
            [
                "*** Job Search ***",
                "1 - Search for Job/Internship",
                "2 - Post Job/Internship",
                "3 - Return to Main Menu",
            ],
            [],
            None,
        ),
        (
            ["4", "3"],
            [
                "*** Job Search ***",
                "1 - Search for Job/Internship",
                "2 - Post Job/Internship",
                "3 - Return to Main Menu",
                'Invalid selection please input "1" or "2" or "3"',
            ],
            [],
            None,
        ),
    ],
    ids=[
        "JobSearchUnderConstruction",
        "CreateJob",
        "MaxJobsReached",
        "ReturnMain",
        "InvalidSelection",
    ],
)
def testJobSearch(mock_input, responses, startingJobDB, expectedReturn, monkeypatch, capfd):
    saveUserDatabase(singleUser)
    saveJobDatabase(startingJobDB)
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printJobSearchScreen(singleUser["username"]) == expectedReturn  # Successful search
    except StopIteration:
        pass
    except TypeError:
        pass
    captured = capfd.readouterr()  # assert captured
    for r in responses:
        assert r in captured.out  # Friend successfully added
