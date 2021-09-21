from wtforms import *


class FeedbackVO:

    feedbackSubject = StringField
    feedbackId = IntegerField
    feedbackDescription = StringField
    feedbackDate = DateField
    feedbackTime = TimeField
    feedbackRatings = IntegerField
    loginId = IntegerField
