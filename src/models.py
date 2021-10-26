from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column
from .database import Base


class BandTable(Base):
    __tablename__ = 'band'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    style = Column(String, nullable=False)
    albuns = relationship("AlbumTable")


    def __repr__(self) -> str:
        return {"id": self.id, "name":self.name, "style":self.style}


class AlbumTable(Base):
    __tablename__ = 'album'
    
    id = Column(Integer, primary_key=True)
    band_name = Column(String, ForeignKey('band.name'))
    name = Column(String, nullable=False)
    release_year = Column(Integer, nullable=False)
    number_of_songs = Column(Integer, nullable=False)


    def __repr__(self) -> str:
        return {"id": self.id, "band":self.band_name, "release year":self.release_year, "number of songs": self.number_of_songs}