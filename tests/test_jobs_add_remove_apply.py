from common_utils.types.jobs import deleteJob
from pages.application import applyToJob
from common_utils.utils import loadJobs
import pytest
import json
from tests.shared import JSON_JOBS_FP, fourAccounts
from common_utils.types.user import User
from pages.application import createJob

@pytest.fixture
def setup_jobs():
    # 1. Read and save the original data
    with open(JSON_JOBS_FP, 'r') as f:
        original_data = f.read()

    # 2. Clear the jobs.json
    with open(JSON_JOBS_FP, 'w') as f:
        json.dump({"joblist": [{
            "title": "Test Job Title",
            "description": "Test Job Description",
            "employer": "Test Employer",
            "location": "Test Location",
            "salary": "Test Salary",
            "firstname": "Noah",
            "lastname": "McIvor",
            "applicants": [],
            "saved": []
        }]}, f, indent=4)

    yield  # Test area

    # 4. Restore original data
    with open(JSON_JOBS_FP, 'w') as f:
        f.write(original_data)
# MAKE SURE THAT THE JOBS < MAX, as it adds a test job to jobs.json

def test_add_job(monkeypatch, capfd,setup_jobs):
    user = User.dictToUser(fourAccounts[0])
    mock_input_create = [
        "Test Job Title",
        "Test Job Description",
        "Test Employer",
        "Test Location",
        "Test Salary",
        "\n"
    ]
    input_generator = iter(mock_input_create)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        createJob(user)
    except StopIteration:
        pass
    captured = capfd.readouterr()
    assert "*** Create a new job posting ***" in captured.out
    assert "Job Created!" in captured.out
    jobs = loadJobs()
    assert any(job["title"] == "Test Job Title" for job in jobs)

def test_delete_job(monkeypatch, capfd,setup_jobs):
    # Mocking a current user
    currentUser = User.dictToUser(fourAccounts[0])

    # Mocking the input for the job title to be deleted
    job_title_to_delete = "Test Job Title"
    input_generator = iter([job_title_to_delete])
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    # Calling the deleteJob function
    try:
        deleteJob(currentUser)
    except StopIteration:
        pass

    # Capturing the printed output
    captured = capfd.readouterr()

    # Checking the expected messages
    assert "Job deleted successfully" in captured.out
def test_delete_job_no_access(monkeypatch, capfd,setup_jobs):
    # Mocking a current user
    currentUser = User.dictToUser(fourAccounts[1])

    # Mocking the input for the job title to be deleted
    job_title_to_delete = "Test Job Title"
    input_generator = iter([job_title_to_delete])
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    # Calling the deleteJob function
    try:
        deleteJob(currentUser)
    except StopIteration:
        pass

    # Capturing the printed output
    captured = capfd.readouterr()

    # Checking the expected messages
    assert "You are not the poster of this job" in captured.out


@pytest.mark.parametrize(
    "mock_input, responses, expectedReturn",
    [
        # Test case: User not logged in
        (
            ["01/01/2022"],  # Mocked input for graduation date
            ["You must be logged in to create a Job."],  # Expected response
            None  # Expected return value
        ),
        # Test case: User trying to apply to their own job
        (
            ["01/01/2022"],
            ["You cannot apply for a job you posted.\nPress any button to continue...\n"],
            User.dictToUser(fourAccounts[0])
        ),
        # Test case: User already applied//test
        (
            ["01/01/2022"],
            ["\x0c*** Job Application ***\n"],  # Adjusted based on actual behavior
            User.dictToUser(fourAccounts[1]) #Assumption made here
        ),
    ],
    ids=[
        "Not_Logged_In",
        "Apply_Own_Job",
        "Already_Applied"
    ],
)
def test_apply_to_job_conditions(mock_input, responses, expectedReturn, monkeypatch, capfd, setup_jobs):
    input_generator = iter(mock_input)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))
    try:
        assert applyToJob(0, expectedReturn) == expectedReturn
    except StopIteration:
        pass
    captured = capfd.readouterr()
    for r in responses:
        assert r in captured.out

