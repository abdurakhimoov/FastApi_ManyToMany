from .database import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped
from sqlalchemy import Integer, String, Table, Column, ForeignKey

actor_movie = Table(
    "actor_movie",
    Base.metadata,
    Column("movie_id", ForeignKey("movies.id"), primary_key=True),
    Column("actor_id", ForeignKey("actors.id"), primary_key=True)
)


class Movie(Base):
    __tablename__ = 'movies'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(150))

    actors = relationship("Actor", secondary=actor_movie, back_populates="movies")

    def __repr__(self):
        return f"id: {self.id}, title: {self.title}"
    


class Actor(Base):
    __tablename__ = 'actors'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(150))
    year: Mapped[int] = mapped_column(Integer)

    movies = relationship("Movie", secondary=actor_movie, back_populates="actors" )

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"
