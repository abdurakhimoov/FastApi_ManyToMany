from pydantic import BaseModel
from typing import List


class MovieBase(BaseModel):
    title: str


class MovieCreate(MovieBase):
    pass


class MovieRead(MovieBase):
    id: int
    actors: List[str] = []

    class Config:
        from_attributes = True


class MoviUpdate(MovieBase):
    pass