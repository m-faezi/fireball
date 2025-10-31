from restfulpy.orm import DeclarativeBase, Field, \
    ActivationMixin, TimestampMixin
from sqlalchemy import Integer


class MoviesWatchList(ActivationMixin, TimestampMixin, DeclarativeBase):
    __tablename__ = 'movies_watch_list'

    id = Field(Integer, primary_key=True)

    movies_id = Field(Integer)
    user_id = Field(Integer)
