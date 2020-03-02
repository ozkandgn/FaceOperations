import pandas as pd
import cv2
import os

from .image_filters import black_and_white


def read_images(path):
    first=True
    images=[]
    outs=[]
    for i in os.listdir(path):
        if i.endswith('.jpg') or i.endswith('.png') or i.endswith('.jpeg'):
            img = cv2.imread(path+"/"+i,0)
            img = cv2.resize(img,(image_x,image_y))
            img = black_and_white(img)
            #cv2.imread("1",img)
            #cv2.waitKey(3000)
            img=pd.DataFrame(data=img)
            img=img.values.reshape(1,(image_x*image_y))
            img=pd.DataFrame(data=img)
            outs.append(int(i[0])-1)
            
            if first:
                first=False
                images=img
            else:
                images=pd.concat([images,img])
    return (images,outs)