from pytube import YouTube
import os

salida ="C:\Repositorio\mp3"
yturl = str(input("Youtube video url :"))
url = YouTube(yturl)

audio_stream = url.streams.filter(only_audio=True).first()
out_file = audio_stream.download(output_path=salida)

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)