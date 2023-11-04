from common_utils.types.user import User
from tests.shared import singleUser, fourAccounts
from pages.friend_search import (
    printFriendSearchScreen,
    friendSearchOptionList,
)  # Search Screen here to preload database
from common_utils.types.user_database import UserDatabase
import pytest


@pytest.fixture
def user_db():
    userDB = UserDatabase([])
    userDB.addUserDictList(fourAccounts)
    return userDB


@pytest.mark.parametrize(
    "mock_input, responses",
    [
        (
            ["Dee", "Snuts", "2", "Y", "X"],
            [
                *friendSearchOptionList,
                "is part of the InCollege system",
            ],
        ),
        (
            ["Jo", "Mama", "Y", "X"],
            [
                *friendSearchOptionList,
                "is part of the InCollege system",
                "Connection request sent",
            ],
        ),
        (
            ["Foam", "Earplugs", "Y", "X"],
            [
                *friendSearchOptionList,
                "They are not yet a part of the InCollege system yet",
            ],
        ),
        (
            ["Dee", "Snuts", "2", "x"],
        )
    ],
    ids=["Found User multiple", "Found User single", "Not Found User"],
)
def test_print_friend_search_screen_in_system(monkeypatch, capfd, mock_input, responses):
    # in system
    testUser = User.dictToUser(singleUser)
    userDB = UserDatabase([])
    userDB.addUserDictList(fourAccounts)
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert printFriendSearchScreen(testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()  # assert captured
    for r in responses:
        assert r in captured.out  # Friend successfully added


# @pytest.mark.parametrize(
#     "input_str, expected_output",
#     [
#         (["Dee", "Snuts", "2", "Y", "X"], singleUser),
#         ("Foam\nEarplugs\nY\nX\n", None),
#     ],
# )
# def test_print_friend_search_screen_not_in_system(
#     monkeypatch, capfd, user_db, input_str, expected_output
# ):
#     testUser = User.dictToUser(singleUser)

#     # Not in system
#     input_generator = iter(input_str.split())
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

#     assert printFriendSearchScreen(testUser, user_db) == expected_output

#     captured = capfd.readouterr()
#     # assert captured
#     responses = [
#         *friendSearchOptionList,
#         "They are not yet a part of the InCollege system yet",
#     ]
#     for r in responses:
#         assert r in captured.out  # Friend not found in system


# @pytest.mark.parametrize(
#     "input_str, expected_output",
#     [
#         ("Jo\nMama\nY\nX\n", None),
#     ],
# )
# def test_print_friend_search_screen_not_logged_in(
#     monkeypatch, capfd, user_db, input_str, expected_output
# ):
#     input_generator = iter(input_str.split())
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

#     assert printFriendSearchScreen(None, user_db) == expected_output

#     captured = capfd.readouterr()
#     assert captured.out == ""


# @pytest.mark.parametrize(
#     "input_str, expected_output",
#     [
#         ("Dee\nSnuts\n2\nY\nX\n", singleUser),
#     ],
# )
# def test_print_friend_search_screen_by_major(
#     monkeypatch, capfd, user_db, input_str, expected_output
# ):
#     testUser = User.dictToUser(singleUser)

#     input_generator = iter(input_str.split())
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

#     assert printFriendSearchScreen(testUser, user_db) == expected_output

#     captured = capfd.readouterr()
#     responses = [
#         *friendSearchOptionList,
#         "part of the InCollege system",
#         "Connection request sent",
#     ]
#     for r in responses:
#         assert r in captured.out  # Friend successfully added


# def testPrintFriendSearchScreen_InSystem(monkeypatch, capfd):
#     # in system
#     userDB = UserDatabase([])
#     userDB.addUserDictList(fourAccounts)

#     # Must create User object from singleUser Dict. See @classmethod dictToUser
#     testUser = User.dictToUser(singleUser)

#     input_generator = iter(["Dee", "Snuts", "2", "Y", "X"])
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

#     try:
#         assert (
#             printFriendSearchScreen(testUser) == testUser
#         )  # assert printFriendSearchScreen returns user context correctly
#     except StopIteration:
#         pass

#     captured = capfd.readouterr()  # assert captured
#     responses = [
#         *friendSearchOptionList,
#         "part of the InCollege system",
#         "Connection request sent",
#     ]
#     for r in responses:
#         assert r in captured.out  # Friend successfully added

#     # print(captured.out)


# def testFriendSearchNotInSystem(monkeypatch, capfd):
#     userDB = UserDatabase([])
#     userDB.addUserDictList(fourAccounts)
#     testUser = User.dictToUser(singleUser)

#     # Not in system
#     input_generator = iter(
#         [
#             "Foam",
#             "Earplugs",
#             "Y",
#             "X",
#         ]  # Y is not used will cause it to ask for input again of X or C
#     )  # Note: Do not add a user "Foam Earplugs" into the test cases or this will not work as intended
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
#     try:
#         assert (
#             printFriendSearchScreen(testUser) == testUser
#         )  # Make sure printFriendSearchScreen returns user context
#     except StopIteration:
#         pass
#     captured = capfd.readouterr()
#     # assert captured
#     responses = [
#         *friendSearchOptionList,
#         "They are not yet a part of the InCollege system yet",
#     ]
#     for r in responses:
#         assert r in captured.out  # Friend not found in system


# # TODO Needs fixing of both logic and test
# # User not logged in handled with return to -1
# def testFriendSearchNotLoggedIn(monkeypatch, capfd):
#     userDB = UserDatabase([])
#     userDB.addUserDictList(fourAccounts)
#     input_generator = iter(
#         [
#             "Jo",
#             "Mama",
#             "Y",
#             "X",
#         ]  # Y is not used will cause it to ask for input again of X or C
#     )
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
#     try:
#         assert (
#             printFriendSearchScreen() == None
#         )  # Tests edge cases of not logged in: ...() defaults to None
#     except StopIteration:
#         pass


# def testFriendSearchByMajor(monkeypatch, capfd):
#     # in system
#     userDB = UserDatabase([])
#     userDB.addUserDictList(fourAccounts)

#     # Must create User object from singleUser Dict. See @classmethod dictToUser
#     testUser = User.dictToUser(singleUser)

#     input_generator = iter(["2", "cs", "2", "Y", "X"])
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

#     try:
#         assert (
#             printFriendSearchScreen(testUser) == testUser
#         )  # assert printFriendSearchScreen returns user context correctly
#     except StopIteration:
#         pass

#     captured = capfd.readouterr()  # assert captured
#     responses = [
#         *friendSearchOptionList,
#         "part of the InCollege system",
#         "Connection request sent",
#     ]
#     for r in responses:
#         assert r in captured.out  # Friend successfully added


# def testFriendSearchByUniversity(monkeypatch, capfd):
#     # in system
#     userDB = UserDatabase([])
#     userDB.addUserDictList(fourAccounts)

#     # Must create User object from singleUser Dict. See @classmethod dictToUser
#     testUser = User.dictToUser(singleUser)

#     input_generator = iter(["3", "usf", "2", "Y", "X"])
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

#     try:
#         assert (
#             printFriendSearchScreen(testUser) == testUser
#         )  # assert printFriendSearchScreen returns user context correctly
#     except StopIteration:
#         pass

#     captured = capfd.readouterr()  # assert captured
#     responses = [
#         *friendSearchOptionList,
#         "part of the InCollege system",
#         "Connection request sent",
#     ]
#     for r in responses:
#         assert r in captured.out  # Friend successfully added


# def test_printFriendSearchScreen_foundUser(monkeypatch, capfd):
#     # in system
#     userDB = UserDatabase([])
#     userDB.addUserDictList(fourAccounts)

#     # Must create User object from singleUser Dict. See @classmethod dictToUser
#     testUser = User.dictToUser(singleUser)

#     input_generator = iter(["Dee", "Snuts", "2", "Y", "X"])
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

#     assert printFriendSearchScreen(testUser) == testUser

#     captured = capfd.readouterr()
#     responses = [
#         *friendSearchOptionList,
#         "part of the InCollege system",
#         "Connection request sent",
#     ]
#     for r in responses:
#         assert r in captured.out


# def test_printFriendSearchScreen_notFoundUser(monkeypatch, capfd):
#     userDB = UserDatabase([])
#     userDB.addUserDictList(fourAccounts)
#     testUser = User.dictToUser(singleUser)

#     # Not in system
#     input_generator = iter(
#         [
#             "Foam",
#             "Earplugs",
#             "Y",
#             "X",
#         ]  # Y is not used will cause it to ask for input again of X or C
#     )  # Note: Do not add a user "Foam Earplugs" into the test cases or this will not work as intended
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

#     assert printFriendSearchScreen(testUser) == testUser

#     captured = capfd.readouterr()
#     responses = [
#         *friendSearchOptionList,
#         "They are not yet a part of the InCollege system yet",
#     ]
#     for r in responses:
#         assert r in captured.out


# def test_printFriendSearchScreen_cancel(monkeypatch, capfd):
#     userDB = UserDatabase([])
#     userDB.addUserDictList(fourAccounts)
#     testUser = User.dictToUser(singleUser)

#     # Not in system
#     input_generator = iter(
#         [
#             "Dee",
#             "Snuts",
#             "2",
#             "x",
#         ]  # x is used to cancel the search
#     )
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

#     assert printFriendSearchScreen(testUser) == testUser

#     captured = capfd.readouterr()
#     responses = [
#         *friendSearchOptionList,
#         "Input c to continue or x to return to menu",
#     ]
#     for r in responses:
#         assert r in captured.out


# def test_printFriendSearchScreen_invalidSelection(monkeypatch, capfd):
#     userDB = UserDatabase([])
#     userDB.addUserDictList(fourAccounts)
#     testUser = User.dictToUser(singleUser)

#     # Not in system
#     input_generator = iter(
#         [
#             "Dee",
#             "Snuts",
#             "2",
#             "5",
#             "x",
#         ]  # 5 is an invalid selection
#     )
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

#     assert printFriendSearchScreen(testUser) == testUser

#     captured = capfd.readouterr()
#     responses = [
#         *friendSearchOptionList,
#         "Invalid selection. Please choose a number from the list.",
#     ]
#     for r in responses:
#         assert r in captured.out


# def test_printFriendSearchScreen_notLoggedIn(monkeypatch, capfd):
#     userDB = UserDatabase([])
#     userDB.addUserDictList(fourAccounts)

#     input_generator = iter(
#         [
#             "Jo",
#             "Mama",
#             "Y",
#             "X",
#         ]  # Y is not used will cause it to ask for input again of X or C
#     )
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

#     assert printFriendSearchScreen() is None


# def test_printFriendSearchScreen_searchByMajor(monkeypatch, capfd):
#     # in system
#     userDB = UserDatabase([])
#     userDB.addUserDictList(fourAccounts)

#     # Must create User object from singleUser Dict. See @classmethod dictToUser
#     testUser = User.dictToUser(singleUser)

#     input_generator = iter(["2", "cs", "2", "Y", "X"])
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

#     assert printFriendSearchScreen(testUser) == testUser

#     captured = capfd.readouterr()
#     responses = [
#         *friendSearchOptionList,
#         "part of the InCollege system",
#         "Connection request sent",
#     ]
#     for r in responses:
#         assert r in captured.out


# def test_printFriendSearchScreen_searchByUniversity(monkeypatch, capfd):
#     # in system
#     userDB = UserDatabase([])
#     userDB.addUserDictList(fourAccounts)

#     # Must create User object from singleUser Dict. See @classmethod dictToUser
#     testUser = User.dictToUser(singleUser)

#     input_generator = iter(["3", "usf", "2", "Y", "X"])
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

#     assert printFriendSearchScreen(testUser) == testUser

#     captured = capfd.readouterr()
#     responses = [
#         *friendSearchOptionList,
#         "part of the InCollege system",
#         "Connection request sent",
#     ]
#     for r in responses:
#         assert r in captured.out
