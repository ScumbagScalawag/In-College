import pytest
import json
from tests.shared import JSON_JOBS_FP, fourAccounts
from common_utils.types.user import User
from pages.application import createJob

@pytest.fixture
def setup_jobs():
    with open(JSON_JOBS_FP, 'r') as f:
        original_data = f.read()
    # 10 jobs
    test_jobs = {
        "joblist": [
            {
                "title": f"Test Job {i}",
                "description": f"Description {i}",
                "employer": f"Employer {i}",
                "location": f"Location {i}",
                "salary": f"Salary {i}",
                "firstname": f"Name {i}",
                "lastname": f"Last {i}",
                "applicants": [],
                "saved": []
            } for i in range(10)
        ]
    }

    with open(JSON_JOBS_FP, 'w') as f:
        json.dump(test_jobs, f, indent=4)

    yield  # Test area

    # Rewrite data back
    with open(JSON_JOBS_FP, 'w') as f:
        f.write(original_data)

def test_exceeding_job_limit(monkeypatch, capfd, setup_jobs):
    input_generator = iter(["11th Job", "11th Description", "11th Employer", "11th Location", "11th Salary"])
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    currentUser = User.dictToUser(fourAccounts[0])

    try:
        createJob(currentUser)
    except StopIteration:
        pass

    captured = capfd.readouterr()
    assert "All permitted jobs have been posted, please try again later" in captured.out
