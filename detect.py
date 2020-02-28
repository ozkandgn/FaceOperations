import cv2
import numpy as np
from imutils import face_utils

from angle import calculate_angle
from dlib_operations import DlibDetector
from get_eye import SubImage
from cnn import CNN_Detect
from blink_detector import predict_blink_with_classes

def draw_landmark_points(image,landmarks):
	#counter for the color
	#for loop for the draw landmarks(there are 68 landmarks)
	counter = 0
	for (x, y) in landmarks:
		cv2.circle(image, (x, y), 2, (round(counter*3.6), round(counter*3.6), round(counter*3.6)), -1)
		counter+=1
	return image

def detect_angle(img):
	image = np.copy(img)
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

		draw_landmark_points(image,landmarks)
		return (image,landmarks)

def detect_cnn(image,left_landmarks,right_landmarks):
	sub_images = SubImage(image)
	detector = CNN_Detect()

	left_eye_image = sub_images.get_sub_image(left_landmarks)
	right_eye_image = sub_images.get_sub_image(right_landmarks)

	left_eye_cnn = detector.predict(left_eye_image)
	right_eye_cnn = detector.predict(right_eye_image)

	print("left_pre_with_cnn = ",left_eye_cnn)
	print("right_pre_with_cnn = ",right_eye_cnn)

def detect_landmarks(left_landmarks,right_landmarks):
	left_eye_landmarks = predict_blink_with_classes(left_landmarks)
	right_eye_landmarks = predict_blink_with_classes(right_landmarks)

	print("left_pre_with_landmarks = ",left_eye_landmarks)
	print("right_pre_with_landmarks = ",right_eye_landmarks)