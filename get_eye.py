import cv2

class SubImage():
	def __init__(self,image):
		self.image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

	def get_sub_image(self,shape):
		x_pos = [i[0] for i in shape]
		y_pos = [i[1] for i in shape]
		self.image = cv2.medianBlur(self.image,5)
		return self.image[min(y_pos):max(y_pos),min(x_pos):max(x_pos)]
