from pytube import YouTube
import uuid
import os

def get_audio(url):
    yt = YouTube(url)
    
    filePath = yt.streams.filter(only_audio = True).first().download()
    
    os.rename(filePath, yt.title + ".mp3")
    return yt.title + ".mp3"

# get_audio('https://www.youtube.com/watch?v=3vSxHROQ4Hs')

# print('THAILAND IN 30 SECONDS | CINEMATIC VIDEO| 4k.'=='THAILAND IN 30 SECONDS | CINEMATIC VIDEO| 4k.')
