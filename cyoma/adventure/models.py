from django.db import models


class Playlist(models.Model):
    id = models.AutoField(primary_key=True)
    spotify_url = models.URLField(blank=True)
    # songs


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    aventure_index = models.IntegerField() # 1 - 14
    title = models.CharField(max_length=100)
    spotify_url = models.URLField()
    playlist = models.ForeignKey(Playlist, blank=True)
    # artists
    # album


class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    songs = models.ForeignKey(Song)
    spotify_url = models.URLField()


class Adventure(models.Model):
    id = models.AutoField(primary_key=True)
    artist = models.ForeignKey(Artist)


# {
#     '<artist-id>': {
#         '1<song-id>': {
#             '3<song-id>': {
#                 '7<song-id>': '<playlist-id>'
#                 '8<song-id>': '<playlist-id>',
#             },
#             '4<song-id>': {
#                 '9<song-id>': '<playlist-id>',
#                 '10<song-id>': '<playlist-id>',
#             }
#         },
#         '2<song-id>': {
#             '5<song-id>': {
#                 '11<song-id>': '<playlist-id>',
#                 '12<song-id>': '<playlist-id>'
#             },
#             '6<song-id>': {
#                 '13<song-id>': '<playlist-id>',
#                 '14<song-id>': '<playlist-id>'
#             }
#         }
#     }
# }


