import cv2,os
#from sklearn.externals import joblib
import numpy as np
import csv
import tensorflow as tf

import numpy
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
import keras.backend.tensorflow_backend as tfback
from keras import backend as K
K.common.set_image_dim_ordering('th')
from keras.models import model_from_json
def _get_available_gpus():

    if tfback._LOCAL_DEVICES is None:
        devices = tf.config.list_logical_devices()
        tfback._LOCAL_DEVICES = [x.name for x in devices]
    return [x for x in tfback._LOCAL_DEVICES if 'device:gpu' in x.lower()]


tfback._get_available_gpus = _get_available_gpus
json_file = open('model_final.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model_final.h5")
im=cv2.imread("adil.png")
im2 = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
train_data=[]
im2=cv2.GaussianBlur(im2,(15,15),0)
im2=cv2.resize(im2,(28,28),interpolation=cv2.INTER_AREA)
thresh = 230
im2_bw = cv2.threshold(im2, thresh, 255, cv2.THRESH_BINARY)[1]
im2_ibw = (255-im2_bw)
#cv2.imshow("okk",im2_ibw)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
im2_ibw=np.reshape(im2_ibw,(1,28,28))

train_data.append(im2_ibw)
train_data[0]=np.array(train_data[0])
train_data[0]=train_data[0].reshape(1,1,28,28)
result=loaded_model.predict_classes(train_data[0])
s=''

if (result[0] == 10):
    s = s + '-'
if (result[0] == 11):
    s = s + '+'
if (result[0] == 12):
    s = s + '*'
if (result[0] == 0):
    s = s + '0'
if (result[0] == 1):
    s = s + '1'
if (result[0] == 2):
    s = s + '2'
if (result[0] == 3):
    s = s + '3'
if (result[0] == 4):
    s = s + '4'
if (result[0] == 5):
    s = s + '5'
if (result[0] == 6):
    s = s + '6'
if (result[0] == 7):
    s = s + '7'
if (result[0] == 8):
    s = s + '8'
if (result[0] == 9):
    s = s + '9'

print(s)