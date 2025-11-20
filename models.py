from peewee import *
from datetime import datetime

# Il database verrà configurato da app.py
db = DatabaseProxy()


class Message(Model):
    name = CharField(unique=True, max_length=255)
    message = CharField(max_length=255)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
        table_name = 'messages'

    def __repr__(self):
        return f"<Message id={self.id}, name='{self.name}', message='{self.message}'>"



def get_message_by_name(name):
    try:
        #come select ma solo 1 record e genera DoesNotExist se non esiste
        return Message.get(Message.name == name)
    except DoesNotExist:
        return None