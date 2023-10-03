class UserNotFoundException(Exception):
    """Custom exception for when a user is not found in the database."""
    pass

class UnexpectedValueInUserAttribute(Exception):
    """Custom exception for when a User has an invlid Value in attribute."""
    pass


