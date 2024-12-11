from fastapi import FastAPI, Depends, HTTPException
from routes.books import books_router
from routes.authors import authors_router
from database.db import Base, engine
from models.authors import Author
from models.books import Book


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(books_router, prefix="/books", tags=["Books"])
app.include_router(authors_router, prefix="/authors", tags=["Authors"])

print("Hello")

print("Second")