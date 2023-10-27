import protoapi
from decouple import config
d = config('id')
t = config('secret')
print(d,t)
sp = protoapi.Spotify(d,t)
playlist = sp.getPlaylistData('2kIOW6Ds9jO7d2NWocHkpS')
for i in playlist:
    track = sp.getTrackData(i)
    protoapi.Downloader.downloadSongs(track)

#Cleaning