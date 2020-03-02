import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
import tensorflow as tf
#for close tensorflow logs

import numpy as np
import argparse
import imutils
import cv2

from .detect import detect_cnn,detect_angle,detect_landmarks,detect_points
from Operations.json_operations import JsonOperations

def get_image(path):
	#get image and return resized image
	image = cv2.imread(path)
	return imutils.resize(image, width=500)

def image_processing(image,counter):
	#read image
	#image = get_image("Image_Processes/test_images/6.jpg")

	#this function detect landmarks(points) on face
	(is_detect,detected_image,landmarks) = detect_landmarks(image)

	if is_detect:
		#this function detect angle of face
		angle = detect_angle(landmarks)

		#left and right eye landmarks
		left_landmarks = landmarks[36:42]
		right_landmarks = landmarks[42:48]

		#this function detect and predict eye with CNN algorithm
		(left_eye_cnn,right_eye_cnn) = detect_cnn(image,left_landmarks,right_landmarks)

		#this function detect and predict eye with point distances
		(left_eye_point,rigth_eye_point) = detect_points(left_landmarks,right_landmarks)

		#for show image
		cv2.imshow("Output", detected_image)
		cv2.waitKey(0)

		#integer to bool
		left_blink = True if left_eye_point==0 else False 
		right_blink = True if rigth_eye_point==0 else False

		#return values for read json log file
		return (True,counter,angle,left_blink,right_blink)

	else:
		print("cannot find face")

def video_processing(video_name):
	cap = cv2.VideoCapture(video_name)
	#counter for frame control
	counter = 0
	json = JsonOperations()

	while (cap.isOpened()):
		ret,frame = cap.read()
		#per ten frame
		if counter%10==0:
			if ret:
				#processed image values sending json write
				json.add_log(image_processing(frame,counter))
		counter+=1
	#in last all operations json file writing
	json.write_json()