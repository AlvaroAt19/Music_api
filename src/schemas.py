from pydantic import BaseModel

class Band(BaseModel):
    name : str
    style : str

class Album(BaseModel):
    band_name: str
    album_name: str
    release_year : int
    number_of_songs: int