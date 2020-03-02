from Socket.server import VideoTaker
from Operations.download_video import video_downloader
from Image_Processes.main import video_processing

def download_function(url_link,video_name):
	is_download = video_downloader(url_link,video_name)
	if is_download:
		processing_function(video_name)

def processing_function(video_name):
	video_processing(video_name)

if __name__ == "__main__":

	video_taker = VideoTaker()

	print("listen start")
	video_taker.listen(download_function)
	print("listen end")
