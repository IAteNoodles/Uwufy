import os
import requests
from dotenv import load_dotenv
load_dotenv()

class Spotify:
    def __init__(self) -> None:
        pass
    def setupConnection(self, id, secret):
        
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

    def fetchPlaylistsData(self, link, need = ['all']):
        response = requests.get(link, headers=self.headers)

        if response.status_code == 200:
            print(response)
            data = response.json()
            if need[0] == 'all':
                return data
            else:
                result = list()
                for needed in need:
                    if needed == 'name' or needed == 'description' or needed == 'tracks':
                        result.append(data[needed])
                    fields = needed.split('/')
                    if fields[0] == 'tracks':
                        if fields[1] == 'total':
                            result.append(data['tracks']['total'])
                        if fields[1] == 'items':
                            '''Too much useless data, need to filter it'''
                            result.append(data['tracks']['items'])
                return result             

    def fetchTrackData(self, link, need = ['all']):
        response = requests.get(link, headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            if need[0] == 'all':
                return data
            else:
                ''' make it happen
                result = list()
                for needed in need:
                    if needed == 'name' or needed == 'description' or needed == 'tracks':
                        result.append(data[needed])
                    fields = needed.split('/')
                    if fields[0] == 'tracks':
                        if fields[1] == 'total':
                            result.append(data['tracks']['total'])
                        if fields[1] == 'items':
                            ''''''Too much useless data, need to filter it''''''
                            result.append(data['tracks']['items'])'''
                return 
    
    def saveTrack(self, track_id):
        response = requests.put(f'https://api.spotify.com/v1/me/tracks?ids={track_id}', headers=self.headers)
        return response
    
    def removeTrack(self, track_id):
        response = requests.delete(f'https://api.spotify.com/v1/me/tracks?ids={track_id}', headers=self.headers)
        return response
    
    def followPlaylist(self, playlist_id):
        response = requests.post(f'https://api.spotify.com/v1/playlists/{playlist_id}/followers', headers=self.headers)
        return response
    
    def unfollowPlaylist(self, playlist_id):
        response = requests.delete(f'https://api.spotify.com/v1/playlists/{playlist_id}/followers', headers=self.headers)
        return response

    def createPlaylist(self, name, description):
        response = requests.post('https://api.spotify.com/v1/me/playlists', headers=self.headers, json={"name": name, "description": description})
        return response    


link = 'https://api.spotify.com/v1/playlists/7tm08i6ITfMB3itnUbeSV2?si=6e10edd4a6ec4ff5'
isPlaylist = lambda link : True if 'playlist' in link else False
id = os.environ.get('id')
secret = os.environ.get('secret')
x=Spotify()
print(x.setupConnection(id, secret))
print(isPlaylist(link))
print(x.fetchPlaylistsData(link=link, need=['name', 'tracks/total', 'tracks/items']))