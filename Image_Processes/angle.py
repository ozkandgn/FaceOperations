def calculate_angle(shape,bottom_box_pos):
	return (calculate_angle_x(shape),calculate_angle_y(shape,bottom_box_pos))

def calculate_angle_x(shape):
	#get angle x of face
	#used malar and nose avarage
	angle_one = ( (shape[28][0] - shape[0][0])/4 - (shape[16][0] - shape[28][0])/4)
	angle_two = ( (shape[30][0] - shape[1][0])/4 - (shape[15][0] - shape[30][0])/4)
	return round((angle_one + angle_two) / 1.75, 4)

def calculate_angle_y(shape,bottom_box_pos):
	#get angle y of face
	#used chin and bottom avarage on shapes
	bottom_shape_pos = ((shape[5][1] + shape[11][1])/2 + (shape[6][1] + shape[10][1])/2 + (shape[7][1] + shape[9][1])/2)/3.05
	low_angle_y = bottom_shape_pos - bottom_box_pos
	return round(low_angle_y*2.5, 4)