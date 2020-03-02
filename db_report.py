# db_report.py
from ml_component.server import db 
from ml_component.server.models import Song


print("DB REPORT:")
songs = Song.query.all() 
print(f"Song #: {len(songs)}")
print(f"Example track_id: {songs[0].track_id}")