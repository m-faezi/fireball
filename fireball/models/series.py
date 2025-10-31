from restfulpy.orm import DeclarativeBase, Field, \
    ActivationMixin, TimestampMixin
from sqlalchemy import Integer, String


class Series(ActivationMixin, TimestampMixin, DeclarativeBase):
    __tablename__ = 'series'

    id = Field(Integer, primary_key=True)

    title = Field(String(48))
    director_id = Field(Integer)
    actor_id = Field(Integer)
    imdb_rate = Field(Integer)
    # oscar_nominations = Field(Integer)
    # oscar_won = Field(Integer)
