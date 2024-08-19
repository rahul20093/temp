import cv2
import numpy as np

img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.array([[0,1,0], [1,-4,1], [0,1,0]])

sharpened = cv2.filter2D(gray, -1, kernel)

imgResized = cv2.resize(sharpened, (500,300))
cv2.imshow("Sharpened",imgResized)
