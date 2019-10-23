from libraries.spotify.spotifyReqLib import spotify as Spotify
from libraries.tools.jsonFunctions import getJsonContents

spotifyCredentials = getJsonContents('libraries/credentials.json')["spotify"]
spotify = Spotify(spotifyCredentials)
print("Spotify Initialized")

def addCurrentTrackToPlst(plid):
	print("kicking Off Spottify Add")
	currentTrackId = spotify.getCurrentTrack()
	print(spotify.addSongToPlaylistById(plid,currentTrackId))

def killToken():
	spotify.killToken()
	print("Spotify Token Cleared")