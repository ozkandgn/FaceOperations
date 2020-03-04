import socketio as socket
import eventlet

print("client")
client = socket.Client()

client.connect('http://127.0.0.1:5000')

url_link = "https://s2.dosya.tc/en2.php?a=server12/39jm50/videotest.mp4&b=f15c1faf1c26a407eae05c0329654d3d"
video_name = "videotest.mp4"

#send data from server
client.emit("videoprocess",{'url':url_link,'name':video_name})
print("sended")
#listen server
@client.on('status')
def Set(data):
	print("recieved ",str(data))
	if (data["status"]=="end"):
		client.disconnect()
		print("end")
