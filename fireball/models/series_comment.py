from restfulpy.orm import DeclarativeBase, Field, \
    ActivationMixin, TimestampMixin
from sqlalchemy import Integer, String


class SeriesComment(ActivationMixin, TimestampMixin, DeclarativeBase):
    __tablename__ = 'series_comment'

    id = Field(Integer, primary_key=True)

    series_id = Field(Integer)
    user_id = Field(Integer)
    comment = Field(String(48))
