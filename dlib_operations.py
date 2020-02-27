import dlib
import cv2

class DlibDetector():
	
	def __init__(self,image):
		self.dlib_base_values()
		self.image = image
		self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

	def dlib_base_values(self):
		#initial dlib 
		self.detector = dlib.get_frontal_face_detector()
		
		#dlib predictor file (using HOG and SVM models)
		self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

	def detect_faces(self):
		#function detect faces
		self.rects = self.detector(self.gray, 2)
		return self.rects

	def get_landmarks(self,rect):
		#for the detect all regions(landmarks) in face
		return self.predictor(self.gray, rect)