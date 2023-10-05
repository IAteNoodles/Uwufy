import yt_dlp

def download(song):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl':song+'ot.mp3',
        '--ffmpeg-location': '/usr/bin/'} 
     
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch1:{song}", download=True)
        video_url = info['entries'][0]['url']
        ydl.download([video_url])
import requests
import sys
import os
from dotenv import load_dotenv
load_dotenv()


id = os.environ.get('id')
secret = os.environ.get('secret')

# Set up authentication
auth_url = 'https://accounts.spotify.com/api/token'
auth_data = {
    'grant_type': 'client_credentials',
    'client_id': id,
    'client_secret': secret,
}

auth_response = requests.post(auth_url, data=auth_data)
auth_token = auth_response.json()['access_token']

link = sys.argv[1]

# Extract the track or playlist ID from the link
if "track" in link:
    track_id = link.split("/track/")[1]
    api_url = f"https://api.spotify.com/v1/tracks/{track_id}"
elif "playlist" in link:
    playlist_id = link.split("/playlist/")[1]
    api_url = f"https://api.spotify.com/v1/playlists/{playlist_id}"

# Make the API request
headers = {"Authorization": f"Bearer {auth_token}"}
response = requests.get(api_url, headers=headers)

# Check the API response
if response.status_code == 200:
    playdata = response.json()
     # Extract and print the names of every song in the playlist
    print("Songs in the Playlist:")
    for track in playdata["tracks"]["items"]:
        download(track["track"]["name"])
else:

    print("Error:", response.status_code)

