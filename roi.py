#!/usr/bin/python3
import cv2

im = cv2.imread("index1.jpeg")
fromCenter=False    
    # Select ROI
r = cv2.selectROI(im,fromCenter)

print('r is------',r)
print('r[0] is-------',r[0])
print('r[1] is----',r[1])
print('r[2] is-----',r[2])
print('r[3] is-----',r[3])
     
    # Crop image
imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

 
    # Display cropped image
cv2.imshow("Image", imCrop)
cv2.waitKey(0)
