from sqlalchemy.orm import Session
from typing import List, Optional
from db import Movie, Actor


def add_actor_to_movie(db: Session, actor_id: int, movie_id: int):
    actor = db.get(Actor, actor_id)
    movie = db.get(Movie, movie_id)

    if actor and movie and actor not in movie.actors:
        movie.actors.append(actor)
        db.commit()
        db.refresh(movie)
        return movie
    return None