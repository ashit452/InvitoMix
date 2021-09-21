from wtforms import *


class SuggestionVO:

    suggestionSubject = StringField
    suggestionId = IntegerField
    suggestionDescription = StringField
    suggestionFile = StringField
    suggestionDate = DateField
    suggestionTime = TimeField
    suggestionReply = StringField
    suggestionStatus = StringField
    loginId = IntegerField
