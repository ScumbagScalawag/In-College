import os

JSONFP2 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "user_file.json")
JSONFPJ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "jobs.json")

singleUser = {
    "username": "asdfasdf",
    "password": "P@ssw0rd",
    "firstname": "Noah",
    "lastname": "McIvor",
    "connections": [],
}

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
