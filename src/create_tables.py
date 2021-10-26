from .database import Base, engine
from .models import BandTable, AlbumTable

def create_tables():
    """Create tables from models"""
    Base.metadata.create_all(engine)