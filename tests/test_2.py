import pytest
from pages.new_user_account import printNewAccountScreen
from pages.main_menu import printMainMenu
from pages.skill_search import printSkillScreen
from pages.new_user_account import saveDatabase
from tests.shared import JSONFP2
import json


def testCreateAccountUnder5(monkeypatch, capfd):
    # Make sure Json is clear
    # Test with 3 accounts
    threeAccounts = [
        {
            "username": "dummy",
            "password": "Password1!",
            "firstname": "Jo",
            "lastname": "Mama",
            "connections": [],
        },
        {
            "username": "sillyBoi",
            "password": "Password2@",
            "firstname": "Dee",
            "lastname": "Snuts",
            "connections": ["notKaren", "dummy"],
        },
        {
            "username": "dummyDude",
            "password": "Password2@",
            "firstname": "Dee",
            "lastname": "Snuts",
            "connections": ["admin"],
        },
    ]
    saveDatabase(JSONFP2, threeAccounts)

    input_generator = iter(["usernew", "Johnathan", "Blow", "P@ssw0rd", "P@ssw0rd"])
    monkeypatch.setattr("builtins.input", lambda: next(input_generator))

    try:
        printNewAccountScreen()
    except StopIteration:
        pass
    captured = capfd.readouterr()

    title = "*** Create a new user account ***\n"
    firstname = "First name:"
    lastname = "Last name:"
    username = "Username:"
    password = "Password:"

    # Better approach than whole-sale output assertions
    assert title in captured.out
    assert firstname in captured.out
    assert lastname in captured.out
    assert username in captured.out
    assert password in captured.out


def testLoginwithMainMenu(monkeypatch, capfd):
    username = "Andrew"
    password = "Valid123!"
    # Check Json for login
    with open("user_file.json", "w") as f:
        json.dump({username: password}, f)
    # Inputs
    input_generator = iter([username, password, password])
    monkeypatch.setattr("builtins.input", lambda: next(input_generator))
    try:
        printNewAccountScreen()
    except StopIteration:
        pass
    captured = capfd.readouterr()
    main_menu = (
        "*** Main Menu ***\n"
        "1 - Search for a job\n"
        "2 - Find someone that you know\n"
        "3 - Learn a skill\n"
    )
    assert main_menu in captured.out


def testJobUnderConstruction(monkeypatch, capfd):
    # Setup Inputs
    input_generator = iter(["1"])
    monkeypatch.setattr("builtins.input", lambda: next(input_generator))
    # Run Inputs untill loop
    try:
        printMainMenu()
    except StopIteration:
        pass
    # See if our input gave us our desired output text
    captured = capfd.readouterr()
    assert "under construction, input anything to return" in captured.out


def testFindSomeoneConstruction(monkeypatch, capfd):
    input_generator = iter(["2"])
    monkeypatch.setattr("builtins.input", lambda: next(input_generator))
    try:
        printMainMenu()
    except StopIteration:
        pass

    captured = capfd.readouterr()
    assert "under construction, input anything to return" in captured.out


@pytest.mark.parametrize("input_value", ["1", "2", "3", "4", "5"])
def testSkillsUnderConstruction(input_value, monkeypatch, capfd):
    input_generator = iter([input_value])
    monkeypatch.setattr("builtins.input", lambda: next(input_generator))

    try:
        printSkillScreen()
    except StopIteration:
        pass

    captured = capfd.readouterr()
    assert "under construction, input anything to return" in captured.out


# def testSkillsReturnButton(monkeypatch, capfd):
#     input_generator = iter(["6"])
#     monkeypatch.setattr("builtins.input", lambda: next(input_generator))
#     try:
#         printSkillScreen()
#     except StopIteration:
#         pass
#     captured = capfd.readouterr()

#     title = "*** Main Menu ***"
#     job = "1 - Search for a job"
#     findSomeone = "2 - Find someone that you know"
#     skill = "3 - Learn a skill"

#     assert title in captured.out
#     assert job in captured.out
#     assert findSomeone in captured.out
#     assert skill in captured.out


@pytest.mark.parametrize("input_value", ["9", "0", "[1", "d", "r"])
def testSkillsWrongInput(input_value, monkeypatch, capfd):
    input_generator = iter([input_value])
    monkeypatch.setattr("builtins.input", lambda: next(input_generator))

    try:
        printSkillScreen()
    except StopIteration:
        pass

    captured = capfd.readouterr()
    assert 'Invalid selection please input "1" or "2" or "3" or "4" or "5" or "6"' in captured.out
