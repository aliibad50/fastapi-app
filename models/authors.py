from sqlalchemy.orm import Mapped, mapped_column
from database.db import Base
from sqlalchemy import String

class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True, index=True) 
    name: Mapped[str] = mapped_column(String(50))
    
