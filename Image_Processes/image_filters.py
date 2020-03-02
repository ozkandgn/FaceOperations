import numpy as np

def black_and_white(image):
	avg = np.average(image)
	#gray image to 0-1 image
	for i in range(len(image)):
	    for j in range(len(image[i])):
	        if image[i,j] > avg:
	            image[i,j] = 1
	        else:
	            image[i,j] = 0
	return image * 255