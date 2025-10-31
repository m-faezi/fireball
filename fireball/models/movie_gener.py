from restfulpy.orm import DeclarativeBase, Field, \
    ActivationMixin, TimestampMixin
from sqlalchemy import Integer


class MoviesGenre(ActivationMixin, TimestampMixin, DeclarativeBase):
    __tablename__ = 'movies_genre'

    id = Field(Integer, primary_key=True)

    movies_id = Field(Integer)
    genre_id = Field(Integer)
