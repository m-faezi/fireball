from restfulpy.orm import DeclarativeBase, Field, \
    ActivationMixin, TimestampMixin
from sqlalchemy import Integer


class MovieActor(ActivationMixin, TimestampMixin, DeclarativeBase):
    __tablename__ = 'movie_actor'

    id = Field(Integer, primary_key=True)

    movie_id = Field(Integer)
    actor_id = Field(Integer)
