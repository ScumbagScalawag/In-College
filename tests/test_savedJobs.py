import pytest
from common_utils.types.user_database import UserDatabase
from common_utils.types.job_database import JobDatabase
from pages.savedJobs import printSavedJobs, createSavedJob, deletedSavedJob
from tests.shared import fiveJobs, singleUser, fourAccounts
from common_utils.types.user import User
from common_utils.utils import anyButtonToContinueMessage

# def testCreateSavedJob(monkeypatch, capfd):
#     # in system
#     userDB = UserDatabase([])
#     jobDB = JobDatabase()
#     jobsToEdit = fiveJobs[:]
#     jobsToEdit[0]["firstname"] = "Bojangle"
#     jobsToEdit[0]["lastname"] = "McGee"
#     # Give us something to apply to
#     jobDB.addJobDictList(jobsToEdit)
#     userDB.addUserDictList(fourAccounts)
#     # Must create User object from singleUser Dict. See @classmethod dictToUser
#     testUser = User.dictToUser(singleUser)

#     input_generator = iter(
#         [
#             "1",
#             "01/01/2020",
#             "02/01/2020",
#             "I am fit",
#             "Foam Earplugs",
#             "X",
#         ]
#     )  # Make it choose to remove friend here
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

#     try:
#         assert (
#             printJobOptionScreen(0, testUser) == testUser
#         )  # assert printFriendsScreen returns user context correctly
#         jobDB.loadJobs()
#         assert jobDB.getJobListDict()[0]["applicants"][0]["username"] == singleUser["username"]
#     except StopIteration:
#         pass

#     captured = capfd.readouterr()  # assert captured
#     responses = [
#         *jobListingChoices,
#         "*** Job Application ***",
#         "Application sucessfully submitted",
#     ]

#     for r in responses:
#         assert r in captured.out


def testCreateSavedJob(monkeypatch, capfd):
    # in system
    userDB = UserDatabase([])
    jobDB = JobDatabase()
    jobsToEdit = fiveJobs[:]
    jobsToEdit[0]["firstname"] = "Bojangle"
    jobsToEdit[0]["lastname"] = "McGee"
    # Give us something to save
    jobDB.addJobDictList(jobsToEdit)
    userDB.addUserDictList(fourAccounts)
    # Must create User object from singleUser Dict. See @classmethod dictToUser
    testUser = User.dictToUser(singleUser)

    input_generator = iter(
        [
            "Foam Earplugs",
        ]
    )  # Make it choose to remove friend here
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert (
            createSavedJob(0, testUser) == testUser
        )  # assert printFriendsScreen returns user context correctly
        jobDB.loadJobs()
        assert jobDB.getJobListDict()[0]["saved"][0]["username"] == singleUser["username"]
    except StopIteration:
        pass

    captured = capfd.readouterr()  # assert captured
    responses = [
        "Sucessfully saved job",
        anyButtonToContinueMessage(),
    ]

    for r in responses:
        assert r in captured.out


def testDeleteSavedJob_Found(monkeypatch, capfd):
    # in system
    userDB = UserDatabase([])
    jobDB = JobDatabase()
    jobsToEdit = fiveJobs[:]
    jobsToEdit[0]["firstname"] = "Bojangle"
    jobsToEdit[0]["lastname"] = "McGee"
    jobsToEdit[0]["saved"].append({"username": singleUser["username"]})
    jobDB.addJobDictList(jobsToEdit)
    userDB.addUserDictList(fourAccounts)
    # Must create User object from singleUser Dict. See @classmethod dictToUser
    testUser = User.dictToUser(singleUser)
    input_generator = iter(["Foam Earplugs"])  # Make it choose to remove friend here
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert (
            deletedSavedJob(0, testUser) == testUser
        )  # assert printFriendsScreen returns user context correctly
        jobDB.loadJobs()
        assert jobDB.getJobListDict()[0]["saved"] == []
    except StopIteration:
        pass
    captured = capfd.readouterr()  # assert captured
    responses = [
        "Sucessfully removed job",
        anyButtonToContinueMessage(),
    ]
    for r in responses:
        assert r in captured.out


def testDeleteSavedJob_NotFound(monkeypatch, capfd):
    # in system
    userDB = UserDatabase([])
    jobDB = JobDatabase()
    jobsToEdit = fiveJobs[:]
    jobsToEdit[0]["firstname"] = "Bojangle"
    jobsToEdit[0]["lastname"] = "McGee"
    # Just don't save it
    # jobsToEdit[0]["saved"].append({"username": singleUser["username"]})
    jobDB.addJobDictList(jobsToEdit)
    userDB.addUserDictList(fourAccounts)
    # Must create User object from singleUser Dict. See @classmethod dictToUser
    testUser = User.dictToUser(singleUser)
    input_generator = iter(["Foam Earplugs"])  # Make it choose to remove friend here
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert (
            deletedSavedJob(0, testUser) == testUser
        )  # assert printFriendsScreen returns user context correctly
        jobDB.loadJobs()
        assert jobDB.getJobListDict()[0]["saved"] == []
    except StopIteration:
        pass
    captured = capfd.readouterr()  # assert captured
    responses = [
        "Job not found in saved list",
        anyButtonToContinueMessage(),
    ]
    for r in responses:
        assert r in captured.out
