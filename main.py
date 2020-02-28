import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
import tensorflow as tf
#for close tensorflow logs

import numpy as np
import argparse
import imutils
import cv2

from detect import detect_cnn,detect_angle,detect_landmarks

def get_image(path):
	#get image and return resized image
	image = cv2.imread(path)
	return imutils.resize(image, width=500)

if __name__ == '__main__':

	#read image
	image = get_image("test_images/6.jpg")

	(detected_image,landmarks) = detect_angle(image)

	left_landmarks = landmarks[36:42]
	right_landmarks = landmarks[42:48]

	detect_cnn(image,left_landmarks,right_landmarks)

	detect_landmarks(left_landmarks,right_landmarks)

	cv2.imshow("Output", detected_image)
	cv2.waitKey(0)