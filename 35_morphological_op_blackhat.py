import cv2
import numpy as np


img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg", cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5,5), np.uint8)

tophat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

imgResized = cv2.resize(tophat, (500,300))

cv2.imshow("Black Hat",imgResized)
