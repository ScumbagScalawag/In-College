from common_utils.types.user import User
from pages.notifications import deletedJobNotification
from tests.shared import singleUser

def test_deletedJobsNotification():
    user = User.dictToUser(singleUser)
    user = deletedJobNotification(user)

    if user != None:
        user.applicationDeleted = "Software Engineering"
    else:
        raise(TypeError("singleUser dict failed to convert to User"))

    user = deletedJobNotification(user)
