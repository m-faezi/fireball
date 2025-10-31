from restfulpy.orm import DeclarativeBase, Field, \
    ActivationMixin, TimestampMixin
from sqlalchemy import Integer, String


class Genre(ActivationMixin, TimestampMixin, DeclarativeBase):
    __tablename__ = 'genre'

    id = Field(Integer, primary_key=True)

    title = Field(String(48))
