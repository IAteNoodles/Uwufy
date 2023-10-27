import yt_dlp

# Create a yt_dlp YoutubeDL object
ytdl = yt_dlp.YoutubeDL()

'''info = ytdl.extract_info('ytsearch: despacito', download = False)
url = info["url"]
print(url)
# Define the search query
search_query = "Welcome to The Internet"  # Replace with your desired search query

# Prepare the search options
search_options = {
    'default_search': 'ytsearch',  # Use YouTube search
    'max_results': 5,  # You can adjust the number of search results to retrieve
    'quiet': True,
    'simulate': True,
    'forceurl': True
}
'''
command = "yt-dlp ytsearch:despacito --get-url"
import os
x=os.system(command=command)
print(x)
'''# Search for the video
search_results = ytdl.extract_info("ytsearch:" + search_query, download=False, extra_info=search_options)
print(search_results)
'''
