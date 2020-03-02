import json

class JsonOperations():
	def __init__(self):
		#creating a dictionary for json
		self.data = {}

	def add_log(self,face_detected,frame,angle,left_blink,right_blink):
		#add data
		self.data[frame] = {"face_detected":face_detected,"frame":frame,"angle":angle,"left_blink":left_blink,"right_blink":right_blink}

	def write_json(self):
		#create and write json file
		with open("logs.json", 'w') as f:
			json.dump(self.data, f,indent=2)