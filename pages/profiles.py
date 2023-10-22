from typing import Optional

from common_utils.types.user import User
from common_utils.types.profile import Profile
from common_utils.utils import clearScreen, printOptionList
from common_utils.types.user_database import UserDatabase


def inputWithExit(prompt: str) -> Optional[str]:
    """Captures input from the user and checks if they want to exit."""
    user_input = input(prompt)
    if user_input.upper() == "X":
        return None
    return user_input


def createProfile(currentUser: Optional[User] = None) -> Optional[User]:
    userDB = UserDatabase([])
    userDB.loadUsers()

    profile = Profile()
    profile.username = currentUser.username

    print("*** Profile Editor ***")

    # Capture title
    title = inputWithExit("Enter title (or X to skip): ")
    if title:
        profile.title = title

    # Capture major
    major = inputWithExit("Enter major (or X to skip): ")
    if major:
        profile.major = major

    # Capture university
    university = inputWithExit("Enter university name (or X to skip): ")
    if university:
        profile.university = university

    # Capture about section
    about = inputWithExit("Enter about paragraph (or X to skip): ")
    if about:
        profile.about = about




    currentUser.profile = profile
    userDB.updateUserProfile(currentUser)
    currentUser = userDB.getUser(currentUser.username)
    return currentUser


# current user should be the user you wish to display
def printProfileScreen(currentUser: Optional[User] = None) -> Optional[User]:

    print(f"*** Profile of {currentUser.firstname} {currentUser.lastname} ***")
    if currentUser.profile.username == "UNDEFINED":
        print("You don't have a profile yet!")
        choice = input("Would you like to create one? (y/n): ")
        if choice.lower() == "y":
            currentUser = createProfile(currentUser)
        return currentUser

    print(f"Title: {currentUser.profile.title}")
    print(f"Major: {currentUser.profile.major}")
    print(f"University: {currentUser.profile.university}")
    print(f"About: {currentUser.profile.about}")

    # experiences
    if currentUser.profile.experiences:
        print(f"Experiences: ")
        for exp in currentUser.profile.experiences:
            print(f"Job Title: {exp.job_title}")
            print(f"Employer: {exp.employer}")
            print(f"Start Date: {exp.date_started}")
            print(f"End Date: {exp.date_ended}")
            print(f"Location: {exp.location}")
            print(f"Description {exp.description}")
            print("***")  # separator line
    else:
        print(f"{currentUser.firstname} {currentUser.lastname} has not added Experiences")

    # education
    if currentUser.profile.education:
        print(f"School Name: {currentUser.profile.education.school_name}")
        print(f"Degree: {currentUser.profile.education.degree}")
        print(f"Years Attended: {currentUser.profile.education.years_attended}")
    else:
        print(f"{currentUser.firstname} {currentUser.lastname} has not added Education")

    return currentUser
