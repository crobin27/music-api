from fastapi import APIRouter, HTTPException
from enum import Enum
from src import database as db
from fastapi.params import Query
from pydantic import BaseModel
import sqlalchemy as sa

router = APIRouter()


class TrackJson(BaseModel):
    title: str
    album_id: str
    runtime: int
    genre_id: str


@router.post("/tracks/", tags=["tracks"])
def add_track(track_id: int, track: TrackJson):
    """ """

    with db.engine.connect() as conn:
        check_album_exists_stmt = (
            sa.select(db.albums.c.album_id)
            .select_from(db.albums)
            .where(db.albums.c.album_id == track.album_id)
        )

        if not (conn.execute(check_album_exists_stmt)):
            raise HTTPException(status_code=404, detail="Album not found.")

        get_artist_id_stmt = (
            sa.select(db.artists.c.artist_id)
            .select_from(db.albums)
            .where(db.albums.c.album_id == track.album_id)
        )

        artist_id = (conn.execute(get_artist_id_stmt).fetchone())._asdict()


@router.get("/tracks/{track_id}", tags=["tracks"])
def get_track(track_id: int):
    """
    This endpoint returns a single track by its identifier. For each track it returns:
    * `track_id`: the internal id of the track.
    * `title`: the title of the track.
    * `artists`: the artist of the track.
    * `album`: the album the track is from.
    * `runtime`: length of the track.
    * `genre`: genre of the track.

    Each artist is represented by a dictionary with the following keys:
    * `artist_id`: the internal id of the artist.
    * `name`: The name of the artist.
    """

    json = {"test"}
    return json

    # raise HTTPException(status_code=404, detail="track not found.")
