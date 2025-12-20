from sqlalchemy.orm  import Session
from schemas import movie_schema
from db import Movie
from typing import Optional, List

def create_movie(db: Session, movie: movie_schema.MovieCreate) -> Movie:
    db_movie = Movie(title=movie.title)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def read_by_movie(id: int, db: Session) -> Optional[Movie]:
    db_movie = db.get(Movie, id)
    return db_movie


def read_all_movie(db: Session) -> List[Movie]:
    db_movie = db.query(Movie).all()
    return db_movie


def update_movie(id: int, db: Session, movie_data: movie_schema.MovieUpdate) -> Optional[Movie]:
    movie = db.get(Movie, id)
    
    if movie_data is not None:
        movie.title = movie_data.title
    
    db.commit()
    db.refresh(movie)
    return movie


def delete_movie(id: int, db: Session) -> bool:
    movie = db.get(Movie, id)
    if movie:
        db.delete(movie)
        db.commit()
        return True
    return False