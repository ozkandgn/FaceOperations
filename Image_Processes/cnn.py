import cv2
import numpy as np
import pandas as pd
from keras.models import load_model

from .image_filters import black_and_white
from .read_file import read_images

image_x = 45
image_y = 10

class CNN_Detect():
    def __init__(self):
        self.model = load_model("Image_Processes/model.h5")

    def predict(self,img):
        img = cv2.resize(img,(image_x,image_y))
        img =black_and_white(img)
        #cv2.imshow("2",img)
        #cv2.waitKey(0)
        img=pd.DataFrame(data=img)
        img=img.values.reshape(1,(image_x*image_y))
        img=pd.DataFrame(data=img)
        test = img
        test/=255.0
        test=test.values.reshape(-1,image_x,image_y,1)
        pred = self.model.predict_classes(test)
        return pred

    def train(self):
	    x_train,y_train=read_images("path_to_dataset")
	    
	    x_train/=255.0
	    x_train=x_train.values.reshape(-1,image_x,image_y,1)
	    y_train=to_categorical(y_train,num_classes=2)
	    
	    x_train,x_test,y_train,y_test=train_test_split(x_train,y_train,\
	                                    test_size=0.1,random_state=2)
	    
	    model=Sequential()
	    
	    model.add(Conv2D(filters = 8, kernel_size = (5,5),padding = 'Same',\
	                     activation ='relu', input_shape = (image_x,image_y,1)))
	    model.add(MaxPool2D(pool_size=(2,2)))
	    model.add(Dropout(0.25))
	    
	    model.add(Conv2D(filters = 8, kernel_size = (3,3),padding = 'Same',\
	                     activation ='relu'))
	    model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))
	    model.add(Dropout(0.25))
	    
	    model.add(Flatten())
	    
	    model.add(Dense(128, activation = "relu"))
	    model.add(Dropout(0.1))
	    model.add(Dense(64, activation = "relu"))
	    model.add(Dropout(0.25))
	    model.add(Dense(32, activation = "relu"))
	    model.add(Dropout(0.25))
	    model.add(Dense(2, activation = "softmax"))
	    
	    optimizer = optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999)
	    
	    model.compile(optimizer=optimizer,loss="categorical_crossentropy",\
	                  metrics=["accuracy"])
	    
	    batch_size=1000
	    model.fit(x_train,y_train,batch_size = batch_size,epochs= 1000)
	    model.save("Image_Processing/model.h5")