import pytest

# underConstructionMessage = "under construction, input anything to return" #
from common_utils.messages import underConstructionMessage
from pages.about import printAboutScreen
from pages.accessibility import printAccessibilityScreen
from pages.brand_policy import printBrandPolicyScreen
from pages.cookie_policy import printCookiePolicyScreen
from pages.copyright_notice import printCopyrightNoticeScreen
from pages.copyright_policy import printCopyrightPolicyScreen
from pages.guest_controls import printGuestControlsScreen
from pages.important_links import importantLinksOptionsList, printImportantLinkScreen
from pages.languages import printLanguagesScreen
from pages.privacy_policy import printPrivacyPolicyScreen
from pages.user_agreement import printUserAgreementScreen


@pytest.mark.parametrize(
    "mock_input,responses,expectedReturn",
    [
        (
            ["1"],  # Copyright Notice
            [
                *importantLinksOptionsList,
                "*** Copyright Notice ***",
            ],
            [],
        ),
        (
            ["2"],  # About
            [
                *importantLinksOptionsList,
                "*** About ***",
            ],
            [],
        ),
        (
            ["3"],  # Accessibiltiy
            [
                *importantLinksOptionsList,
                "*** Accessibility ***",
            ],
            [],
        ),
        (
            ["4"],  # User Agreement
            [*importantLinksOptionsList, "*** User Agreement ***"],
            [],
        ),
        (
            ["5"],  # Privacy Policy
            [*importantLinksOptionsList, "*** Privacy Policy ***"],
            [],
        ),
        (
            ["6"],  # Cookie Policy
            [
                *importantLinksOptionsList,
                "*** Cookie Policy ***",
            ],
            [],
        ),
        (
            ["7"],  # Copyright Policy
            [
                *importantLinksOptionsList,
                "*** Copyright Policy ***",
            ],
            [],
        ),
        (
            ["8"],  # Brand Policy
            [
                *importantLinksOptionsList,
                "*** Brand Policy ***",
            ],
            [],
        ),
        (
            ["9"],  # Guest Controls
            [
                *importantLinksOptionsList,
                "*** Guest Control ***",
            ],
            [],
        ),
        (
            ["10"],  # Languages
            [
                *importantLinksOptionsList,
                "*** Languages ***",
            ],
            [],
        ),
        (
            ["X"],  # Return
            [
                *importantLinksOptionsList,
            ],
            None,  # We are currentUser=None
        ),
        (
            ["FoamEarplugs"],  # Invalid Input
            [
                *importantLinksOptionsList,
            ],
            [],
        ),
    ],
    ids=[
        "1 - A Copyright Notice",
        "2 - About",
        "3 - Accessibility",
        "4 - User Agreement",
        "5 - Privacy Policy",
        "6 - Cookie Policy",
        "7 - Copyright Policy",
        "8 - Brand Policy",
        "9 - Guest Controls",
        "10 - Languages",
        "X - Return",
        "InvalidSelection",
    ],
)
def testPrintUsefulLinkScreen(mock_input, responses, expectedReturn, monkeypatch, capfd):
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert printImportantLinkScreen() == expectedReturn
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
