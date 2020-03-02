import socketio as socket
import eventlet

print("client")
client = socket.Client()

client.connect('http://127.0.0.1:5000')

#send data from server
client.emit("HelloS",{'Hello server':'from client'})

#listen server
@client.on('HelloTooC')
def Set(data):
	print("recieved ",str(data))
	client.disconnect()
print("end")
