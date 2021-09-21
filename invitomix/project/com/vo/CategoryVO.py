from wtforms import *


class CategoryVO:
    categoryId = IntegerField
    categoryName = StringField
    categoryDescription = StringField
    categoryStatus = StringField
