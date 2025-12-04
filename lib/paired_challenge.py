class Spotifoo:

    def __init__(self):
        self.songs = []


    def add_songs(self, song):
        self.songs.append(song)


    def list_songs(self):
        return self.songs 