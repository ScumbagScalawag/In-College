# import pytest
# from pages.application import applyToJob, checkDate, personalApplicationList, notAppliedList
# from common_utils.messages import anyButtonToContinueMessage, invalidInput, underConstructionMessage
# from tests.shared import (
#     JSON_JOBS_FP,
#     singleUser,
#     fourJobs,
#     fiveJobs,
#     fourAccounts,
#     threeAccounts,
#     singleJob,
# )
# from common_utils.types.user_database import UserDatabase
# from common_utils.types.user import User
# from common_utils.types.job_database import JobDatabase
# from common_utils.types.job import Job


# @pytest.mark.parametrize(
#     "mock_input,jobIndex,startingUser,startingUserDB,startingJobDB,responses",
#     [
#         (
#             [""],  # mock input
#             0,  # job index
#             singleUser,  # test user
#             threeAccounts,  # starting userDB
#             singleJob,  # starting jobDB
#             [
#                 "You must be logged in to apply for a Job.",
#                 anyButtonToContinueMessage(),
#             ],  # responses
#         ),
#         (
#             [""],  # mock input
#             0,  # job index
#             singleUser,  # test user
#             fourAccounts,  # starting userDB
#             [],  # starting jobDB
#             [
#                 "You must be logged in to create a Job.",
#                 anyButtonToContinueMessage(),
#             ],  # responses
#         ),
#     ],
#     ids=[
#         "User is not logged in",
#         "User has already applied",
#         # "User created job posting",
#         # "User has already applied",
#     ],
# )
# def testApplyToJob(
#     mock_input, jobIndex, startingUser, startingUserDB, startingJobDB, responses, monkeypatch, capfd
# ):
#     testUser = User.dictToUser(startingUser)
#     userDB = UserDatabase([])
#     userDB.addUserDictList(startingUserDB)
#     jobDB = JobDatabase([])
#     jobDB.addJobDictList(startingJobDB)
#     jobDB.saveDatabase()
#     input_generator = iter(mock_input)
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

#     try:
#         assert applyToJob(jobIndex, testUser) == testUser
#     except StopIteration:
#         pass
#     captured = capfd.readouterr()
#     for r in responses:
#         assert r in captured.out


# def test_applyToJob(monkeypatch, capfd):
#     mock_input = [""]
#     responses = [
#         *accessibilityOptions,
#         anyButtonToContinueMessage(),
#     ]
#     input_generator = iter(mock_input)
#     monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
#     testUser = None
#     try:
#         assert printAccessibilityScreen(testUser) == testUser
#     except StopIteration:
#         pass
#     captured = capfd.readouterr()
#     for r in responses:
#         assert r in captured.out
import pytest
from pages.application import applyToJob, checkDate, personalApplicationList, notAppliedList
from common_utils.messages import anyButtonToContinueMessage, invalidInput, underConstructionMessage
from tests.shared import (
    JSON_JOBS_FP,
    singleUser,
    fourJobs,
    fiveJobs,
    fourAccounts,
    threeAccounts,
    singleJob,
)
from common_utils.types.user_database import UserDatabase
from common_utils.types.user import User
from common_utils.types.job_database import JobDatabase
from common_utils.types.job import Job


@pytest.mark.parametrize(
    "mock_input,jobIndex,startingUser,startingUserDB,startingJobDB,responses",
    [
        (
            ["01/01/2022", "02/01/2022", "I am fit", ""],  # mock input
            0,  # job index
            singleUser,  # test user
            fourAccounts,  # starting userDB
            fourJobs,  # starting jobDB
            [
                "*** Job Application ***",
                "Application sucessfully submitted",
                anyButtonToContinueMessage(),
            ],  # responses
        ),
        (
            [""],  # mock input
            1,  # job index
            singleUser,  # test user
            fourAccounts,  # starting userDB
            fourJobs,  # starting jobDB
            [
                "You cannot apply for a job you posted.",
                anyButtonToContinueMessage(),
            ],  # responses
        ),
        (
            ["", "01/01/2022", "02/01/2022", "I am a good fit"],  # mock input
            0,  # job index
            singleUser,  # test user
            threeAccounts,  # starting userDB
            singleJob,  # starting jobDB
            [
                "You must be logged in to apply for a Job.",
                anyButtonToContinueMessage(),
            ],  # responses
        ),
        (
            ["", "invalid date", "02/01/2022", "I am a good fit"],  # mock input
            0,  # job index
            singleUser,  # test user
            fourAccounts,  # starting userDB
            singleJob,  # starting jobDB
            [
                "Invalid input. Please enter the date in the valid date format",
                anyButtonToContinueMessage(),
            ],  # responses
        ),
        (
            ["", "01/01/2022", "invalid date", "I am a good fit"],  # mock input
            0,  # job index
            singleUser,  # test user
            fourAccounts,  # starting userDB
            singleJob,  # starting jobDB
            [
                "Invalid input. Please enter the date in the valid date format",
                anyButtonToContinueMessage(),
            ],  # responses
        ),
        (
            ["", "01/01/2022", "02/01/2022", "I am a good fit"],  # mock input
            0,  # job index
            singleUser,  # test user
            fourAccounts,  # starting userDB
            singleJob,  # starting jobDB
            [
                "You cannot apply for a job you have already applied to.",
                anyButtonToContinueMessage(),
            ],  # responses
        ),
        (
            ["", "01/01/2022", "02/01/2022", "I am a good fit"],  # mock input
            0,  # job index
            singleUser,  # test user
            fourAccounts,  # starting userDB
            fourJobs,  # starting jobDB
            [
                "You cannot apply for a job you posted.",
                anyButtonToContinueMessage(),
            ],  # responses
        ),
    ],
    ids=[
        "Valid input apply to job",
        "User has created a job",
        "User is not logged in",
        "Invalid graduation date",
        "Invalid start date",
        "User has already applied",
        "User created job posting",
    ],
)
def testApplyToJob(
    mock_input, jobIndex, startingUser, startingUserDB, startingJobDB, responses, monkeypatch, capfd
):
    testUser = User.dictToUser(startingUser)
    userDB = UserDatabase([])
    userDB.addUserDictList(startingUserDB)
    jobDB = JobDatabase([])
    jobDB.addJobDictList(startingJobDB)
    jobDB.saveDatabase()
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    try:
        assert applyToJob(jobIndex, testUser) == testUser
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out
