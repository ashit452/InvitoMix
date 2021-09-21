from wtforms import *


class LoginVO:
    loginId = IntegerField
    loginUserName = StringField
    loginPassword = StringField
    loginRole = StringField
    loginStatus = StringField
