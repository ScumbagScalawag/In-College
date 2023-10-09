import os

JSON_USERS_FP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "user_file.json")
JSON_JOBS_FP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "jobs.json")
UNEXPECTED_TESTING_ERROR_MESSAGE = (
    "Unexpected Error occured while testing. Please make sure to double check fixture data"
)

# Users ------- [[[
singleUser = {
    "username": "asdfasdf",
    "password": "P@ssw0rd",
    "firstname": "Noah",
    "lastname": "McIvor",
    "email": "asdfasdf@gmail.com",
    "phoneNumber": "1932930298",
    "language": "English",
    "emailSub": True,
    "smsSub": True,
    "adSub": True,
    "friends": [],
    "friendRequests": [],
}

# A user with no Defualt values to ensure r/w operations are working
nonDefualtsSingleUser = {
    "username": "asdfasdf",
    "password": "P@ssw0rd",
    "firstname": "Dude",
    "lastname": "Dummy",
    "email": "nondefaultuser@gmail.com",
    "phoneNumber": "6666666666",
    "language": "Spanish",
    "emailSub": False,
    "smsSub": False,
    "adSub": False,
    "friends": ["someUser"],
    "friendRequests": ["someOtherUser", "anotherUser"],
}
# Three Accounts does not include single user
threeAccounts = [
    {
        "username": "dummy",
        "password": "Password1!",
        "firstname": "Jo",
        "lastname": "Mama",
        "email": "asdfasdf@gmail.com",
        "phoneNumber": "1932930298",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [],
    },
    {
        "username": "sillyBoi",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "email": "asdfasdf@gmail.com",
        "phoneNumber": "1932930298",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": ["notKaren", "dummy"],
    },
    {
        "username": "dummyDude",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "email": "dummyDude@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": ["admin"],
    },
]
# four accounts = three + single user
fourAccounts = [
    {
        "username": "asdfasdf",
        "password": "P@ssw0rd",
        "firstname": "Noah",
        "lastname": "McIvor",
        "email": "nm@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [],
    },
    {
        "username": "dummy",
        "password": "Password1!",
        "firstname": "Jo",
        "lastname": "Mama",
        "email": "dummy@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [],
    },
    {
        "username": "sillyBoi",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "email": "dee@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": ["dummy"],
    },
    {
        "username": "dummyDude",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "email": "dummyDude@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [],
    },
]
# 5 = 3 + 1 + 1
fiveAccounts = [
    {
        "username": "dummy",
        "password": "Password1!",
        "firstname": "Jo",
        "lastname": "Mama",
        "email": "dummyDude@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [],
    },
    {
        "username": "sillyBoi",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "email": "sillyboi@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": ["notKaren", "dummy"],
    },
    {
        "username": "dummyDude",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "email": "dummydude@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": ["admin"],
    },
    {
        "username": "notKaren",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "email": "notkaren@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": ["dummy"],
    },
    {
        "username": "theSilliestOfAll",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "email": "silly@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [""],
    },
]

tenAccounts = [
    {
        "username": "dummy",
        "password": "Password1!",
        "firstname": "Jo",
        "lastname": "Mama",
        "email": "dummyDude@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [],
    },
    {
        "username": "sillyBoi",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "email": "sillyboi@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": ["notKaren", "dummy"],
    },
    {
        "username": "dummyDude",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "email": "dummydude@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": ["admin"],
    },
    {
        "username": "notKaren",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "email": "notkaren@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": ["dummy"],
    },
    {
        "username": "theSilliestOfAll",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "email": "silly@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [""],
    },
    {
        "username": "A",
        "password": "Password2@",
        "firstname": "A",
        "lastname": "A",
        "email": "A@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [""],
    },
    {
        "username": "B",
        "password": "Password2@",
        "firstname": "B",
        "lastname": "B",
        "email": "B@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [""],
    },
    {
        "username": "C",
        "password": "Password2@",
        "firstname": "C",
        "lastname": "C",
        "email": "C@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [""],
    },
    {
        "username": "D",
        "password": "Password2@",
        "firstname": "D",
        "lastname": "D",
        "email": "D@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [""],
    },
    {
        "username": "E",
        "password": "Password2@",
        "firstname": "E",
        "lastname": "E",
        "email": "E@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [""],
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
