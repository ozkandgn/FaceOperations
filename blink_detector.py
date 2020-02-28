def predict_blink(shape):
	avg = ((shape[5][1] - shape[1][1]) + (shape[4][1] - shape[2][1]))/2 
	print("avg ",avg)
	# if avg val == 0 eye is open
	if avg>10:
		return 0
	else:
		return 1 - (avg-0.1)/10 # -0.1 to balance

def predict_blink_with_classes(shape):
	result = predict_blink(shape)
	if result < 0.5:
		return 0
	else:
		return 1
