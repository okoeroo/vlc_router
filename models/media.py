from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy import Column, Integer, String
from funcs.database import Base


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True, index=True)
    friendly_name = Column(String)
    filepath = Column(String)

    def __repr__(self):
        return f"<Media::{self.friendly_name}>"


class MovingData(Base):
    __tablename__ = 'movingdata'
    id = Column(Integer, primary_key=True, index=True)
    friendly_name = Column(String)
    filepath = Column(String)

    def __repr__(self):
        return f"<MovingData::{self.friendly_name}>"
