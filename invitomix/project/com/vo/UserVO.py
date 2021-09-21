from wtforms import *


class UserVO:

    userId = IntegerField
    userFirstName = StringField
    userLastName = StringField
    userGender = StringField
    userContact = IntegerField
    user_loginId = IntegerField
    loginStatus = StringField
