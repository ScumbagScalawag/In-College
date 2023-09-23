import pytest
from pages.skill_search import printSkillScreen
from pages.new_user_account import saveDatabase
from tests.shared import JSONFP2
import json


@pytest.mark.parametrize(
    "mock_input,responses,expectedReturn",
    [
        (
            ["1", "anything"],
            [
                "*** Learn a skill ***",
                "1 - Learn how to skate",
                "2 - Learn how to cook",
                "3 - Learn how to drive",
                "4 - Learn how to paint",
                "5 - Learn how to whistle",
                "6 - Return to main menu",
                "*** Learn ",
                "under construction, input anything to return",
            ],
            None,
        ),
        (
            ["2", "anything"],
            [
                "*** Learn a skill ***",
                "1 - Learn how to skate",
                "2 - Learn how to cook",
                "3 - Learn how to drive",
                "4 - Learn how to paint",
                "5 - Learn how to whistle",
                "6 - Return to main menu",
                "*** Learn ",
                "under construction, input anything to return",
            ],
            None,
        ),
        (
            ["3", "anything"],
            [
                "*** Learn a skill ***",
                "1 - Learn how to skate",
                "2 - Learn how to cook",
                "3 - Learn how to drive",
                "4 - Learn how to paint",
                "5 - Learn how to whistle",
                "6 - Return to main menu",
                "*** Learn ",
                "under construction, input anything to return",
            ],
            None,
        ),
        (
            ["4", "anything"],
            [
                "*** Learn a skill ***",
                "1 - Learn how to skate",
                "2 - Learn how to cook",
                "3 - Learn how to drive",
                "4 - Learn how to paint",
                "5 - Learn how to whistle",
                "6 - Return to main menu",
                "*** Learn ",
                "under construction, input anything to return",
            ],
            None,
        ),
        (
            ["5", "anything"],
            [
                "*** Learn a skill ***",
                "1 - Learn how to skate",
                "2 - Learn how to cook",
                "3 - Learn how to drive",
                "4 - Learn how to paint",
                "5 - Learn how to whistle",
                "6 - Return to main menu",
                "*** Learn ",
                "under construction, input anything to return",
            ],
            None,
        ),
        (
            ["6"],
            [
                "*** Learn a skill ***",
                "1 - Learn how to skate",
                "2 - Learn how to cook",
                "3 - Learn how to drive",
                "4 - Learn how to paint",
                "5 - Learn how to whistle",
                "6 - Return to main menu",
            ],
            0,
        ),
        (
            ["FoamEarplugs"],
            [
                "*** Learn a skill ***",
                "1 - Learn how to skate",
                "2 - Learn how to cook",
                "3 - Learn how to drive",
                "4 - Learn how to paint",
                "5 - Learn how to whistle",
                "6 - Return to main menu",
                'Invalid selection please input "1" or "2" or "3" or "4" or "5" or "6"',
            ],
            0,
        ),
    ],
    ids=["1-Skill", "2-Skill", "3-Skill", "4-Skill", "5-Skill", "6-Close", "InvalidSelection"],
)
def testSkillsScreen(mock_input, responses, expectedReturn, monkeypatch, capfd):
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert printSkillScreen() == expectedReturn
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out

    # Possibly delete below code, it does not test correctly
    # username = "Andrew"
    # password = "Valid123!"
    # # Check Json for login
    # with open("user_file.json", "w") as f:
    #     json.dump({username: password}, f)
    # # Inputs
    # input_generator = iter([username, password, password])
    # monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    # try:
    #     printNewAccountScreen()
    # except StopIteration:
    #     pass
    # captured = capfd.readouterr()
    # main_menu = (
    #     "*** Main Menu ***\n"
    #     "1 - Search for a job\n"
    #     "2 - Find someone that you know\n"
    #     "3 - Learn a skill\n"
    # )
    # assert main_menu in captured.out


# @pytest.mark.parametrize("input_value", ["1", "2", "3", "4", "5"])
# def testSkillsUnderConstruction(input_value, monkeypatch, capfd):
#     input_generator = iter([input_value])
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

#     try:
#         printSkillScreen()
#     except StopIteration:
#         pass

#     captured = capfd.readouterr()
#     assert "under construction, input anything to return" in captured.out


# def testSkillsReturnButton(monkeypatch, capfd):
#     input_generator = iter(["6"])  # causes skill screen to break
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
#     assert printSkillScreen() == 0  # break from skill screen loop causes return 0

    # monkeypatch.setattr("builtins.input", lambda: next(input_generator))
    # try:
    #     printSkillScreen()
    # except StopIteration:
    #     pass
    # assert excinfo.value.code == 0  # Check if the exit code is 0 when "break" is reached

    # captured = capfd.readouterr()

    # title = "*** Main Menu ***"
    # job = "1 - Search for a job"
    # findSomeone = "2 - Find someone that you know"
    # skill = "3 - Learn a skill"

    # assert title in captured.out
    # assert job in captured.out
    # assert findSomeone in captured.out
    # assert skill in captured.out


# @pytest.mark.parametrize("input_value", ["9", "0", "[1", "d", "r"])
# def testSkillsWrongInput(input_value, monkeypatch, capfd):
#     input_generator = iter([input_value])
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

#     try:
#         printSkillScreen()
#     except StopIteration:
#         pass

#     captured = capfd.readouterr()
#     assert 'Invalid selection please input "1" or "2" or "3" or "4" or "5" or "6"' in captured.out