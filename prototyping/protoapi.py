import requests
class Spotify:
    
    def __init__(self,id,secret):
        # Set up authentication
        auth_url = 'https://accounts.spotify.com/api/token'
        auth_data = {
        'grant_type': 'client_credentials',
        'client_id': id,
        'client_secret': secret,
        }
        auth_response = requests.post(auth_url, data=auth_data)
        response = auth_response.json()
        print(response)
        auth_token = response['access_token']
        self.headers = {"Authorization": f"Bearer {auth_token}"}
        
        
    def getPlaylistData(self, playlist_id):
        response = requests.get(f"https://api.spotify.com/v1/playlists/{playlist_id}", headers=self.headers)
        data = response.json()
        links = []
        for i in data['tracks']['items']:
            links.append(i['track']['external_urls']['spotify'])

        # Extracting track_ids 
        track_ids = []
        for i in links:
            track_ids.append(i.split('/')[4])
        print(track_ids)
        return track_ids

    def getTrackData(self, track_id):
        response = requests.get(f"https://api.spotify.com/v1/tracks/{track_id}", headers=self.headers)
        data = response.json()
        name = data['name']
        return name

class Downloader:
    def downloadSongs(name):
        command = "yt-dlp -x --audio-format m4a ytsearch:'{name}'".format(name=name)
        print(command)
        import subprocess
        import os
        #Run the command
        os.system(command)
        #output = subprocess.check_output(command, shell=True)
        #print(output)
       

class Lyrics:
    def getLyrics(name):
        pass    
#Cleaning
