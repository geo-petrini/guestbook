# models/__init__.py
from .database import db
from .message import Message, get_message_by_name

__all__ = ["db", "Message", "get_message_by_name"]
