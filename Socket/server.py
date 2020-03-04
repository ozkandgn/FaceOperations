from flask import Flask, render_template
from flask_socketio import SocketIO


class VideoTaker():
	def __init__(self):
		#initial flask variables
		self.app = Flask(__name__)
		self.app.config['SECRET_KEY'] = 'high_top_awesome_secret_key_dont_listen'
		self.socketio = SocketIO(self.app, ping_timeout= 500000)

	def listen(self,run_func):
		#listening
		@self.socketio.on("videoprocess")
		def reciever(data):
			print("recieved "+str(data))
			#sending data
			#self.socketio.emit("status",{"status":"start"})
			#running sended function
			data = run_func(data["url"],data["name"])
			#emit functions closed because there is a session error
			#self.socketio.emit("status",{"status":"end","data":str(data)})
			
		#start socketio
		self.socketio.run(self.app,debug=True,use_reloader=False)