import pytest
from pages.initial_screen import printInitialScreen, initialScreenOptionsList
from pages.friend_search import friendSearchOptionList
from common_utils.types.user_database import UserDatabase
from common_utils.types.user import User
from tests.shared import singleUser, fourAccounts


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
# Ability to post a job
# The ability to switch between English and Spanish
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
