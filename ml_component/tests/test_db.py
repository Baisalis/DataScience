import unittest 
from ml_component.server import db 
from ml_component.server.models import Song


class TestDB(unittest.TestCase):
    def test_song_count(self):
        songs = Song.query.all() 
        self.assertEqual(len(songs), 130663)