from restfulpy.orm import DeclarativeBase, Field, \
    ActivationMixin, TimestampMixin
from sqlalchemy import Integer, String


class Actor(ActivationMixin, TimestampMixin, DeclarativeBase):
    __tablename__ = 'actor'

    id = Field(Integer, primary_key=True)

    first_name = Field(String(48))
    last_name = Field(String(48))
    oscar_nominations = Field(Integer)
    oscar_won = Field(Integer)
