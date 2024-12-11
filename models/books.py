from sqlalchemy.orm import Mapped, mapped_column
from database.db import Base
from sqlalchemy import String, ForeignKey

class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, index=True) 
    name: Mapped[str] = mapped_column(String(50))
    
