# ml_component/server/models.py
from ml_component.server import db  


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String)
    track_id = db.Column(db.String)
    track_name = db.Column(db.String)
    acousticness = db.Column(db.Float)
    danceability = db.Column(db.Float)
    duration_ms = db.Column(db.Integer)
    energy = db.Column(db.Float)
    instrumentalness = db.Column(db.Float)
    key = db.Column(db.Integer)
    liveness = db.Column(db.Float)
    loudness = db.Column(db.Float)
    mode = db.Column(db.Integer)
    speechiness = db.Column(db.Float)
    tempo = db.Column(db.Float)
    time_signature = db.Column(db.Integer)
    valence = db.Column(db.Float)
    popularity = db.Column(db.Integer)

    def to_json(self):
        return {
            "id": self.id,
            "track_id": self.track_id, 
            "artist_name": self.artist_name,
            "track_name": self.track_name,
            "acousticness": self.acousticness,
            "danceability": self.danceability,
            "duration_ms": self.duration_ms,
            "energy": self.energy,
            "instrumentalness": self.instrumentalness,
            "key": self.key,
            "liveness": self.liveness,
            "loudness": self.loudness,
            "mode": self.mode,
            "speechiness": self.speechiness,
            "tempo": self.tempo,
            "time_signature": self.time_signature,
            "valence": self.valence,
            "popularity": self.popularity
        }