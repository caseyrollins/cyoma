from rest_framework import serializers
from adventure.models import Adventure, Artist, Song, Playlist


class PlaylistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Playlist
        fields = ('id', 'spotify_url')


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('id', 'adventure_index', 'title', 'spotify_url', 'playlist')


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'name', 'songs', 'spotify_url')


class AdventureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adventure
        fields = ('id', 'artist')
