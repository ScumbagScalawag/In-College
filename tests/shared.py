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
    "uni": "usf",
    "major": "cs",
    "email": "asdfasdf@gmail.com",
    "phoneNumber": "1932930298",
    "language": "English",
    "emailSub": True,
    "smsSub": True,
    "adSub": True,
    "friends": [],
    "friendRequests": [],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
}

# A user with no Defualt values to ensure r/w operations are working
nonDefualtsSingleUser = {
    "username": "asdfasdf",
    "password": "P@ssw0rd",
    "firstname": "Dude",
    "lastname": "Dummy",
    "uni": "usf",
    "major": "cs",
    "email": "nondefaultuser@gmail.com",
    "phoneNumber": "6666666666",
    "language": "Spanish",
    "emailSub": False,
    "smsSub": False,
    "adSub": False,
    "friends": ["someUser"],
    "friendRequests": ["someOtherUser", "anotherUser"],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
}
# Three Accounts does not include single user
threeAccounts = [
    {
        "username": "dummy",
        "password": "Password1!",
        "firstname": "Jo",
        "lastname": "Mama",
        "uni": "usf",
        "major": "cs",
        "email": "asdfasdf@gmail.com",
        "phoneNumber": "1932930298",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
    },
    {
        "username": "sillyBoi",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "uni": "fsu",
        "major": "cs",
        "email": "asdfasdf@gmail.com",
        "phoneNumber": "1932930298",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": ["notKaren", "dummy"],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
    },
    {
        "username": "dummyDude",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "uni": "uf",
        "major": "ee",
        "email": "dummyDude@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": ["admin"],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
    },
]
# four accounts = three + single user
fourAccounts = [
    {
        "username": "asdfasdf",
        "password": "P@ssw0rd",
        "firstname": "Noah",
        "lastname": "McIvor",
        "uni": "fsu",
        "major": "cs",
        "email": "nm@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
    },
    {
        "username": "dummy",
        "password": "Password1!",
        "firstname": "Jo",
        "lastname": "Mama",
        "uni": "usf",
        "major": "cs",
        "email": "dummy@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
    },
    {
        "username": "sillyBoi",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "uni": "usf",
        "major": "cs",
        "email": "dee@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": ["dummy"],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
    },
    {
        "username": "dummyDude",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "uni": "uf",
        "major": "cs",
        "email": "dummyDude@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
    },
]
# 5 = 3 + 1 + 1
fiveAccounts = [
    {
        "username": "dummy",
        "password": "Password1!",
        "firstname": "Jo",
        "lastname": "Mama",
        "uni": "uf",
        "major": "cs",
        "email": "dummyDude@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
    },
    {
        "username": "sillyBoi",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "uni": "uf",
        "major": "cs",
        "email": "sillyboi@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": ["notKaren", "dummy"],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
    },
    {
        "username": "dummyDude",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "uni": "usf",
        "major": "cs",
        "email": "dummydude@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": ["admin"],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
    },
    {
        "username": "notKaren",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "uni": "usf",
        "major": "ee",
        "email": "notkaren@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": ["dummy"],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
    },
    {
        "username": "theSilliestOfAll",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "uni": "usf",
        "major": "ee",
        "email": "silly@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [""],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
    },
]

tenAccounts = [
    {
        "username": "dummy",
        "password": "Password1!",
        "firstname": "Jo",
        "lastname": "Mama",
        "uni": "usf",
        "major": "ee",
        "email": "dummyDude@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
    },
    {
        "username": "sillyBoi",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "uni": "usf",
        "major": "ee",
        "email": "sillyboi@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": ["notKaren", "dummy"],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
    },
    {
        "username": "dummyDude",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "uni": "usf",
        "major": "ee",
        "email": "dummydude@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": ["admin"],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
    },
    {
        "username": "notKaren",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "uni": "usf",
        "major": "ee",
        "email": "notkaren@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": ["dummy"],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
    },
    {
        "username": "theSilliestOfAll",
        "password": "Password2@",
        "firstname": "Dee",
        "lastname": "Snuts",
        "uni": "usf",
        "major": "ee",
        "email": "silly@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [""],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
    },
    {
        "username": "A",
        "password": "Password2@",
        "firstname": "A",
        "lastname": "A",
        "uni": "usf",
        "major": "cs",
        "email": "A@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [""],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
    },
    {
        "username": "B",
        "password": "Password2@",
        "firstname": "B",
        "lastname": "B",
        "uni": "usf",
        "major": "cs",
        "email": "B@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [""],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
    },
    {
        "username": "C",
        "password": "Password2@",
        "firstname": "C",
        "lastname": "C",
        "uni": "usf",
        "major": "cs",
        "email": "C@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [""],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
    },
    {
        "username": "D",
        "password": "Password2@",
        "firstname": "D",
        "lastname": "D",
        "uni": "usf",
        "major": "cs",
        "email": "D@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [""],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
    },
    {
        "username": "E",
        "password": "Password2@",
        "firstname": "E",
        "lastname": "E",
        "uni": "usf",
        "major": "cs",
        "email": "E@gmail.com",
        "phoneNumber": "1234567890",
        "language": "English",
        "emailSub": True,
        "smsSub": True,
        "adSub": True,
        "friends": [],
        "friendRequests": [""],
        "profile": {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                },
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

# ------- ]]]

# Profiles ------ [[[

emptyProfile = {
                    "username": "UNDEFINED",
                    "title": "UNDEFINED",
                    "major": "Undefined",
                    "university": "Undefined",
                    "about": "UNDEFINED",
                    "education": {
                        "school_name": "UNDEFINED",
                        "degree": "UNDEFINED",
                        "years_attended": "UNDEFINED"
                    },
                    "experiences": []
                }

sampleProfile = {
                    "username": "asdfasdf",
                    "title": "Software Engineer",
                    "major": "Cs",
                    "university": "Usf",
                    "about": "I like trains",
                    "education": {
                        "school_name": "USF",
                        "degree": "Bachelors in Computer Science",
                        "years_attended": "4"
                    },
                    "experiences": [
                        {
                            "job_title": "Software Intern",
                            "employer": "Google",
                            "date_started": "May 2020",
                            "date_ended": "August 2020",
                            "location": "Tampa, FL",
                            "description": "Idk whatever they do at google"
                        }
                    ]
                }