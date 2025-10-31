from restfulpy.orm import DeclarativeBase, Field, \
    ActivationMixin, TimestampMixin
from sqlalchemy import Integer


class SeriesActor(ActivationMixin, TimestampMixin, DeclarativeBase):
    __tablename__ = 'series_actor'

    id = Field(Integer, primary_key=True)

    series_id = Field(Integer)
    actor_id = Field(Integer)
