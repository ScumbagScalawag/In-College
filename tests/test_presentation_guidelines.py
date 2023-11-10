import pytest
from pages.initial_screen import printInitialScreen, initialScreenOptionsList
from pages.friend_search import friendSearchOptionList
from pages.job_search import jobOptionsList
from pages.important_links import importantLinksOptionsList
from pages.languages import languageLoggedInOptions
from common_utils.types.user_database import UserDatabase
from common_utils.types.user import User
from common_utils.types.job_database import JobDatabase
from common_utils.utils import anyButtonToContinueMessage
from tests.shared import singleUser, fourAccounts, fourJobs


# Tests for the following
# The ability to search for an InCollege user before logging in
def test_search_for_user_before_login(monkeypatch, capfd):
    user_db = UserDatabase([])
    user_db.addUserDictList(fourAccounts)
    mock_input = [
        "Foam Earplugs",
        "3",
        "Noah",
        "McIvor",  # Search by last name
    ]
    responses = [
        *initialScreenOptionsList,
        *friendSearchOptionList,
        "Noah McIvor is part of the InCollege system",
        "You must be logged in to make a connection",
    ]
    expectedReturn = None

    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert printInitialScreen() == expectedReturn
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
    pass


# Creation of a new user account
def test_create_new_user_account(monkeypatch, capfd):
    user_db = UserDatabase([])
    user_db.addUserDictList(fourAccounts)
    mock_input = [
        "Foam Earplugs",
        "2",
        "zackzack38",
        "Zack",
        "Levi",
        "USF",
        "CS",
        "Password1!",
        "Password1!",
        "N",
        "X",
    ]
    responses = [
        *initialScreenOptionsList,
        "*** Create a new user account ***",
        "Username: ",
        "First name: ",
        "Last name: ",
        "University: ",
        "Major: ",
        "Password: ",
        "Exiting InCollege",
    ]
    expectedReturn = User("zackzack38", "Password1!", "Zack", "Levi", "USF", "CS", False)
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert printInitialScreen() == expectedReturn  # == doesnt really work here good enough
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
    pass


# Ability to post a job
def test_post_job(monkeypatch, capfd):
    user_db = UserDatabase([])
    user_db.addUserDictList(fourAccounts)
    test_user = User.dictToUser(singleUser)  # log in user
    job_db = JobDatabase([])
    job_db.addJobDictList(fourJobs)
    mock_input = [
        "Foam Earplugs",
        "7",
        "2",
        "ASSISTANT PROFESSOR OF INSTRUCTION",
        "Lecturer",
        "Dr. Jim Anderson",
        "ENG 215",
        "Not Enough",
        "Foam Earplugs",
        "X",
        "X",
    ]
    responses = [
        *initialScreenOptionsList,
        *jobOptionsList,
        "*** Post a Job/Internship ***",
        "*** Create a new job posting ***",
        anyButtonToContinueMessage(),
        "Exiting InCollege",
    ]
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert printInitialScreen(test_user) == test_user  # == doesnt really work here good enough
    except StopIteration:
        pass
    job_db.loadJobs()
    assert job_db.jobExists("ASSISTANT PROFESSOR OF INSTRUCTION")
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
    pass


# The ability to switch between English and Spanish
def test_language_switch(monkeypatch, capfd):
    user_db = UserDatabase([])
    user_db.addUserDictList(fourAccounts)
    test_user = User.dictToUser(singleUser)  # log in user

    mock_input = [
        "Foam Earplugs",
        "5",
        "10",
    ]
    responses = [
        *initialScreenOptionsList,
        *importantLinksOptionsList,
        *languageLoggedInOptions,
        f"Your current language is {test_user.language}",
        "Exiting InCollege",
    ]
    mock_input1 = mock_input + ["2", "X", "X", "X"]
    input_generator = iter(mock_input1)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert printInitialScreen(test_user) == test_user  # == doesnt really work here good enough
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
    assert test_user.language == "Spanish"
    mock_input2 = mock_input + ["1", "X", "X", "X"]
    input_generator = iter(mock_input2)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printInitialScreen(test_user) == test_user  # == doesnt really work here good enough
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
    assert test_user.language == "English"


# The ability to request to connect with a friend. Have the request accepted. Show a list of friends.
# Creation of a user profile
# Display profile of a friend
# Display a posted job
# Apply for a job
# See a list of jobs that have been applied for
# See a list of jobs that have been “saved”
# Show that a plus user can message anyone and a standard user can only message friends
# Show notification of a message from another student
# Show notification of a new job being posted
# Show notification of a new user joining the InCollege system
# def test_search_for_user_before_login(monkeypatch, capfd):
#     mock_input = [""]
#     responses = [""]
#     expectedReturn = None

#     input_generator = iter(mock_input)
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

#     try:
#         assert printInitialScreen() == expectedReturn
#     except StopIteration:
#         pass
#     captured = capfd.readouterr()
#     for r in responses:
#         assert r in captured.out
#     pass
