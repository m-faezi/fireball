from restfulpy.orm import DeclarativeBase, Field, \
    ActivationMixin, TimestampMixin
from sqlalchemy import Integer


class MovieDirector(ActivationMixin, TimestampMixin, DeclarativeBase):
    __tablename__ = 'movie_director'

    id = Field(Integer, primary_key=True)

    movie_id = Field(Integer)
    director_id = Field(Integer)
