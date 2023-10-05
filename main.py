import os
import requests
from dotenv import load_dotenv
load_dotenv()

class Spotify:
    def __init__(self) -> None:
        pass
    def setupConnection(self, id, secret) -> bool:
        
        # Set up authentication
        auth_url = 'https://accounts.spotify.com/api/token'
        auth_data = {
        'grant_type': 'client_credentials',
        'client_id': id,
        'client_secret': secret,
        }
        auth_response = requests.post(auth_url, data=auth_data)
        auth_token = auth_response.json()['access_token']
        self.headers = {"Authorization": f"Bearer {auth_token}"}

    def fetchPlaylistsData(self, link):
        pass
        


link = 'https://open.spotify.com/playlist/7tm08i6ITfMB3itnUbeSV2?si=6e10edd4a6ec4ff5'
isPlaylist = lambda link : True if 'playlist' in link else False
id = os.environ.get('id')
secret = os.environ.get('secret')
x=Spotify()
print(x.setupConnection(id, secret))
print(isPlaylist(link))