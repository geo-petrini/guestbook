from datetime import datetime
from .database import BaseModel
from peewee import CharField, DateTimeField, DoesNotExist

class Message(BaseModel):
    name = CharField(unique=True, max_length=255)
    message = CharField(max_length=255)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        #peewee unisce le classi Meta in una gerarchia, quindi ereditiamo da BaseModel.Meta
        table_name = 'messages'

    def __repr__(self):
        return f"<Message id={self.id}, name='{self.name}', message='{self.message}'>"



def get_message_by_name(name):
    try:
        #come select ma solo 1 record e genera DoesNotExist se non esiste
        return Message.get(Message.name == name)
    except DoesNotExist:
        return None