import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)

path = "C:/Users/Rahul/Pictures/wallpapers/oppie.jpg"
img =cv2.imread(path)


imgCanny = cv2.Canny(img,500,500)

imgDilation = cv2.dilate(imgCanny,kernel , iterations = 4)
imgEroded = cv2.erode(imgDilation,kernel,iterations=2)
 
imgResized = cv2.resize(imgEroded, (500,300))

cv2.imshow("Img Erosion",imgResized)
cv2.waitKey(0)
