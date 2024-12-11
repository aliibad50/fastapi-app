from pydantic import BaseModel

class BookCreate(BaseModel):
    name: str
    author_id: int

