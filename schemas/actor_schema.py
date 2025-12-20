from typing import List
from pydantic import BaseModel


class ActorModel(BaseModel):
    name: str
    year: int


class ActorCreate(ActorModel):
    pass


class ActorRead(ActorModel):
    id: int
    movies: List[str] = []

    class Config:
        from_attributes = True