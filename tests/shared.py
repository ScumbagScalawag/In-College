import os

JSON_USERS_FP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "user_file.json")
JSON_JOBS_FP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "jobs.json")

# Users ------- [[[
singleUser = [
    {
        "username": "asdfasdf",
        "password": "P@ssw0rd",
        "firstname": "Noah",
        "lastname": "McIvor",
        "connections": [],
    },
]
# Three Accounts does not include single user
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
# four accounts = three + single user
fourAccounts = [
    {
        "username": "asdfasdf",
        "password": "P@ssw0rd",
        "firstname": "Noah",
        "lastname": "McIvor",
        "connections": [],
    },
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
        "connections": ["dummy"],
    },
    {
        "username": "dummyDude",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "connections": [],
    },
]
# 5 = 3 + 1 + 1
fiveAccounts = [
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
    {
        "username": "notKaren",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "connections": ["dummy"],
    },
    {
        "username": "theSilliestOfAll",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "connections": [""],
    },
]

# ------- ]]]

# Jobs ------ [[[
singleJob = {
    "title": "Chocolate Taster",
    "description": "Test Chocolate",
    "employer": "Hershey Chocolate Company",
    "location": "Hershey, Pennsylvania",
    "salary": "1",
    "firstname": "Noah",
    "lastname": "McIvor",
}

# Used to check when under maximum number of jobs
fourJobs = [
    {
        "title": "Software Engineer",
        "description": "Developing software applications",
        "employer": "Company A",
        "location": "San Francisco, CA",
        "salary": "90000",
        "firstname": "Noah",
        "lastname": "McIvor",
    },
    {
        "title": "Data Analyst",
        "description": "Analyzing data and generating reports",
        "employer": "Data Analytics Inc.",
        "location": "New York, NY",
        "salary": "75000",
        "firstname": "Noah",
        "lastname": "McIvor",
    },
    {
        "title": "Potato Masher",
        "description": "Mashes potatos and mixes in butter",
        "employer": "JP Morgan",
        "location": "Miami, FL",
        "salary": "1000000",
        "firstname": "Noah",
        "lastname": "McIvor",
    },
    {
        "title": "Magician",
        "description": "Maintain linux servers",
        "employer": "Amazon",
        "location": "Miami, OH",
        "salary": "275000",
        "firstname": "Noah",
        "lastname": "McIvor",
    },
]

# Used to test over maximum number of jobs
fiveJobs = [
    {
        "title": "Software Engineer",
        "description": "Developing software applications",
        "employer": "Company A",
        "location": "San Francisco, CA",
        "salary": "90000",
        "firstname": "Noah",
        "lastname": "McIvor",
    },
    {
        "title": "Data Analyst",
        "description": "Analyzing data and generating reports",
        "employer": "Data Analytics Inc.",
        "location": "New York, NY",
        "salary": "75000",
        "firstname": "Noah",
        "lastname": "McIvor",
    },
    {
        "title": "Potato Masher",
        "description": "Mashes potatos and mixes in butter",
        "employer": "JP Morgan",
        "location": "Miami, FL",
        "salary": "1000000",
        "firstname": "Noah",
        "lastname": "McIvor",
    },
    {
        "title": "Magician",
        "description": "Maintain linux servers",
        "employer": "Amazon",
        "location": "Miami, OH",
        "salary": "275000",
        "firstname": "Noah",
        "lastname": "McIvor",
    },
    {
        "title": "Pokemon Trainer",
        "description": "Capture, train, and battle with a team of Pokemon",
        "employer": "Professor Oak",
        "location": "Pallet Town, KA",
        "salary": "0",
        "firstname": "Noah",
        "lastname": "McIvor",
    },
]
