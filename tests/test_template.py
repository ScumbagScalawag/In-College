"""
Template for pytests, parametrize is first then a template for indivual tests
Feel free to ask any questions you have on discord
-Zack
"""

import pytest  # needed for pytest
from tests.shared import JSON_USERS_FP, fourAccounts  # needed for testWithDatabaseSet
from common_utils.types.user_database import UserDatabase


def tempFunction():  # Temp function is placeholder for function to be imported from test file
    return


@pytest.mark.parametrize(
    "mock_input,responses,expectedReturn",
    [
        (
            ["", ""],  # mock input
            [
                "",  # responses
                "",
            ],
            None,  # expected return
        ),
        (
            ["1st input", "2nd input"],
            [
                "",
                "",
            ],
            None,
        ),
        (
            [""],
            [
                "",
            ],
            None,
        ),
    ],
    ids=[
        "TempName1",
        "TempName2",
        "TempName3",
    ],
)
def testTempName(mock_input, responses, expectedReturn, monkeypatch, capfd):
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert tempFunction() == expectedReturn
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out


# can be used for individual tests: use case of needing to save a database before hand for a single test
# if multiple tests, can be done with @pytest.mark.parametrize, read documentation on how to change it
# to change paramertize to handle the loading of diffrent databases, make a new variable for them have it be included in the test's function definition NAME(monkeypatch, capfd, ..., NEWVARIABLE)
# look at new_user_account tests and job search tests to see paramertized implementation of it
def testWithDatabaseSet(monkeypatch, capfd):
    userDB = UserDatabase()
    userDB.addUserDictList(fourAccounts)

    input_generator = iter(
        [
            "",  # "input 1",
            "",  # "input 2",
            "",  # "input 3",
        ]
    )
    responses = [
        "",  # "Response 1",
        "",  # "Response 2",
        "",  # "Response 3",
    ]
    expectedReturn = None
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert tempFunction() == expectedReturn  # function == expected return
    except StopIteration:
        pass
    captured = capfd.readouterr()
    # assert captured
    for r in responses:
        assert r in captured.out  # Friend not found in system
