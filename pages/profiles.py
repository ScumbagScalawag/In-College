from typing import Optional

from common_utils.types.user import User
from common_utils.types.profile import Profile
from common_utils.types.user_database import UserDatabase
from common_utils.types.education import Education
from common_utils.types.experience import Experience


def inputWithExit(prompt: str) -> Optional[str]:
    """Captures input from the user and checks if they want to exit."""
    user_input = input(prompt)
    if user_input.upper() == "X":
        return None
    return user_input


def addEducationToProfile(profile: Profile):
    school_name = inputWithExit("Enter school name (or X to skip): ")
    degree = inputWithExit("Enter degree (or X to skip): ")
    years_attended = inputWithExit("Enter years attended (or X to skip): ")
    profile.education = Education(school_name, degree, years_attended)
    return profile


def addExperiencesToProfile(profile: Profile):
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
            another = input("Do you want to add another experience? (y/n or X to skip): ")
            if another.lower() != "y":
                break
        else:
            print("You've added the maximum number of experiences.")
    profile.experiences = experiences
    return profile


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

    # TODO Only works with y, any other input skips
    add_education = input("Do you want to add education details? (y/n or X to skip): ")
    if add_education.lower() == "y":
        profile = addEducationToProfile(profile)

    # TODO Only works with y, any other input skips
    add_experience = input("Do you want to add experience details? (y/n or X to skip): ")
    if add_experience.lower() == "y":
        profile = addExperiencesToProfile(profile)

    currentUser.profile = profile
    userDB.updateUserProfile(currentUser)
    currentUser = userDB.getUser(currentUser.username)
    return currentUser


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

    return currentUser


def printEditProfile(currentUser: Optional[User] = None) -> Optional[User]:
    userDB = UserDatabase([])
    userDB.loadUsers()

    while True:
        # TODO Make a variable
        print("\n*** Edit Profile ***")
        print("1. Edit Title")
        print("2. Edit Major")
        print("3. Edit University")
        print("4. Edit About")
        print("5. Edit Education")
        print("6. Edit Experiences")
        print("X. Exit")

        choice = input("Select an option: ").lower()

        if choice == "1":
            new_title = input("Enter new title: ")
            currentUser.profile.title = new_title
        elif choice == "2":
            new_major = input("Enter new major: ")
            currentUser.profile.major = new_major
        elif choice == "3":
            new_university = input("Enter new university: ")
            currentUser.profile.university = new_university
        elif choice == "4":
            new_about = input("Enter new about paragraph: ")
            currentUser.profile.about = new_about
        elif choice == "5":
            currentUser.profile = addEducationToProfile(currentUser.profile)
        elif choice == "6":
            while True:
                # List all experiences
                print("\n*** Edit Experiences ***")
                for idx, exp in enumerate(currentUser.profile.experiences, 1):
                    print(f"{idx}. {exp.job_title} at {exp.employer}")

                # Only show the option to add if there are less than 3 experiences
                if len(currentUser.profile.experiences) < 3:
                    print("A. Add New Experience")
                print("X. Exit Experience Editing")

                exp_choice = input(
                    "Select an experience number to edit, 'A' to add, or 'X' to exit: "
                ).lower()

                if exp_choice == "x":
                    break

                if exp_choice == "a" and len(currentUser.profile.experiences) < 3:
                    currentUser.profile = addNewExperience(currentUser.profile)
                    continue

                try:
                    selected_idx = int(exp_choice) - 1
                    selected_exp = currentUser.profile.experiences[selected_idx]
                except (ValueError, IndexError):
                    print("Invalid choice. Please select a valid number.")
                    continue
                while True:
                    # TODO Make a variable for print
                    print(f"\nEditing {selected_exp.job_title} at {selected_exp.employer}")
                    print("1. Job Title")
                    print("2. Employer")
                    print("3. Start Date")
                    print("4. End Date")
                    print("5. Location")
                    print("6. Description")
                    print("X. Exit this Experience Editing")

                    detail_choice = input("Select an option: ").lower()
                    if detail_choice == "1":
                        new_title = input("Enter new job title: ")
                        selected_exp.job_title = new_title
                        userDB.updateUserProfile(currentUser)
                        currentUser = userDB.getUser(currentUser.username)
                    elif detail_choice == "2":
                        new_employer = input("Enter new employer: ")
                        selected_exp.employer = new_employer
                    elif detail_choice == "3":
                        new_start_date = input("Enter new start date: ")
                        selected_exp.date_started = new_start_date
                    elif detail_choice == "4":
                        new_end_date = input("Enter new end date: ")
                        selected_exp.date_ended = new_end_date
                    elif detail_choice == "5":
                        new_location = input("Enter new location: ")
                        selected_exp.location = new_location
                        userDB.updateUserProfile(currentUser)
                        currentUser = userDB.getUser(currentUser.username)
                    elif detail_choice == "6":
                        new_description = input("Enter new description: ")
                        selected_exp.description = new_description
                    elif detail_choice == "x":
                        break
        userDB.updateUserProfile(currentUser)
        currentUser = userDB.getUser(currentUser.username)
        return currentUser


def addNewExperience(profile: Profile) -> Profile:
    print("\n*** Add New Experience ***")

    job_title = inputWithExit("Enter job title (or X to skip): ")
    if not job_title:
        return profile

    employer = inputWithExit("Enter employer (or X to skip): ")
    date_started = inputWithExit("Enter start date (or X to skip): ")
    date_ended = inputWithExit("Enter end date (or X to skip): ")
    location = inputWithExit("Enter location (or X to skip): ")
    description = inputWithExit("Enter description (or X to skip): ")

    new_experience = Experience(
        job_title, employer, date_started, date_ended, location, description
    )
    profile.experiences.append(new_experience)

    print("Experience added successfully!")
    return profile
