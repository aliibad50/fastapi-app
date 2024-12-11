from fastapi import APIRouter, Depends, HTTPException
from database.db import get_db
from models.books import Book
from schema.books import BookCreate
from typing import List

books_router = APIRouter()

@books_router.get("", response_model=List[BookCreate])
def get_all_books(db = Depends(get_db)):
    books = db.query(Book).all()
    return books

@books_router.post("", response_model=BookCreate)
def create_a_book(book: BookCreate, db = Depends(get_db)):
    new_book = Book(name=book.name, author_id=book.author_id)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@books_router.patch("/{id}")
def update_a_book(id: int, db = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    #db.patch(book)
    db.commit()
    db.refresh(book)
    return "Book has been updated"

@books_router.delete("/{id}")
def delete_a_book(id: int, db = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first()
    if not book:
        raise HTTPException (status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return "Book Deleted"





    




