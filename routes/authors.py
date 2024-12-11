from fastapi import APIRouter, Depends, HTTPException
from database.db import get_db
from schema.authors import AuthorCreate
from models.authors import Author
from typing import List


authors_router = APIRouter()

@authors_router.get("")
def get_all_authors(db = Depends(get_db)):
    authors = db.query(Author).all()
    return authors

@authors_router.post("", response_model=AuthorCreate)
def create_a_author(author: AuthorCreate, db = Depends(get_db)):
    existing_author = db.query(Author).filter(Author.name == author.name).first()
    if existing_author:
        raise HTTPException(status_code=400, detail="Author already exists")
    new_author = Author(name=author.name)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return AuthorCreate( name=new_author.name)

@authors_router.patch("/{id}")
def update_a_author(id: int, db = Depends(get_db)):
    authors = db.query(Author).filter(Author.id == id).first()
    if not authors:
        raise HTTPException(status_code=404, detail="Author not found")
    #db.patch(book)
    db.commit()
    db.refresh(authors)
    return "Author has been updated"

@authors_router.delete("/{id}")
def delete_a_author(id: int, db = Depends(get_db)):
    authors = db.query(Author).filter(Author.id == id).first()
    if not authors:
        raise HTTPException (status_code=404, detail="Author not found")
    db.delete(authors)
    db.commit()
    return "Author Deleted"




