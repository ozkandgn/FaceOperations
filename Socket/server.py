from flask import Flask, render_template
from flask_socketio import SocketIO


class VideoTaker():
	def __init__(self):
		#initial flask variables
		self.app = Flask(__name__)
		self.app.config['SECRET_KEY'] = 'high_top_awesome_secret_key_dont_listen'
		self.socketio = SocketIO(self.app)

	def listen(self,run_func):
		#listening
		@self.socketio.on("HelloS")
		def reciever(data):
			print("recieved "+str(data))
			#sending data
			self.socketio.emit("HelloTooC","{'Hello too client':'from server'}")
			url_link = "https://s2.dosya.tc/en2.php?a=server12/39jm50/videotest.mp4&b=d20780ff8a5a185085c1cbe776a8a8b5"
			video_name = "videotest.mp4"
			#running sended function
			run_func(url_link,video_name)
			
		#start socketio
		self.socketio.run(self.app,debug=True,use_reloader=False)