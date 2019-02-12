#!/usr/bin/python3
import cv2
import numpy as np

image = cv2.imread('ultra.png')

#image = cv2.resize(image, (0, 0), None, .50, .50)    
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Make the grey scale image have three channels

grey_3_channel = cv2.cvtColor(grey, cv2.COLOR_GRAY2BGR)

#numpy_horizontal = np.hstack((image, grey_3_channel))

numpy_horizontal_concat = np.concatenate((image, grey_3_channel), axis=1)
#numpy_vertical_concat = np.concatenate((image, grey_3_channel), axis=0)




cv2.imshow('Numpy Horizontal Concat', numpy_horizontal_concat)
#cv2.imshow('Numpy Horizontal Concat1', numpy_vertical_concat)
cv2.waitKey()
