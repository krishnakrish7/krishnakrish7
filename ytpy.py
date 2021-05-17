from pytube import youtube
link = input('Enter url')
video = youtube(link)
stream = video.streams.get_highest_resolution()
stream.download()
