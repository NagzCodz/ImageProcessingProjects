import cv2
import numpy as np

# get the webcam
cap = cv2.VideoCapture(0)

while True:
    # read the frame from the webcam, ret is a boolean that indicates if the frame was read correctly
    ret, frame = cap.read()
    # hsv now contains the frame in HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define the range of the color in HSV space
    # red color range
    lower_color = np.array([160, 100, 100])
    upper_color = np.array([180, 255, 255])
    # create a mask for the color
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # apply the mask to the frame
    # result contains the original frame with the mask applied
    # parameters: src, dst, mask which means the source image, destination image, and mask
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Original Frame", frame)
    cv2.imshow("Red Detection", result)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()    

