import youtube_dl
from time import sleep

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(title)s.%(ext)s'})

with ydl:
    result = ydl.extract_info(
        'https://www.youtube.com/watch?v=WLIfbiTUMiU',
        download=True # We just want to extract the info
    )

if 'entries' in result:
    # Can be a playlist or a list of videos
    video = result['entries'][0]
else:
    # Just a video
    video = result

sleep(3)
metadata = False

if metadata == True:
    print(video)
