import numpy as np
import argparse
import imutils
import cv2
from imutils import face_utils

from angle import calculate_angle
from dlib_operations import DlibDetector

def get_image(path):
	#get image and return resized image
	image = cv2.imread(path)
	return imutils.resize(image, width=500)

def draw_landmark_points(image,landmarks):
	#counter for the color
	#for loop for the draw landmarks(there are 68 landmarks)
	counter = 0
	for (x, y) in landmarks:
		cv2.circle(image, (x, y), 2, (round(counter*3.6), round(counter*3.6), round(counter*3.6)), -1)
		counter+=1
	return image


if __name__ == '__main__':

	#read gray image
	image = get_image("test_images/1.jpg")

	dlib_detector = DlibDetector(image)

	#each face
	rects = dlib_detector.detect_faces()

	#for loop for each face
	for (i, rect) in enumerate(rects):

		#landmarks (dlib format)
		shape = dlib_detector.get_landmarks(rect)

		#convert shape to array
		landmarks = face_utils.shape_to_np(shape)

		# for draw boinding box
		(x, y, w, h) = face_utils.rect_to_bb(rect)

		# bottom y value of the bounding box
		bottom_box_pos = y + h
		
		#drawing bounding box
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

		(angle_x, angle_y) = calculate_angle(landmarks, bottom_box_pos)

		print("angle_x = ",angle_x)
		print("angle_y = ",angle_y)

		image = draw_landmark_points(image,landmarks)

	cv2.imshow("Output", image)
	cv2.waitKey(0)
