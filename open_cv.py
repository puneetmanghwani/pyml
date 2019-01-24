#!/usr/bin/python3

import cv2,time

cap=cv2.VideoCapture(0)



status,frame=cap.read()
if status:
	frame = cv2.resize(status, (0, 0), .25, .25)

	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)



	#numpy_vertical = np.vstack((frame, grey))
	numpy_horizontal = np.hstack((frame,grey))

	#numpy_vertical_concat = np.concatenate((image, grey_3_channel), axis=0)
	#numpy_horizontal_concat = np.concatenate((image, grey_3_channel), axis=1)

	#cv2.imshow('Main', image)
	#cv2.imshow('Numpy Vertical', numpy_vertical)
	cv2.imshow('Numpy Horizontal', numpy_horizontal)
	#cv2.imshow('Numpy Vertical Concat', numpy_vertical_concat)
	c#v2.imshow('Numpy Horizontal Concat', numpy_horizontal_concat)

	#cv2.waitKey()






	#cv2.imshow('camera',frame)
	  
	cv2.waitKey(0)

	cap.release()
	cv2.destroyAllWindows()
