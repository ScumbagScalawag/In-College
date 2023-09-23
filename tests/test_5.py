import pytest
from pages.new_user_account import saveDatabase
from pages.job_search import printJobSearchScreen, saveJobDatabase
import json
from tests.shared import JSONFP2, JSONFPJ, singleUser

# TODO move into some shared testing utils
singleJob = {
    "title": "Chocolate Taster",
    "description": "Test Chocolate",
    "employer": "Hershey Chocolate Company",
    "location": "Hershey, Pennsylvania",
    "salary": "1",
    "firstname": "Noah",
    "lastname": "McIvor",
}
fourJobs = [
    {
        "title": "Software Engineer",
        "description": "Developing software applications",
        "employer": "Company A",
        "location": "San Francisco, CA",
        "salary": "90000",
        "firstname": "Noah",
        "lastname": "McIvor",
    },
    {
        "title": "Data Analyst",
        "description": "Analyzing data and generating reports",
        "employer": "Data Analytics Inc.",
        "location": "New York, NY",
        "salary": "75000",
        "firstname": "Noah",
        "lastname": "McIvor",
    },
    {
        "title": "Potato Masher",
        "description": "Mashes potatos and mixes in butter",
        "employer": "JP Morgan",
        "location": "Miami, FL",
        "salary": "1000000",
        "firstname": "Noah",
        "lastname": "McIvor",
    },
    {
        "title": "Magician",
        "description": "Maintain linux servers",
        "employer": "Amazon",
        "location": "Miami, OH",
        "salary": "275000",
        "firstname": "Noah",
        "lastname": "McIvor",
    },
]  # Used to check when under maximum number of jobs

fiveJobs = [
    {
        "title": "Software Engineer",
        "description": "Developing software applications",
        "employer": "Company A",
        "location": "San Francisco, CA",
        "salary": "90000",
        "firstname": "Noah",
        "lastname": "McIvor",
    },
    {
        "title": "Data Analyst",
        "description": "Analyzing data and generating reports",
        "employer": "Data Analytics Inc.",
        "location": "New York, NY",
        "salary": "75000",
        "firstname": "Noah",
        "lastname": "McIvor",
    },
    {
        "title": "Potato Masher",
        "description": "Mashes potatos and mixes in butter",
        "employer": "JP Morgan",
        "location": "Miami, FL",
        "salary": "1000000",
        "firstname": "Noah",
        "lastname": "McIvor",
    },
    {
        "title": "Magician",
        "description": "Maintain linux servers",
        "employer": "Amazon",
        "location": "Miami, OH",
        "salary": "275000",
        "firstname": "Noah",
        "lastname": "McIvor",
    },
    {
        "title": "Pokemon Trainer",
        "description": "Capture, train, and battle with a team of Pokemon",
        "employer": "Professor Oak",
        "location": "Pallet Town, KA",
        "salary": "0",
        "firstname": "Noah",
        "lastname": "McIvor",
    },
]  # Used to test over maximum number of jobs


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
                "under construction, input anything to return",
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
            [-1],
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
            [0],
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
            [0],
        ),
    ],
)
def testJobSearch(mock_input, responses, startingJobDB, expectedReturn, monkeypatch, capfd):
    saveDatabase(JSONFP2, singleUser)
    saveJobDatabase(JSONFPJ, startingJobDB)
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printJobSearchScreen(singleUser["username"]) == expectedReturn  # Successful search
    except StopIteration:
        pass
    captured = capfd.readouterr()  # assert captured
    for r in responses:
        assert r in captured.out  # Friend successfully added
