import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
import tensorflow as tf
#for close tensorflow logs

import numpy as np
import argparse
import imutils
import cv2

from .detect import detect_cnn,detect_angle,detect_landmarks,detect_points

def get_image(path):
	#get image and return resized image
	image = cv2.imread(path)
	return imutils.resize(image, width=500)

def image_processing(image):
	#read image
	#image = get_image("Image_Processes/test_images/6.jpg")

	(detected_image,landmarks) = detect_landmarks(image)

	angle = detect_angle(landmarks)

	left_landmarks = landmarks[36:42]
	right_landmarks = landmarks[42:48]

	(left_eye_cnn,right_eye_cnn) = detect_cnn(image,left_landmarks,right_landmarks)

	(left_eye_point,rigth_eye_point) = detect_points(left_landmarks,right_landmarks)

	cv2.imshow("Output", detected_image)
	cv2.waitKey(0)

def video_processing(video_name):
	cap = cv2.VideoCapture(video_name)
	while (cap.isOpened()):
		_,frame = cap.read()
		image_processing(frame)

