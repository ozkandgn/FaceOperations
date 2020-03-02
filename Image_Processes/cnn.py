import cv2
import numpy as np
import pandas as pd
from keras.models import load_model

from .image_filters import black_and_white

#eye image size
image_x = 45
image_y = 10

class CNN_Detect():
    def __init__(self):
    		#model file
        self.model = load_model("Image_Processes/model.h5")

    def predict(self,img):
        img = cv2.resize(img,(image_x,image_y))
        #gray image to 0-1 black and white image
        img =black_and_white(img)
        #cv2.imshow("2",img)
        #cv2.waitKey(0)
        
        #reshaping operations
        img=pd.DataFrame(data=img)
        img=img.values.reshape(1,(image_x*image_y))
        img=pd.DataFrame(data=img)
        test = np.copy(img)
        test/=255.0
        test=test.values.reshape(-1,image_x,image_y,1)
        pred = self.model.predict_classes(test)
        return pred