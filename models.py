from pydantic import BaseModel


class Note(BaseModel):
    title: str
    content: str
