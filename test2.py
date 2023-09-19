import pytest
from main import printNewAccountScreen, saveUser, printMainMenu, printSkillScreen
import json
def testCreateAccountUnder5(monkeypatch, capfd):
    # Make sure Json is clear
    with open("user_file.json", "w") as f:
        f.write("{}")
        # Test with 3 accounts
    accounts = {
        "Tomas": "Valid123!",
        "Carry": "Valid123!",
        "Tools": "Valid123!",
    }
    for username, password in accounts.items():
        saveUser(username, password)
    input_generator = iter(["usernew", "P@ssw0rd", "P@ssw0rd"])
    monkeypatch.setattr('builtins.input', lambda: next(input_generator))
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

def testLoginwithMainMenu(monkeypatch, capfd):
        username = "Andrew"
        password = "Valid123!"
        #Check Json for login
        with open("user_file.json", "w") as f:
            json.dump({username: password}, f)
        #Inputs
        input_generator = iter([username, password, password])
        monkeypatch.setattr('builtins.input', lambda: next(input_generator))
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
    #Setup Inputs
    input_generator = iter(["1"])
    monkeypatch.setattr('builtins.input', lambda: next(input_generator))
    #Run Inputs untill loop
    try:
        printMainMenu()
    except StopIteration:
        pass
    #See if our input gave us our desired output text
    captured = capfd.readouterr()
    assert "under construction, input anything to return" in captured.out
def testFindSomeoneConstruction(monkeypatch, capfd):
    input_generator = iter(["2"])
    monkeypatch.setattr('builtins.input', lambda: next(input_generator))
    try:
        printMainMenu()
    except StopIteration:
        pass

    captured = capfd.readouterr()
    assert "under construction, input anything to return" in captured.out

@pytest.mark.parametrize("input_value", ["1", "2", "3", "4", "5"])
def testSkillsUnderConstruction(input_value, monkeypatch, capfd):
    input_generator = iter([input_value])
    monkeypatch.setattr('builtins.input', lambda: next(input_generator))

    try:
        printSkillScreen()
    except StopIteration:
        pass

    captured = capfd.readouterr()
    assert "under construction, input anything to return" in captured.out

def testSkillsReturnButton(monkeypatch, capfd):
    input_generator = iter(["6"])
    monkeypatch.setattr('builtins.input', lambda: next(input_generator))
    try:
        printSkillScreen()
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
@pytest.mark.parametrize("input_value", ["9", "0", "[1", "d", "r"])
def testSkillsWrongInput(input_value, monkeypatch, capfd):
    input_generator = iter([input_value])
    monkeypatch.setattr('builtins.input', lambda: next(input_generator))

    try:
        printSkillScreen()
    except StopIteration:
        pass

    captured = capfd.readouterr()
    assert "Invalid selection please input \"1\" or \"2\" or \"3\" or \"4\" or \"5\" or \"6\"" in captured.out

