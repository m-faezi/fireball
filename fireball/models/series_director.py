from restfulpy.orm import DeclarativeBase, Field, \
    ActivationMixin, TimestampMixin
from sqlalchemy import Integer


class SeriesDirector(ActivationMixin, TimestampMixin, DeclarativeBase):
    __tablename__ = 'series_director'

    id = Field(Integer, primary_key=True)

    series_id = Field(Integer)
    director_id = Field(Integer)
