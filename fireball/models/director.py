from restfulpy.orm import DeclarativeBase, Field, \
    ActivationMixin, TimestampMixin
from sqlalchemy import Integer, String


class Director(ActivationMixin, TimestampMixin, DeclarativeBase):
    __tablename__ = 'director'

    id = Field(Integer, primary_key=True)

    first_name = Field(String(48))
    last_name = Field(String(48))
    oscar_nominations = Field(Integer)
    oscar_won = Field(Integer)
