from pytube import YouTube
from pytube import Playlist
import sys
import os
import subprocess

def Download(link):

    #ask to where?
    dir = input('download it where? ')

    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_audio_only()

    try:
        youtubeObject.download(dir)
    except:
        print("An error has occurred")

    print("Downloaded :)")

    #ask to convert to wav
        

print('YOUTUBE MP3 DOWNLOADER')
print('----------------------')

#ask 4 url
link = input("Enter the YouTube video URL: ")



Download(link)