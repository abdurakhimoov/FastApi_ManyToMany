from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from schemas import actor_schema
from services.actor_service import (
    create_actor,
    read_by_actor,
    read_all_actor,
    update_actor,
    delete_actor
)

router = APIRouter(
    prefix="/actors",
    tags=["Actors"]
)

@router.post("/", response_model=actor_schema.ActorRead, status_code=status.HTTP_201_CREATED)
def add_actor(actor: actor_schema.ActorCreate, db: Session = Depends(get_db)):
    return create_actor(db=db, actor=actor)

@router.get("/", response_model=List[actor_schema.ActorRead])
def get_all_actors(db: Session = Depends(get_db)):
    return read_all_actor(db=db)

@router.get("/{actor_id}", response_model=actor_schema.ActorRead)
def get_actor(actor_id: int, db: Session = Depends(get_db)):
    actor = read_by_actor(id=actor_id, db=db)
    if actor is None:
        raise HTTPException(status_code=404, detail="Aktyor topilmadi")
    return actor

@router.put("/{actor_id}", response_model=actor_schema.ActorRead)
def edit_actor(actor_id: int, actor_data: actor_schema.ActorUpdate, db: Session = Depends(get_db)):
    existing_actor = read_by_actor(id=actor_id, db=db)
    if existing_actor is None:
        raise HTTPException(status_code=404, detail="Yangilash uchun aktyor topilmadi")
    
    return update_actor(id=actor_id, db=db, actor_data=actor_data)

@router.delete("/{actor_id}")
def remove_actor(actor_id: int, db: Session = Depends(get_db)):
    success = delete_actor(id=actor_id, db=db)
    if not success:
        raise HTTPException(status_code=404, detail="O'chirish uchun aktyor topilmadi")
    return {"message": "Aktyor muvaffaqiyatli o'chirildi"}