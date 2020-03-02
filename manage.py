from Socket.server import VideoTaker
from Socket.download_video import video_downloader
from Image_Processes.main import start_image_processing

def download_function(url_link,video_name):
	is_download = video_downloader(url_link,video_name)
	print("is ",is_download)


if __name__ == "__main__":

	video_taker = VideoTaker()

	print("listen start")
	video_taker.listen(download_function)
	print("listen end")
