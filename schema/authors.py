from pydantic import BaseModel

class AuthorCreate(BaseModel):
    name: str
    book_id: int|None= None



