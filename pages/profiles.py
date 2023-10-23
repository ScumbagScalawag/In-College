from typing import Optional

from common_utils.types.user import User
from common_utils.types.profile import Profile
from common_utils.types.user_database import UserDatabase
from common_utils.types.education import Education
from common_utils.types.experience import Experience
from common_utils.messages import anyButtonToContinueMessage


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

    add_education = inputWithExit("Do you want to add education details? (y/n or X to skip): ")
    if add_education.lower() == "y":
        school_name = inputWithExit("Enter school name (or X to skip): ")
        degree = inputWithExit("Enter degree (or X to skip): ")
        years_attended = inputWithExit("Enter years attended (or X to skip): ")
        profile.education = Education(
            school_name, degree, years_attended
        )  # Assuming you've imported Education

    add_experience = inputWithExit("Do you want to add experience details? (y/n or X to skip): ")
    if add_experience.lower() == "y":
        experiences = []  # A list to hold experiences
        max_experiences = 3  # Maximum number of experiences allowed
        for i in range(max_experiences):
            print(f"\nAdding experience {i + 1}/{max_experiences}")
            job_title = inputWithExit("Enter job title (or X to skip): ")
            if not job_title:
                break  # if user chooses to skip
            employer = inputWithExit("Enter employer (or X to skip): ")
            date_started = inputWithExit("Enter start date (or X to skip): ")
            date_ended = inputWithExit("Enter end date (or X to skip): ")
            location = inputWithExit("Enter location (or X to skip): ")
            description = inputWithExit("Enter description (or X to skip): ")

            experiences.append(
                Experience(job_title, employer, date_started, date_ended, location, description)
            )

            if i < max_experiences - 1:  # Check if there's room for another experience
                another = inputWithExit(
                    "Do you want to add another experience? (y/n or X to skip): "
                )
                if another.lower() != "y":
                    break
            else:
                print("You've added the maximum number of experiences.")

        profile.experiences = experiences

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
    # education
    if currentUser.profile.education:
        print("Education:")
        print(f"School Name: {currentUser.profile.education.school_name}")
        print(f"Degree: {currentUser.profile.education.degree}")
        print(f"Years Attended: {currentUser.profile.education.years_attended}")
    else:
        print(f"{currentUser.firstname} {currentUser.lastname} has not added Education")

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
    print(anyButtonToContinueMessage())
    input("")
    return currentUser


def printEditProfile(currentUser: Optional[User] = None) -> Optional[User]:
    userDB = UserDatabase([])
    userDB.loadUsers()
    field_to_edit = input(
        "Enter field to edit (title, major, university, about, experience, education) or X to exit: "
    ).lower()

    if field_to_edit == "x":
        return currentUser

    if field_to_edit in ["title", "major", "university", "about"]:
        new_value = input(f"Enter new value for {field_to_edit}: ")
        if field_to_edit in ["major", "university"]:
            new_value = new_value.title()
        setattr(currentUser.profile, field_to_edit, new_value)

    elif field_to_edit == "experience":
        # TODO Fix input
        exp_num = int(input("Which experience number would you like to edit? "))
        if 0 < exp_num <= len(currentUser.profile.experiences):
            exp_to_edit = currentUser.profile.experiences[exp_num - 1]
            exp_field = input(
                "Which experience field would you like to edit (job_title, employer, date_started, date_ended, location, description): "
            )
            new_value = input(f"Enter new value for {exp_field}: ")
            setattr(exp_to_edit, exp_field, new_value)

    elif field_to_edit == "education":
        if currentUser.profile.education:
            edu_field = input(
                "Which education field would you like to edit (school_name, degree, years_attended): "
            )
            new_value = input(f"Enter new value for {edu_field}: ")
            setattr(currentUser.profile.education, edu_field, new_value)
    else:
        print("Invalid field!")
    userDB.updateUserProfile(currentUser)
    currentUser = userDB.getUser(currentUser.username)
    return currentUser
