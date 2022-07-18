import youtube_dl

ydl_link = ["https://www.youtube.com/watch?v=qH95H5GQ8ro"]

with youtube_dl.YoutubeDL() as ydl:
	ydl.download(ydl_link)
