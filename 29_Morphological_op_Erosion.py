import cv2
import numpy as np


img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg", cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(img, kernel, iterations=1)

imgResized = cv2.resize(erosion, (500,300))
cv2.imshow("Erosion",imgResized)

