from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
import uuid


class Message(BaseModel):
    id = uuid.uuid4()
    msg: str
    timestamp = str(datetime.now())

class Chat(BaseModel):
    token: str
    messages: List[Message]
    email: str
    session_start = str(datetime.now())

class DataObject(BaseModel):
    file_directory: str
    title : str 
    embedding : List[float]

