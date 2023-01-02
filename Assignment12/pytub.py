from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=o_26SGY83-I').streams.first().download()
yt.streams.filter(progressive=True, file_extension='mp4')
# yt.streams.first().download()
# yt.streams.order_by('resolution')
# yt.streams.desc()
# yt.streams.first()
# yt.streams.download()


