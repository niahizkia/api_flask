import datetime
from peewee import *

DATABASE = SqliteDatabase('tweets.db')


class BaseModel(Model):
    class Meta:
        database = DATABASE


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()

class Message(BaseModel):
    user_id     = ForeignKeyField(User, backref='messages')
    content     = TextField()
    published_at= DateTimeField(default=datetime.datetime.now())


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Message, User], safe=True)
    DATABASE.close()