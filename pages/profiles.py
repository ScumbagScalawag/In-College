from typing import Optional

from common_utils.types.user import User
from common_utils.types.profile import Profile
from common_utils.types.user_database import UserDatabase
from common_utils.utils import clearScreen, printOptionList

"""
After entering their profile information, the student will be able to view their profile.
    When their profile is displayed, their name will be automatically be displayed at the top of the profile information.
Students will be able to display the profile of any student that they have a friend relationship with.
They will be able to do this by displaying a list of people that they are friends with and then selecting the "profile" option that is by a friend's name.
When they do this, the friend's profile will be displayed.
The number of friends that that friend has will not be displayed.
If they don't have a friend relationship with someone, they won't be able to see that person's profile information.
"""


def tempName(profile, string):
    while True:
        print(f"Enter {string}: ", end="")
        user_input = input("")
        print("***")
        print(f"{string}: {user_input}")
        print("Confirm - C, Retry - R, Save and Exit - X")
        flag = input("")
        if flag == "C":
            profile.string = user_input
            return profile
        elif flag == "R":
            clearScreen()
        elif flag == "X":
            # TODO Implement save and exit
            return


def createProfile(currentUser: Optional[User] = None) -> Optional[User]:
    # profile = currentUser.profile
    proifle = Profile()
    profile.username = currentUser.username
    print("*** Profile Editor ***")
    profile = tempName(profile, "title")
    # TODO Finish profile
    user_input = input("")
    profile.title = user_input

    return currentUser


# current user should be the user you wish to display
def printProfileScreen(currentUser: Optional[User] = None) -> Optional[User]:
    # assuming profile option is shown and they now choose to display the profile
    print(f"*** Profile of {currentUser.firstname} {currentUser.lastname} ***")

    print(currentUser.profile)
    print(f"{currentUser.profile.title}")
    print(f"Major: {currentUser.profile.major}")
    print(f"University: {currentUser.profile.university}")
    print(f"About: {currentUser.profile.about}")

    # experiences
    if currentUser.profile.experiences != []:
        # not empty
        print(f"Experiences: ")
        for exp in currentUser.profile.experiences:
            print(f"Job Title: {exp.job_title}")
            print(f"Employer: {exp.employer}")
            print(f"Start Date: {exp.date_started}")
            print(f"End Date: {exp.date_ended}")
            print(f"Location: {exp.location}")
            print(f"Description {exp.description}")
            print("***")  # seperator line
    else:
        # empty, skip printing it
        print(f"{currentUser.firstname} {currentUser.lastname} has not added Experiences")

    # education
    if currentUser.profile.education != []:
        # not empty
        print(f"School Name: {currentUser.profile.education.school_name}")
        print(f"Degree: {currentUser.profile.education.degree}")
        print(f"Years Attened: {currentUser.profile.education.years_attended}")
    else:
        # empty
        print(f"{currentUser.firstname} {currentUser.lastname} has not added Education")

    return currentUser
