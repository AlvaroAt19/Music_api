from fastapi import FastAPI
from fastapi.params import Depends
from .schemas import Band, Album
from sqlalchemy.orm import Session
from .database import get_db
from .models import BandTable, AlbumTable
from .create_tables import create_tables


create_tables() #Creates tables from models

app = FastAPI()

@app.post("/insert_band")
async def create_band(info: Band, db: Session = Depends(get_db)):
    try:     
        to_create = BandTable(
            name = info.name.lower(),
            style = info.style
        )

        db.add(to_create)
        db.commit()
    
    except:
        
        return {
            "Error": "Band already exists"
        }
    
    else:

        return{
            "sucess" : True,
            "create_id" : to_create.id
        }

@app.post("/insert_album")
async def register_album(info: Album, db: Session = Depends(get_db)):
    try:
        to_create = AlbumTable(
            band_name = info.band_name.lower(),
            name = info.album_name,
            release_year = info.release_year,
            number_of_songs = info.number_of_songs
        )

        db.add(to_create)
        db.commit()
    
    except:

        return {
            "error": "Invalid band name or Album already exists"
        }
    
    else:

        return{
            "sucess" : True,
            "create_id" : to_create.id
        }


@app.get("/album/{name}")
async def album_by_name(name: str, db: Session = Depends(get_db)):
    try:
        row = db.query(AlbumTable).filter(AlbumTable.name == name).all()
        
        return {
            "albuns" : row
        }
    
    except:

        return {
            "Error":"No match"
        }

@app.get("/band/{name}")
async def album_by_name(name: str, db: Session = Depends(get_db)):
    try:
        row = db.query(BandTable).filter(BandTable.name == name).all()
        
        return {
            "Bands" : row
        }
                 
    except:

        return {
            "Error":"No match"
        }

