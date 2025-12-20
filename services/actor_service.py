from typing import Optional, List
from sqlalchemy.orm import Session
from schemas import actor_schema
from db import Actor

def create_actor(db: Session, actor: actor_schema.ActorCreate) -> Actor:
    db_actor = Actor(name=actor.name, year=actor.year)
    db.add(db_actor)
    db.commit()
    db.refresh(db_actor)
    return db_actor


def read_by_actor(id: int, db: Session) -> Optional[Actor]:
    actor = db.get(Actor, id)
    return actor


def read_all_actor(db: Session) -> List[Actor]:
    actors = db.query(Actor).all()
    return actors


def update_actor(id: int, db: Session, actor_data: actor_schema.ActorUpdate) -> Optional[Actor]:
    actor = db.get(Actor, id)

    if actor_data.name is not None:
        actor.name = actor_data.name
    if actor_data.year is not None:
        actor.year = actor_data.year

    db.commit()
    db.refresh(actor)
    return actor


def delete_actor(id: int, db: Session) -> bool:
    actor = db.get(Actor, id)
    if actor:
        db.delete(actor)
        db.commit()
        return True
    return False