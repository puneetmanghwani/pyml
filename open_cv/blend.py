#!/usr/bin/python3
import cv2


im = cv2.imread("goku.jpg")
fromCenter=False    
    # Select ROI
r = cv2.selectROI(im,fromCenter)

#select roi
r1 = cv2.selectROI(im,fromCenter)

    # Crop image

imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
imCrop1 = im[int(r1[1]):int(r1[1]+r1[3]), int(r1[0]):int(r1[0]+r1[2])]


width,height=imCrop1.shape[1],imCrop1.shape[0]
image=cv2.resize(imCrop,(width,height))


rows,cols,channels = image.shape
roi = im[int(r1[1]):int(r1[1]+r1[3]), int(r1[0]):int(r1[0]+r1[2])]
# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask= mask_inv)
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(image,image,mask = mask)
# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
im[int(r1[1]):int(r1[1]+r1[3]), int(r1[0]):int(r1[0]+r1[2])] = dst
cv2.imshow('res',im)
cv2.waitKey(0)
cv2.destroyAllWindows()

