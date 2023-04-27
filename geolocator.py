from tensorflow.keras.layers import Input , Lambda , Dense, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.applications.resnet50 import ResNet50 , preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator , load_img
from tensorflow.keras.models import Sequential
import numpy as np
from glob import glob 
import matplotlib.pyplot as plt 
import os

#original image size >>>
IMAGE_SIZE = [1920,1920]

#add padding to image.

train_folder = "C:/Users/harry/genshin-geolocator/genshin-geolocator/images/train"
validate_folder = "" #put the folder here later

resnetmodel = ResNet50(input_shape = IMAGE_SIZE+[3], )


