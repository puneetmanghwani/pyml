#!/usr/bin/ python3

import numpy as np
import cv2 



cap=cv2.VideoCapture('http://10.139.212.14:8080//video?x.mjpg')


# Parameters for ShiTomasi corner detection
corner_track_params = dict(maxCorners = 10,
                       qualityLevel = 0.3,
                       minDistance = 15,
                       blockSize = 7 )

# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (200,200),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10,0.03))

ret, prev_frame = cap.read()
# Grab a grayscale image (as the previous frame)
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

# Grabbing the corners
prevPts = cv2.goodFeaturesToTrack(prev_gray, mask = None, **corner_track_params)

print(prevPts)

# Create a matching mask of the previous frame for drawing on later
mask = np.zeros_like(prev_frame)

while cap.isOpened():
    


    # Grab current frame
    ret,frame = cap.read()
    
    # Grab gray scale
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  
    # Calculate the Optical Flow on the Gray Scale Frame
    nextPts, status, err = cv2.calcOpticalFlowPyrLK(prev_gray, frame_gray, prevPts, None, **lk_params)
    
    # Using the returned status array (the status output)
    # each element of the vector is set to 1 if the flow for the corresponding features has been found, otherwise, it is set to 0. 
  
    #print(nextPts)
    #print('------------$&^*^&)(&^%$%$^&(*^%$#%$@#%^)&^%$^@^&*&^%$#@%^&*^%#$@%%&^*')
    #print(status)
    #print('------------$&^*^&)(&^%$%$^&(*^%$#%$@#%^)&^%$^@^&*&^%$#@%^&*^%#$@%%&^*')
    #print(err)
    #print('------------$&^*^&)(&^%$%$^&(*^%$#%$@#%^)&^%$^@^&*&^%$#@%^&*^%#$@%%&^*')
    good_new = nextPts[status==1]
    good_prev = prevPts[status==1]

    for i,(new,prev) in enumerate(zip(good_new,good_prev)):
        
        x_new,y_new = new.ravel()
        x_prev,y_prev = prev.ravel()
        
        # Lines will be drawn using the mask created from the first frame
        mask = cv2.line(mask, (x_new,y_new),(x_prev,y_prev), (0,255,0), 3)
        
        # Draw red circles at corner points
        frame = cv2.circle(frame,(x_new,y_new),8,(0,0,255),-1)
    

    img = cv2.add(frame,mask)
    cv2.imshow('frame',img)
    

   
    # Now update the previous frame and previous points
    prev_gray = frame_gray.copy()
    prevPts = good_new.reshape(-1,1,2)

    if cv2.waitKey(1) & 0xFF == ord('q') :
        
        break

cv2.destroyAllWindows()
cap.release()



#print(prevPts.shape)

