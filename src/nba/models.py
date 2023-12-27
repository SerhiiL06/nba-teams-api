from django.conf import settings
from mongoengine import Document, fields


class Team(Document):
    team_id = fields.IntField()
    team_name = fields.StringField(max_length=settings.TEAM_MAX_LENGTH)
    simple_name = fields.StringField(max_length=settings.TEAM_MAX_LENGTH)
    location = fields.StringField(max_length=settings.TEAM_MAX_LENGTH)
