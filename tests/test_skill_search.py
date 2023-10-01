import pytest
from pages.skill_search import printSkillScreen, skillOptionsList
from common_utils.messages import underConstructionMessage

@pytest.mark.parametrize(
    "mock_input,responses,expectedReturn",
    [
        (
            ["1", "anything"],
            [
                *skillOptionsList,
                underConstructionMessage(),
            ],
            None,
        ),
        (
            ["2", "anything"],
            [
                *skillOptionsList,
                underConstructionMessage(),
            ],
            None,
        ),
        (
            ["3", "anything"],
            [
                *skillOptionsList,
                underConstructionMessage(),
            ],
            None,
        ),
        (
            ["4", "anything"],
            [
                *skillOptionsList,
                underConstructionMessage(),
            ],
            None,
        ),
        (
            ["5", "anything"],
            [
                *skillOptionsList,
                underConstructionMessage(),
            ],
            None,
        ),
        (
            ["6"],
            [
                *skillOptionsList,
            ],
            None,
        ),
        (
            ["FoamEarplugs"],
            [
                *skillOptionsList,
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


#Already tested for above
@pytest.mark.parametrize(
    "input_value",
    [
        "1",
        "2",
        "3",
        "4",
        "5",
    ],
)
def testSkillsUnderConstruction(input_value, monkeypatch, capfd):
    input_generator = iter([input_value])
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        printSkillScreen()
    except StopIteration:
        pass

    captured = capfd.readouterr()
    assert underConstructionMessage() in captured.out
    
# Already handled above in testSkillsScreen
@pytest.mark.parametrize(
    "input_value",
    [
        "9",
        "0",
        "[1",
        "d",
        "r",
    ],
)
def testSkillsWrongInput(input_value, monkeypatch, capfd):
    input_generator = iter([input_value])
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        printSkillScreen()
    except StopIteration:
        pass

    captured = capfd.readouterr()
    assert 'Invalid selection please input "1" or "2" or "3" or "4" or "5" or "6"' in captured.out
