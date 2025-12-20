from typing import List
from pydantic import BaseModel


class ActorBase(BaseModel):
    name: str
    year: int


class ActorCreate(ActorBase):
    pass


class ActorRead(ActorBase):
    id: int
    movies: List[str] = []

    class Config:
        from_attributes = True


class ActorUpdate(ActorBase):
    pass