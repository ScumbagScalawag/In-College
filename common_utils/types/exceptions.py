class UserNotFoundException(Exception):
    """Custom exception for when a user is not found in the database."""

    pass


class JobNotFoundException(Exception):
    """Custom exception for when a job is not found in the database."""

    pass


class UnexpectedValueInUserAttribute(Exception):
    """Custom exception for when a User has an invlid Value in attribute."""

    pass


class MaximumNumberOfUsers(Exception):
    """Custom exception for when a user cannot be added to the UserDatabase becuase of size limitation"""

    pass


class MaximumNumberOfJobs(Exception):
    """Custom exception for when a job cannot be added to the JobDatabase becuase of size limitation"""

    pass
