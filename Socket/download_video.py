import urllib.request

def video_downloader(url_link, video_name):
	try:
		urllib.request.urlretrieve(url_link, video_name)
		print("video_download success!!")
		return True
	except:
		print("video_download occurred an error!!")
		return False