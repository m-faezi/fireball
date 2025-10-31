from restfulpy.orm import DeclarativeBase, Field, \
    ActivationMixin, TimestampMixin
from sqlalchemy import Integer


class SeriesGenre(ActivationMixin, TimestampMixin, DeclarativeBase):
    __tablename__ = 'series_genre'

    id = Field(Integer, primary_key=True)

    series_id = Field(Integer)
    genre_id = Field(Integer)
