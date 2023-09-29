import pytest
from pages.initial_screen import printInitialScreen
from pages.main_menu import printMainMenu
from pages.friend_search import printFriendSearchScreen


def test_start_back(monkeypatch, capfd):
    input_generator = iter(["X", "X"])
    monkeypatch.setattr("builtins.input", lambda *args: next(input_generator))
    try:
        printInitialScreen() == 0
    except StopIteration:
        pass
    captured = capfd.readouterr()
    exit_statment = "Exiting InCollege"
    assert exit_statment in captured.out


def test_start_find_users_false(monkeypatch, capfd):
    input_generator = iter(["Brad", "Ley", "X"])
    monkeypatch.setattr("builtins.input", lambda *args: next(input_generator))

    result = printFriendSearchScreen("test")
    assert result == 0
    captured = capfd.readouterr()
    assert "*** Find A Friend ***" in captured.out


def test_search_for_job_back(monkeypatch, capfd):
    input_generator = iter(["1", "3"])
    monkeypatch.setattr("builtins.input", lambda *args: next(input_generator))
    try:
        printMainMenu("Test")
    except StopIteration:
        pass
    captured = capfd.readouterr()
    assert captured.out.count("*** Main Menu ***") == 2


def test_find_users_false(monkeypatch, capfd):
    input_generator = iter(["2", "Brad", "Ley", "X"])
    monkeypatch.setattr("builtins.input", lambda *args: next(input_generator))
    try:
        printMainMenu("Test")
    except StopIteration:
        pass

    captured = capfd.readouterr()
    assert "*** Find A Friend ***" in captured.out
    assert "*** Main Menu ***" in captured.out
    assert "They are not yet a part of the InCollege system yet" in captured.out


def test_skill_back(monkeypatch, capfd):
    input_generator = iter(["3", "6"])
    monkeypatch.setattr("builtins.input", lambda *args: next(input_generator))
    try:
        printMainMenu("Test")
    except StopIteration:
        pass

    captured = capfd.readouterr()
    assert "*** Learn a skill ***" in captured.out
    assert captured.out.count("*** Main Menu ***") == 2


def test_main_menu_back(monkeypatch):
    input_generator = iter(["X"])
    monkeypatch.setattr("builtins.input", lambda *args: next(input_generator))
    result = printMainMenu("Test")
    assert result == 0
