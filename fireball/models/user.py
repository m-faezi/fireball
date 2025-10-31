from restfulpy.orm import DeclarativeBase, Field, \
    ActivationMixin, TimestampMixin
from sqlalchemy import Integer, String, BOOLEAN


class User(ActivationMixin, TimestampMixin, DeclarativeBase):
    __tablename__ = 'user'

    id = Field(Integer, primary_key=True)

    user_name = Field(String(48))
    password = Field(String(48))
    is_premium = Field(BOOLEAN)
