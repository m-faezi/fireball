from restfulpy.orm import DeclarativeBase, Field, \
    ActivationMixin, TimestampMixin
from sqlalchemy import Integer


class SeriesWatchList(ActivationMixin, TimestampMixin, DeclarativeBase):
    __tablename__ = 'series_watch_list'

    id = Field(Integer, primary_key=True)

    series_id = Field(Integer)
    user_id = Field(Integer)
