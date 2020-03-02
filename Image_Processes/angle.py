def calculate_angle(shape):
	#get angle x of face
	#used malar and nose avarage
	angle_one = ( (shape[28][0] - shape[0][0])/4 - (shape[16][0] - shape[28][0])/4)
	angle_two = ( (shape[30][0] - shape[1][0])/4 - (shape[15][0] - shape[30][0])/4)
	return round((angle_one + angle_two) / 1.75, 4)