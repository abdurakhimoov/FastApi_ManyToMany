from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from schemas import movie_schema
from services.movie_service import (
    create_movie, 
    read_by_movie, 
    read_all_movie, 
    update_movie, 
    delete_movie
)

router = APIRouter(
    prefix="/movies",
    tags=["Movies"]
)

@router.post("/", response_model=movie_schema.MovieRead, status_code=status.HTTP_201_CREATED)
def add_movie(movie: movie_schema.MovieCreate, db: Session = Depends(get_db)):
    return create_movie(db=db, movie=movie)

@router.get("/", response_model=List[movie_schema.MovieRead])
def get_all_movies(db: Session = Depends(get_db)):
    return read_all_movie(db=db)

@router.get("/{movie_id}", response_model=movie_schema.MovieRead)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = read_by_movie(id=movie_id, db=db)
    if movie is None:
        raise HTTPException(status_code=404, detail="Kino topilmadi")
    return movie

@router.put("/{movie_id}", response_model=movie_schema.MovieRead)
def edit_movie(movie_id: int, movie_data: movie_schema.MovieUpdate, db: Session = Depends(get_db)):
    movie = update_movie(id=movie_id, db=db, movie_data=movie_data)
    if movie is None:
        raise HTTPException(status_code=404, detail="Yangilash uchun kino topilmadi")
    return movie

@router.delete("/{movie_id}")
def remove_movie(movie_id: int, db: Session = Depends(get_db)):
    success = delete_movie(id=movie_id, db=db)
    if not success:
        raise HTTPException(status_code=404, detail="O'chirish uchun kino topilmadi")
    return {"message": "Kino muvaffaqiyatli o'chirildi"}