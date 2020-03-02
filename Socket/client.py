import socketio as socket #pip install python-socketio
import eventlet

print("client")
client = socket.Client()

client.connect('http://127.0.0.1:5000')


client.emit("HelloS",{'Hello server':'from client'})

@client.on('HelloTooC')
def Set(data):
	print("recieved ",str(data))
	client.disconnect()
print("end")
