# etl_pipeline.py
from ml_component.server import db  
from ml_component.server.models import Song
import pandas as pd


print("Starting...")
DATA_PATH = "data/"
file_name = "April2019.csv"

df = pd.read_csv(DATA_PATH+file_name)
assert(df.shape == (130663, 17))

for row in df.values:
    curr_song = Song(
        artist_name=row[0],
        track_id=row[1],
        track_name=row[2],
        acousticness=row[3],
        danceability=row[4],
        duration_ms=row[5],
        energy=row[6],
        instrumentalness=row[7],
        key=row[8],
        liveness=row[9],
        loudness=row[10],
        mode=row[11],
        speechiness=row[12],
        tempo=row[13],
        time_signature=row[14],
        valence=row[15],
        popularity=row[16]
    )
    db.session.add(curr_song)
    db.session.commit()


# sanity check 
assert(len(Song.query.all()) == 130663)
print("done.")