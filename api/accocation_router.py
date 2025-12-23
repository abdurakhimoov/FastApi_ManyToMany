from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.association_service import add_actor_to_movie

router = APIRouter(
    prefix="/accocation",
    tags=["Actors"]
)


from schemas import movie_schema
from db.database import get_db




@router.post("/{movie_id}/actors/{actor_id}", response_model=movie_schema.MovieRead)
def link_actor_to_movie(movie_id: int, actor_id: int, db: Session = Depends(get_db)):
    movie = add_actor_to_movie(db=db, movie_id=movie_id, actor_id=actor_id)
    if not movie:
        raise HTTPException(
            status_code=404, 
            detail="Kino yoki Aktyor topilmadi yoki ular allaqachon bog'langan"
        )
    return movie