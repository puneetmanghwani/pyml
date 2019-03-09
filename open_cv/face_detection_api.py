#!/usr/bin/env python

import cv2


#function to select api which to use
def ask_for_tracker():
    print("select api")
    print("boosting -0: ")
    print("MIL-1: ")
    print("KCF-2: ")
    print("TLD-3: ")
    print("median flow-4: ")
    choice = int(input("Please select your tracker: "))
    
    if choice == 0:
        tracker = cv2.TrackerBoosting_create()
    if choice == 1:
        tracker = cv2.TrackerMIL_create()
    if choice == 2:
        tracker = cv2.TrackerKCF_create()
    if choice == 3:
        tracker = cv2.TrackerTLD_create()
    if choice == 4:
        tracker = cv2.TrackerMedianFlow_create()


    return tracker
 





tracker = ask_for_tracker()
tracker_name = str(tracker).split()[0][1:]


cap = cv2.VideoCapture(0)

#first frame.
ret, frame = cap.read()


#select the roi means which thing you want to detect
roi = cv2.selectROI(frame, False)

# Initialize tracker with first frame and bounding box
ret = tracker.init(frame, roi)

while cap.isOpened():
    #new frame
    ret, frame = cap.read()
    
    
    # Update the tracker
    success, roi = tracker.update(frame)


    #the roi we get is a tuple of 4 floats so we convert them in integers
    (x,y,w,h) = tuple(map(int,roi))
    
    #drawing rectangle according to tracker
    if success:
        # Tracking success
        p1 = (x, y)
        p2 = (x+w, y+h)
        cv2.rectangle(frame, p1, p2, (0,255,0), 3)
    else :
        #if tracker is not able to detect
        cv2.putText(frame, "Failure to Detect Tracking!!", (100,200), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),3)


    cv2.imshow(tracker_name, frame)

  
    if cv2.waitKey(1) & 0xFF == ord('q') :
        
        break

        
cap.release()
cv2.destroyAllWindows()





