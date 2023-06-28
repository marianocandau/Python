from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp #to convert the mp4 to wav then mp3
import re

yturl = str(input("Youtube video url :"))
playlist = Playlist(yturl)
salida ="C:\Repositorio\mp3"

for url in playlist:
    print(url)
for vid in playlist.videos:
    print(vid)
for url in playlist:
    YouTube(url).streams.filter(only_audio=True).first().download(output_path=salida)

for file in os.listdir(salida):
    if re.search('mp4', file):
        print("Converting: " + file)
        mp4_path = os.path.join(salida,file)
        mp3_path = os.path.join(salida,os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
