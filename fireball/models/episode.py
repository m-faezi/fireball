from restfulpy.orm import DeclarativeBase, Field, \
    ActivationMixin, TimestampMixin
from sqlalchemy import Integer, String


class Episode(ActivationMixin, TimestampMixin, DeclarativeBase):
    __tablename__ = 'episode'

    id = Field(Integer, primary_key=True)

    episode_number = Field(Integer)
    season_id = Field(Integer)
    description = Field(String(48))
    subtitle_id = Field(Integer)
