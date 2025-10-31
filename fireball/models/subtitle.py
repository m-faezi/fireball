from restfulpy.orm import DeclarativeBase, Field, \
    ActivationMixin, TimestampMixin
from sqlalchemy import Integer, String


class Subtitle(ActivationMixin, TimestampMixin, DeclarativeBase):
    __tablename__ = 'subtitle'

    id = Field(Integer, primary_key=True)

    description = Field(String(48))
